'''
Created on 19 Feb 2014

@author: richard.m
'''
# For writing output to the log

# imports
import datetime

LOG_PATH="c:/log/toolscleanup.log"

def get_time():
    """gets the current date & time"""
    return datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

def log_entry(machine_name="test", event="test", outcome="test"):
    """takes the time stamp, machine_name and event and adds them to the log file"""
    # Open the log file
    if (open(LOG_PATH, 'a')):
        log = open(LOG_PATH, 'a')
    else:
        log = open(LOG_PATH, 'w')
                       
    # Write to the log file
    log.write(get_time()+" - "+machine_name+" - "+event+" - "+outcome+"\n")
    
    # Close the log file
    log.close()
    return