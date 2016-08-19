#!/usr/bin/env python2
# -*- coding: utf-8-*-
import os
import wave
import json
import tempfile
import logging
import urllib
import urlparse
import re
import subprocess
from abc import ABCMeta, abstractmethod
import requests
import yaml
import jasperpath
import diagnose
import vocabcompiler
import datetime

class AbstractSTTEngine(object):
    """
    Generic parent class for all STT engines
    """

    __metaclass__ = ABCMeta
    VOCABULARY_TYPE = None

    @classmethod
    def get_config(cls):
        return {}

    @classmethod
    def get_instance(cls, vocabulary_name, phrases):
        config = cls.get_config()
        if cls.VOCABULARY_TYPE:
            vocabulary = cls.VOCABULARY_TYPE(vocabulary_name,
                                             path=jasperpath.config(
                                                 'vocabularies'))
            if not vocabulary.matches_phrases(phrases):
                vocabulary.compile(phrases)
            config['vocabulary'] = vocabulary
        instance = cls(**config)
        return instance

    @classmethod
    def get_passive_instance(cls):
        phrases = vocabcompiler.get_keyword_phrases()
        return cls.get_instance('keyword', phrases)

    @classmethod
    def get_active_instance(cls):
        phrases = vocabcompiler.get_all_phrases()
        return cls.get_instance('default', phrases)

    @classmethod
    @abstractmethod
    def is_available(cls):
        return True

    @abstractmethod
    def transcribe(self, fp):
        pass

'''
class PocketSphinxSTT(AbstractSTTEngine):
    """
    The default Speech-to-Text implementation which relies on PocketSphinx.
    """

    SLUG = 'sphinx'
    VOCABULARY_TYPE = vocabcompiler.PocketsphinxVocabulary

    def __init__(self, vocabulary, hmm_dir="/usr/local/share/" +
                 "pocketsphinx/model/hmm/en_US/hub4wsj_sc_8k"):

        """
        Initiates the pocketsphinx instance.

        Arguments:
            vocabulary -- a PocketsphinxVocabulary instance
            hmm_dir -- the path of the Hidden Markov Model (HMM)
        """

        self._logger = logging.getLogger(__name__)

        # quirky bug where first import doesn't work
        try:
            import pocketsphinx as ps
        except:
            import pocketsphinx as ps

        with tempfile.NamedTemporaryFile(prefix='psdecoder_',
                                         suffix='.log', delete=False) as f:
            self._logfile = f.name

        self._logger.debug("Initializing PocketSphinx Decoder with hmm_dir " +
                           "'%s'", hmm_dir)

        # Perform some checks on the hmm_dir so that we can display more
        # meaningful error messages if neccessary
        if not os.path.exists(hmm_dir):
            msg = ("hmm_dir '%s' does not exist! Please make sure that you " +
                   "have set the correct hmm_dir in your profile.") % hmm_dir
            self._logger.error(msg)
            raise RuntimeError(msg)
        # Lets check if all required files are there. Refer to:
        # http://cmusphinx.sourceforge.net/wiki/acousticmodelformat
        # for details
        missing_hmm_files = []
        for fname in ('mdef', 'feat.params', 'means', 'noisedict',
                      'transition_matrices', 'variances'):
            if not os.path.exists(os.path.join(hmm_dir, fname)):
                missing_hmm_files.append(fname)
        mixweights = os.path.exists(os.path.join(hmm_dir, 'mixture_weights'))
        sendump = os.path.exists(os.path.join(hmm_dir, 'sendump'))
        if not mixweights and not sendump:
            # We only need mixture_weights OR sendump
            missing_hmm_files.append('mixture_weights or sendump')
        if missing_hmm_files:
            self._logger.warning("hmm_dir '%s' is missing files: %s. Please " +
                                 "make sure that you have set the correct " +
                                 "hmm_dir in your profile.",
                                 hmm_dir, ', '.join(missing_hmm_files))

        self._decoder = ps.Decoder(hmm=hmm_dir, logfn=self._logfile,
                                   **vocabulary.decoder_kwargs)

    def __del__(self):
        os.remove(self._logfile)

    @classmethod
    def get_config(cls):
        # FIXME: Replace this as soon as we have a config module
        config = {}
        # HMM dir
        # Try to get hmm_dir from config
        profile_path = jasperpath.config('profile.yml')

        if os.path.exists(profile_path):
            with open(profile_path, 'r') as f:
                profile = yaml.safe_load(f)
                try:
                    config['hmm_dir'] = profile['pocketsphinx']['hmm_dir']
                except KeyError:
                    pass

        return config

    def transcribe(self, fp):
        """
        Performs STT, transcribing an audio file and returning the result.

        Arguments:
            fp -- a file object containing audio data
        """

        fp.seek(44)

        # FIXME: Can't use the Decoder.decode_raw() here, because
        # pocketsphinx segfaults with tempfile.SpooledTemporaryFile()
        data = fp.read()
        self._decoder.start_utt()
        self._decoder.process_raw(data, False, True)
        self._decoder.end_utt()

        result = self._decoder.get_hyp()
        with open(self._logfile, 'r+') as f:
            for line in f:
                self._logger.debug(line.strip())
            f.truncate()

        transcribed = [result[0]]
        self._logger.info('Transcribed: %r', transcribed)
        return transcribed

    @classmethod
    def is_available(cls):
        return diagnose.check_python_import('pocketsphinx')



'''


class WitAiSTT(AbstractSTTEngine):
    """
    Speech-To-Text implementation which relies on the Wit.ai Speech API.

    This implementation requires an Wit.ai Access Token to be present in
    profile.yml. Please sign up at https://wit.ai and copy your instance
    token, which can be found under Settings in the Wit console to your
    profile.yml:
        ...
        stt_engine: witai
        witai-stt:
          access_token:    ERJKGE86SOMERANDOMTOKEN23471AB
    """

    SLUG = "witai"

    def __init__(self, access_token):
        self._logger = logging.getLogger(__name__)
        self.token = access_token

    @classmethod
    def get_config(cls):
        # FIXME: Replace this as soon as we have a config module
        config = {}
        # Try to get wit.ai Auth token from config
        profile_path = jasperpath.config('profile.yml')
        if os.path.exists(profile_path):
            with open(profile_path, 'r') as f:
                profile = yaml.safe_load(f)
                if 'witai-stt' in profile:
                    if 'access_token' in profile['witai-stt']:
                        config['access_token'] = \
                            profile['witai-stt']['access_token']
        return config

    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, value):
        self._token = value
        self._headers = {'Authorization': 'Bearer %s' % self.token,
                         'accept': 'application/json',
                         'Content-Type': 'audio/wav'}

    @property
    def headers(self):
        return self._headers

    def transcribe(self, fp):
        data = fp.read()
        r = requests.post('https://api.wit.ai/speech?v=20150101',
                          data=data,
                          headers=self.headers)
        try:
            r.raise_for_status()
            text = r.json()['_text']
        except requests.exceptions.HTTPError:
            self._logger.critical('Request failed with response: %r',
                                  r.text,
                                  exc_info=True)
            return []
        except requests.exceptions.RequestException:
            self._logger.critical('Request failed.', exc_info=True)
            return []
        except ValueError as e:
            self._logger.critical('Cannot parse response: %s',
                                  e.args[0])
            return []
        except KeyError:
            self._logger.critical('Cannot parse response.',
                                  exc_info=True)
            return []
        else:
            transcribed = []
            if text:
                transcribed.append(text.upper())
            self._logger.info('Transcribed: %r', transcribed)
            return transcribed

    @classmethod
    def is_available(cls):
        return diagnose.check_network_connection()


def get_engine_by_slug(slug=None):
    """
    Returns:
        An STT Engine implementation available on the current platform

    Raises:
        ValueError if no speaker implementation is supported on this platform
    """

    if not slug or type(slug) is not str:
        raise TypeError("Invalid slug '%s'", slug)

    selected_engines = filter(lambda engine: hasattr(engine, "SLUG") and
                              engine.SLUG == slug, get_engines())
    if len(selected_engines) == 0:
        raise ValueError("No STT engine found for slug '%s'" % slug)
    else:
        if len(selected_engines) > 1:
            print(("WARNING: Multiple STT engines found for slug '%s'. " +
                   "This is most certainly a bug.") % slug)
        engine = selected_engines[0]
        if not engine.is_available():
            raise ValueError(("STT engine '%s' is not available (due to " +
                              "missing dependencies, missing " +
                              "dependencies, etc.)") % slug)
        return engine


def get_engines():
    def get_subclasses(cls):
        subclasses = set()
        for subclass in cls.__subclasses__():
            subclasses.add(subclass)
            subclasses.update(get_subclasses(subclass))
        return subclasses
    return [tts_engine for tts_engine in
            list(get_subclasses(AbstractSTTEngine))
            if hasattr(tts_engine, 'SLUG') and tts_engine.SLUG]
