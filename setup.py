'''
Created on Aug 7, 2013

@author: pavan
'''
from pysqlite2 import dbapi2 as sqlite
import os, sys

def main():
    print '***AutoTimelog v0.1 setup***'
    
    try:
        pathname = os.path.dirname(sys.argv[0])
        fullpath = os.path.abspath(pathname)
        if not os.path.exists(fullpath + '/data'):
            os.makedirs(fullpath + '/data')
            
        print 'creating sqlite database...'
        connection = sqlite.connect(fullpath + '/data/timelog.sqlite')
        cursor = connection.cursor()
        
        print 'executing ddls'
        #appliction list
        cursor.execute('CREATE TABLE application ' +
                        '(id INTEGER NOT NULL, ' +
                        'name VARCHAR(50), ' +
                        'class VARCHAR(50), ' +
                        ' PRIMARY KEY (id));')
        
        #activities of current session 
        cursor.execute('CREATE TABLE activity_session ' +
                        '(appid INTEGER NOT NULL, ' +
                        'hours INTEGER NOT NULL, ' +
                        'minutes INTEGER NOT NULL, ' +
                        'FOREIGN KEY(appid) REFERENCES application(id));')
            
        #activity lifetime
        cursor.execute('CREATE TABLE activity_lifetime ' +
                        '(appid INTEGER NOT NULL, ' +
                        'days INTEGER NOT NULL, ' +
                        'hours INTEGER NOT NULL, ' +
                        'minutes INTEGER NOT NULL, ' +
                        'FOREIGN KEY(appid) REFERENCES application(id));')
        
        connection.commit()
            
        print 'setup complete'
    
    except:
        raise

if __name__ == "__main__":
    main()

        