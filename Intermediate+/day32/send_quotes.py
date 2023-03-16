#!/usr/bin/env python3
from random import choice
import datetime as dt
import smtplib


email = 'email'
recipient_email = 'email'
password = 'password'

now = dt.datetime.now()

day_of_week = now.weekday()
if day_of_week == 2:
    with open("quotes.txt") as quote_file:
        total_quotes = quote_file.readlines()
    quotes = choice("total_quotes")
    
    message = "Subject: Wednesday Quote of the Day\n\n" + "\n\n".join(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = email, password = password)
        connection.sendmail(from_addr=email, to_addrs=recipient_email, msg=message)
