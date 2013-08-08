'''
Created on Aug 7, 2013

@author: pavan
'''
from pysqlite2 import dbapi2 as sqlite
import application

class Database(object):
    '''
    database connection, datamanipulation
    '''    

    def get_appliction_list(self):
        apps = []
        self.cursor.execute('select id,name,class from application;')
        for row in self.cursor:
            app = application.Application(row[1],row[2],row[0])
            apps.append(app)                        
        return apps
    
    def add_new_application(self, app):
        self.cursor.execute('insert into application values (null,?,?)',(app.application,app.classification))
        self.connection.commit()
        
    def app_exists(self, app_name, apps):
        for app in apps:
            if str(app.application) == str(app_name):
                return app
        return ''

    def get_config_value(self, key):
        self.cursor.execute("select value from config where key = ?",(key,))
        row = self.cursor.fetchone()
        if row:
            value = row[0]
        else:
            value = 0        
        return str(value)
    
    def record_activity(self,app):
        self.cursor.execute("select duration from activity where appid = ?",(app.appid,))
        row = self.cursor.fetchone()
        if row:
            duration = int(row[0]) + 1    
            self.cursor.execute("update activity set duration = ? where appid = ?",(duration,app.appid,))        
        else:
            duration = 1
            self.cursor.execute('insert into activity values (?,?)',(app.appid,duration,))
        self.connection.commit()        

    def __init__(self):
        '''
        Constructor
        '''
        self.connection = sqlite.connect('../data/timelog.sqlite')
        self.cursor = self.connection.cursor()
        