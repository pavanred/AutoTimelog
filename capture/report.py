'''
Created on Aug 8, 2013

@author: pavan
'''
import datalib

def main(reporttype):
    reportlist = get_session_list()
    reportlist_life = get_lifetime_list()
    total = calculate_total(reportlist)
    reportlist = calculate_percentage(reportlist,total)
    total = calculate_total(reportlist_life)
    reportlist_life = calculate_percentage(reportlist_life,total)
    
    print 'AutoTimelog v0.1'   
    print '' 
     
    if reporttype == 'lifetime':
        print 'Life time'
        display_report(reportlist_life)
    elif(reporttype ==  'session'):
        print 'Current session'
        display_report(reportlist)
    else:
        print 'Current session'
        display_report(reportlist)
        print ''
        print 'Life time'
        display_report(reportlist_life)

def display_report(reportlist):
    
    sortedlist = sorted(reportlist,key=lambda x:x.percentage, reverse=True)    
    for item in sortedlist:        
        print item.name + ' - ' + str("%.2f" %item.percentage) + '% ' + '(' + str(item.days) + ' days, ' + str(item.hours) + ' hours, ' + str(item.minutes) + ' mins)'

def calculate_total(reportlist):
    totaldays = 0.0
    totalhours = 0.0
    totalminutes = 0.0
    
    for item in reportlist:
        totaldays = totaldays + item.days
        totalhours = totalhours + item.hours
        totalminutes = totalminutes + item.minutes
    
    if totalminutes > 0:
        totalhours = totalhours + (totalminutes/60.0)
            
    if totalhours > 0:
        totaldays = totaldays + (totalhours/24.0)        
    
    return totaldays

def calculate_percentage(reportlist,total):
    
    for item in reportlist:
        hours = 0.0
        days = 0.0                    
        if item.minutes > 0:
            hours = item.hours + (item.minutes/60.0)
        if hours > 0:
            days = item.days + (hours/24.0)
        
        item.percentage = 0
        
        if total > 0:
            item.percentage = (days/total)*100
            
    return reportlist       
    
def get_session_list():
    db = datalib.Database()
    reportlist = db.get_session_data()
    return reportlist
    
def get_lifetime_list():
    db = datalib.Database()
    reportlist = db.get_lifetime_data()
    return reportlist

if __name__ == '__main__':
    main('all')
        
class Report(object):
        
    def __init__(self, name, days, hours, minutes):
        self.name = name
        self.days = days
        self.hours = hours
        self.minutes = minutes
        self.percentage = 0.0 