#Author:Ken Bacchiani
#Program to graphically compare the win record of two Nationals teams in history
#Uses pybaseball's schedule and record API and maplotlib.pyplot with numpy

from pybaseball import schedule_and_record
import numpy as nump
import matplotlib.pyplot as plt
from datetime import datetime

today = datetime.today()
currentY = today.year
firstYear = 2005
valid = False
while(not valid):
    try:
        year1 = int(input("Enter the year for the first Nationals Team. "))
    except:
        print("Invalid Input. Try Again.")
        continue
    if((year1 < firstYear) or (year1 > currentY)):
        if(year1 < firstYear):
            print("Year entered was before Nationals first season(2005). Please enter a year 2005 or later.")
            continue
        else:
            print("Year entered was after this current year and therefore a season doesn't exist. Please enter a year %i or earlier." % currentY)
            continue
    if(year1 == 2020):
        print("Remember, 2020 was a COVID-19 shortened season and only 60 games were played versus the normal 162 for other years.")
    valid = True
valid = False
while(not valid):
    try:
        year2 = int(input("Enter the year for the second Nationals Team. "))
    except:
        print("Invalid Input. Try Again")
        continue
    if((year2 < firstYear) or (year2 > currentY)):
        if(year2 < firstYear):
            print("Year entered was before Nationals first season(2005). Please enter a year 2005 or later.")
            continue
        else:
            print("Year entered was after this current year and therefore a season doesn't exist. Please enter a year %i or earlier." % currentY)
            continue
    if(year2 == 2020):
        print("Remember, 2020 was a COVID-19 shortened season and only 60 games were played versus the normal 162 for other years.")
    valid = True

nats1 = schedule_and_record(year1, 'WSN')
nats2 = schedule_and_record(year2, 'WSN')

nats1['win-count'] = nump.where(nats1['W/L']=='W', 1, 0).cumsum()
nats2['win-count'] = nump.where(nats2['W/L']=='W', 1, 0).cumsum()

plt.plot(nats1['win-count'],label =  "%d Nationals" % year1)
plt.plot(nats2['win-count'],label = "%d Nationals" % year2)
plt.legend(loc=4)
plt.xlabel('Games Played')
plt.ylabel('Wins')
plt.title('%d Nationals vs. %d Nationals Win Record Throughout Season' % (year1, year2))
plt.show()
