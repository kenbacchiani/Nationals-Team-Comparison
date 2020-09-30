#Author:Ken Bacchiani
#Program to graphically compare the win record of two Nationals teams in history
#Uses pybaseball's schedule and record API and maplotlib.pyplot with numpy

from pybaseball import schedule_and_record
import numpy as nump
import matplotlib.pyplot as plt


year1 = int(input("Enter the year for the first Nationals Team. "))
year2 = int(input("Enter the year for the second Nationals Team. "))

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
