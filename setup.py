'''
Created on Aug 7, 2013

@author: pavan
'''
from pysqlite2 import dbapi2 as sqlite

class Setup(object):
    '''
    application setup 
    '''
    def makedb(self):
        connection = sqlite.connect('data/timelog.sqlite')
        cursor = connection.cursor()
        
        #appliction list
        cursor.execute('CREATE TABLE application ' +
                       '(id INTEGER NOT NULL, ' +
                       'name VARCHAR(50), ' +
                       'class VARCHAR(50), ' +
                       ' PRIMARY KEY (id));')
        
        #capture lookup - daily / weekly / montly 
        cursor.execute('CREATE TABLE capturetype ' + 
                       '(id INTEGER NOT NULL, ' +
                       'type VARCHAR(10), ' +
                       'PRIMARY KEY (id));')
        
        #log 
        cursor.execute('CREATE TABLE log ' +
                       '(appid INTEGER NOT NULL, ' +
                       'duration REAL NOT NULL, ' +
                       'capturetype INTEGER NOT NULL, '+
                       'FOREIGN KEY(appid) REFERENCES application(id), ' +
                       'FOREIGN KEY(capturetype) REFERENCES capturetype(id));')
        
        #configuration values
        cursor.execute('CREATE TABLE config ' +
                       '(key VARCHAR(50) NOT NULL, ' +
                       'value VARCHAR(50));')
        
        connection.commit()

    def __init__(self):
        '''
        constructor
        '''

        