#!/usr/bin/python3
import smtplib
import datetime as dt
import pandas
import random 

MY_EMAIL = "example@gmail.com"
PASSWORD = "password"

date = dt.datetime.now()
date_tuple = (date.month, date.day)

birthday_data = pandas.read_csv("birthdays.csv")
birthday_dict= {(data_row.month, data_row.day): data_row for (index, data_row) in birthday_data.iterrows()}
if date_tuple in birthday_dict:
    birthday_person = birthday_dict[date_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
    
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=email, to_addrs=email, msg = f"Subject:Happy Birthday\n\n{contents}")
