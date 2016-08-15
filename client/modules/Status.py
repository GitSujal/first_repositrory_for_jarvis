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
     def getdiskspace():
        p = os.popen("df -h /")
        i = 0
        while 1:
            i = i +1
            line = p.readline()
            if i==2:
                return(line.split()[1:5])

    w = getdiskspace()
    w1 = w[3]
    w2 = w[2].replace("M","")
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
    message = ("CPU temperature is %s degrees celsius." %temp)
    message2 = ("Disk is %s full and has %s megabytes left" %(w1, w2))

    response = "I am currently running on %s version %s.  " %(os1, version)
    response += "This system is named %s and has %s CPU cores.  " %(name, cores)
    response += "Current CPU utilization is %s percent.  " %cpu_percent
    response += message
    response += "Current memory utilization is %s percent." %memory_percent
    response += message2
    
    mic.say(response)
