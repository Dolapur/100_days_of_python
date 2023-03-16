#!/usr/bin/env python3
import datetime as dt


now = dt.datetime.now() #current date and time
print(now)
print(now.year)
print(now.weekday())

# Create Date time of my own
date_of_birth = dt.datetime(year = 1988, month=6, day= 4)
print(date_of_birth)
