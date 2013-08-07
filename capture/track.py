'''
Created on Aug 7, 2013

@author: pavan
'''

from subprocess import Popen, PIPE
import re, time

def main():
    while True:
        print get_active_window_title()
        time.sleep(5)

def get_active_window_title():
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
            match = re.match("WM_NAME\((?P<type>.+)\) = (?P<name>.+)", line)
            if match != None:
                mtype = match.group("type")
                if mtype == "STRING" or mtype == "COMPOUND_TEXT":
                    return match.group("name")
        return "Active window not found"

if __name__ == "__main__":
    main()