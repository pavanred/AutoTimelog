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
    
    def clear_session_data(self):
        self.cursor.execute('delete from activity_session')
        self.connection.commit()        
    
    def record_activity(self,appid):
        self.cursor.execute("select hours, minutes from activity_session where appid = ?",(appid,))
        row = self.cursor.fetchone()
        if row:
            hours = int(row[0])
            minutes = int(row[1])
            if minutes == 59:
                hours = hours + 1
                minutes = 0
            self.cursor.execute("update activity_session set minutes = ?,hours =? where appid = ?",(minutes,hours,appid,))        
        else:
            minutes = 1
            self.cursor.execute('insert into activity_session values (?,?,?)',(appid,0,minutes,))
        self.connection.commit()        
        
        self.cursor.execute("select days, hours, minutes from activity_lifetime where appid = ?",(appid,))
        row = self.cursor.fetchone()
        if row:
            days = int(row[0])
            hours = int(row[1])
            minutes = int(row[2])
            if hours == 23:
                days = days + 1
                hours = 0
            if minutes == 59:
                hours = hours + 1
                minutes = 0            
            self.cursor.execute("update activity_lifetime set minutes = ?,hours = ?, days = ? where appid = ?",(minutes,hours,days,appid,))        
        else:
            minutes = 1
            self.cursor.execute('insert into activity_lifetime values (?,?,?,?)',(appid,0,0,minutes,))
        self.connection.commit()        

    def __init__(self):
        '''
        Constructor
        '''
        self.connection = sqlite.connect('../data/timelog.sqlite')
        self.cursor = self.connection.cursor()
        