# -*- coding: utf-8-*-
import re
from imdb import IMDb
import os
import datetime
fileDir = os.path.dirname(os.path.realpath('__file__'))

WORDS = ["MOVIE", "MOVIES", "YES","CINEMA","DRAMA"]

def format_names(people):
    del people[5:] # Max of 5 people listed
    ret = ''
    for person in people:
        ret += '%s.  ' %person.get('name')
    return ret.strip('. ')

def yes(text):
    return bool(re.search(r'\b(yes)\b', text, re.IGNORECASE))

def isValid(text):
    return bool(re.search(r'\b(movie|movies|cinema|Drama)\b', text, re.IGNORECASE))

def logdata(filename,text):
    date_string = datetime.datetime.now()
    issue_time = str(date_string.year) +'-' + str(date_string.month) +'-' + str(date_string.day) +','+ str(date_string.hour) +':'+ str(date_string.minute) +':'+ str(date_string.second)
    filename = os.path.join(fileDir, '../Logs/'+filename)
    filename = os.path.abspath(os.path.realpath(filename))
    with open(filename, "a") as myfile:
        print("Name of the file: ", myfile.name)
        print("Opening mode : ", myfile.mode)
        myfile.write('"' +text + '"' + ',' + issue_time + '\n')
        myfile.close()
        print("File Closed : ", myfile.closed)
    return 


def handle(text, mic, profile):
    mic.say('What movie?')
    movie_name = mic.activeListen()
    mic.say('Searching top five results for.  %s' %movie_name)
    ia = IMDb()
    movie_query = ia.search_movie(movie_name)
    del movie_query[5:]
    for movie in movie_query:
        mic.say('Did you mean %s (%s)?' %(movie.get('title'), movie.get('year')))
        response = mic.activeListen()
        if yes(response):
            ia.update(movie)
            filename = "Movie.CSV"
            text = '%s' %movie.get('title')
            if movie.get('rating'): 
                movie_info += 'Rating.  %s out of 10.  ' %movie.get('rating')
            if movie.get('runtimes'): 
                movie_info += 'Runtime.  %s minutes.  ' %movie.get('runtimes')[0]
            if movie.get('genres'): 
                movie_info += 'Genres.  %s.  ' %'.  '.join(movie.get('genres'))
                text += ',"' + '%s' %'.  '.join(movie.get('genres')) + '"'
            if movie.get('plot outline'): 
                movie_info += 'Plot.  %s  ' %movie.get('plot outline')
            if movie.get('director'): 
                movie_info += 'Directors.  %s.  ' %format_names(movie.get('director'))
            if movie.get('producer'): 
                movie_info += 'Producers.  %s.  ' %format_names(movie.get('producer'))
            if movie.get('cast'): 
                movie_info += 'Cast.  %s.  ' %format_names(movie.get('cast'))
                text+= ',"'+ '%s' %format_names(movie.get('cast') +'"'
            logdata(filename,text)
            mic.say(movie_info)
        return
    mic.say('Unable to find information on the requested movie')
