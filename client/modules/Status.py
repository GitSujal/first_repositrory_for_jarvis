# -*- coding: utf-8-*-
import re
import psutil
import platform
import datetime
import os

WORDS = ["STATUS"]

def isValid(text):
    return bool(re.search(r'\b(status)\b', text, re.IGNORECASE))

def handle(text, mic, profile):
    os1, name, version, _, _, _ = platform.uname()
    version = version.split('-')[0]
    cores = psutil.cpu_count()
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory()[2]
    disk_percent = psutil.disk_usage('/')[3]
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    running_since = boot_time.strftime("%A %d. %B %Y")
    t = os.popen('vcgencmd measure_temp').readline()
    temp = t.replace("temp=","").replace("'C\n","")
    message = ("cpu temperature is %s degrees celsius." %temp)

    response = "I am currently running on %s version %s.  " %(os1, version)
    response += "This system is named %s and has %s CPU cores.  " %(name, cores)
    response += "Current CPU utilization is %s percent.  " %cpu_percent
    response += "Current memory utilization is %s percent." %memory_percent
    response += message
    mic.say(response)
