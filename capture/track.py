'''
Created on Aug 7, 2013

@author: pavan
'''

from subprocess import Popen, PIPE
import re, time
import datalib, application

def main():    
    while True:
        apps = datalib.Database().get_appliction_list()    
        x = get_active_window_title(apps)
        print str(x)
        time.sleep(2)

def get_active_window_title(apps):     
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
                    app = db.app_exists(str(match.group("app")).replace("\"",""),apps)
                    if app != '':
                        print 'return - ' + app.application
                        return app
                    else:
                        newapp = application.Application(match.group("app"),match.group("class"),'')                        
                        db.add_new_application(newapp)                        
                        
        return ''

if __name__ == "__main__":
    main()