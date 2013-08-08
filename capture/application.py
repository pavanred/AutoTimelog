'''
Created on Aug 7, 2013

@author: pavan
'''

class Application(object):
    '''
    classdocs
    '''
    

    def __init__(self, app, cls, appid ):
        '''
        Constructor
        '''
        self.application = str(app).replace("\"","")
        self.classification = str(cls).replace("\"","")
        self.appid = appid
        