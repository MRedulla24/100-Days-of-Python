import os
from dotenv import load_dotenv
import smtplib
import datetime as dt
import random

load_dotenv()

# CONSTANTS
FILEPATH = r"100 Days of Python/Intermediate+ (Days 32 - 57)/Day 32 - Send Emails (smtplive) and Date Time (datetime)/Motivational Email Project/quotes.txt"
EMAIL = os.getenv('EMAIL_ACCOUNT')
PASSWORD = os.getenv('EMAIL_PASSWORD')

with open(FILEPATH, "r") as file:
    quotes = [quote.replace("\n","") for quote in file.readlines()]

now = dt.datetime.now()

if now.weekday() == 0:
    quote = random.choice(quotes).replace("-","\n-")
    content = f"Subject: Motivational Message\n\n{quote}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL, 
                            to_addrs='m.redulla2024@gmail.com',
                            msg=content)