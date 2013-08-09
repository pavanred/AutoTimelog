'''
Created on Aug 7, 2013

@author: pavan
'''

from subprocess import Popen, PIPE
import re, time
import datalib, application
from apscheduler.scheduler import Scheduler
import logging 

def main():
    clear_session_data()  
    logging.basicConfig()  
    sched = Scheduler(standalone=True)    
    sched.add_interval_job(activity_tracking_job, minutes=1)
    sched.start()
    #capture_interval = int(db.get_config_value('capture_interval')) #in seconds 

def activity_tracking_job():
    db = datalib.Database()
    active_app = get_active_window_title()
    if active_app != '':
        db.record_activity(active_app.appid)   
     
def clear_session_data():
    db = datalib.Database()
    db.clear_session_data()
     
def get_active_window_title():  
    try:   
        root_check = ''
        root = Popen(['xprop', '-root'],  stdout=PIPE)
    
        if root.stdout != root_check:
            root_check = root.stdout
    
            for i in root.stdout:
                if '_NET_ACTIVE_WINDOW(WINDOW):' in i:
                    id_ = i.split()[4]
                    id_w = Popen(['xprop', '-id', id_], stdout=PIPE)
            id_w.wait()
            buff = []
            for j in id_w.stdout:
                buff.append(j)
    
            for line in buff:
                #print line
                match = re.match("WM_CLASS\((?P<type>.+)\) = (?P<class>.+), (?P<app>.+)", line)
                if match != None:
                    mtype = match.group("type")
                    if mtype == "STRING" or mtype == "COMPOUND_TEXT":
                        db = datalib.Database()
                        apps = db.get_appliction_list()    
                        app = db.app_exists(str(match.group("app")).replace("\"",""),apps)
                        if app != '':
                            #print 'return - ' + app.application
                            return app
                        else:
                            newapp = application.Application(match.group("app"),match.group("class"),'')                        
                            db.add_new_application(newapp)                        
                            
            return ''
    except:
        print 'AutoTimelog - Error tracking activity'

if __name__ == "__main__":
    main()