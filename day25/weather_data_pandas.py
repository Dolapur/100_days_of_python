#!/usr/bin/env python3
#How to read csv data files using pandas
import pandas

data = pandas.read_csv("weather_data.csv")

#How to get a row 
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

#How to create a data frame from scratch
data_dict = {
    "students": ["Amy", "James", "Angel"],
    "scores": [73, 54, 36]
}
data_dictionary = pandas.DataFrame(data_dict)
data_dictionary.to_csv("new_data.csv")
