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

    def __init__(self):
        '''
        Constructor
        '''
        self.connection = sqlite.connect('../data/timelog.sqlite')
        self.cursor = self.connection.cursor()
        