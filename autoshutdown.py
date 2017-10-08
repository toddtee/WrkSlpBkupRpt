#! /usr/bin/python

import os
import time
import subprocess

#declare system user
user = #zoidberg

#Time from keyboard for sleep process to start (minutes)
afk_mins = #10

#Time to recheck afk time (seconds)
retryTimer = #300

#Time PC sleeps until wakesup (minutes)
sleepTime_mins = #120

#time conversion to suit argument requirements
afk = afk_mins * 60 * 1000 #milliseconds
sleepTime = sleepTime_mins * 60 #seconds



while True:
    idleTime = int(subprocess.check_output(["'sudo', '-u', %s, 'env', 'DISPLAY=:0', 'xprintidle'" % user]))
    if idleTime<afk: 
        time.sleep(retryTimer) #checks idle time and sleeps execution 
    else:
        os.system('sudo rtcwake -m off -s %s' % sleepTime)
        
    
    

