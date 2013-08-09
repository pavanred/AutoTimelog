## AutoTimelog v0.1

AutoTimelog is a personal time tracking tool. AutoTimelog captures the current application being used by capturing active window at every minute and helps track personal time tracking. It uses a sqlite database to store the captured data. It provides the user with a reporting module for the time tracked for each application used and the respective time spent, for the current session and complete lifetime. 

###Installation

1. copy the folder AutoTimelog/ to ~/AutoTimelog

2. Execute the setup to create and setup the sqlite database
	
	python ~/AutoTimelog/setup.py

3. Execute track.py to begin your capturing your activity

	python ~/AutoTimelog/capture/track.py

###Usage

Once time tracking is strated, the current application being used is captured by tracking the active window every minute and it is stored. The reporting module can be used to check your activty and time usage. The sqlite database used to store data is present in ~/AutoTimelog/data/timelog.sqlite

###Report

Execute the reporting module to check your activity and time usage of the current session and lifetime.

	python ~/AutoTimelog/capture/report.py

A sample of the report will be - 

	AutoTimelog v0.1

	Current session	
	Firefox - 49.25% (0 days, 0 hours, 33 mins)
	Guake - 23.88% (0 days, 0 hours, 16 mins)
	Eclipse - 17.91% (0 days, 0 hours, 12 mins)
	Vlc - 5.97% (0 days, 0 hours, 4 mins)
	Liferea - 1.49% (0 days, 0 hours, 1 mins)	

	Life time	
	Firefox - 44.16% (0 days, 0 hours, 34 mins)
	Guake - 32.47% (0 days, 0 hours, 25 mins)
	Eclipse - 15.58% (0 days, 0 hours, 12 mins)	
	Vlc - 5.19% (0 days, 0 hours, 4 mins)
	Liferea - 1.30% (0 days, 0 hours, 1 mins)

###Change log

v0.1
* capture activity data for current session and lifetime
* report session and lifetime report of applications used and the time period they were used for

###Todo

* create a daemon/service to start AutoTimelog on reboot without requiring a manual start on reboot
* Add user defined categories e.g. Eclipse, MySql workbench classified as "work" and allow reporting based on categories

