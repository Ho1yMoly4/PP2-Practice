#Datetime Module

import datetime

x = datetime.datetime.now()
print(x)

__________________________________

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

__________________________________

#Creating Date Objects

import datetime

x = datetime.datetime(2020, 5, 17)

print(x)

__________________________________

#Date Formatting

import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))

__________________________________

#Calculating Time Differences

from datetime import timedelta

d1 = datetime(2026, 1, 1)
d2 = datetime(2026, 1, 10)

diff = d2 - d1
print(diff.days)          # 9
print(diff.total_seconds())

__________________________________

#Working with Timezones

from datetime import timezone, timedelta

tz = timezone(timedelta(hours=3))
dt = datetime(2026, 1, 1, tzinfo=tz)
print(dt)
