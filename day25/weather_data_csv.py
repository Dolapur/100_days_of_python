#!/usr/bin/env python3
#How to read a csv file using the csv module
import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    for row in data:
        print(row)
