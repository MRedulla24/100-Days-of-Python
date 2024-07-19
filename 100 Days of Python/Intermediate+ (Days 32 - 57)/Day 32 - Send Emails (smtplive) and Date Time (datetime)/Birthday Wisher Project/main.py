##################### Extra Hard Starting Project ######################
import os
from dotenv import load_dotenv
import pandas as pd
import datetime as dt
import random
import smtplib

load_dotenv()

YOUR_NAME = "Marco"
letters = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']

email = os.getenv('EMAIL_ACCOUNT')
password = os.getenv('EMAIL_PASSWORD')
csv_filepath = os.getenv('CSV_FILEPATH')
letter_filepath = os.getenv('LETTER_FILEPATH')

birthdays = pd.read_csv(csv_filepath)

# Add SMTP for your email address here
if email.endswith('@gmail.com'):
    smtp_line = 'smtp.gmail.com'
elif email.endswith('@yahoo.com'):
    smtp_line = 'smtp.mail.yahoo.com'
elif email.endswith('@outlook.com'):
    smtp_line = 'outlook.office365.com'
# DO NOT CHANGE
else:
    smtp_line = None


birthday_count = 0
birthday_list = []
for index,row in birthdays.iterrows():
    now = dt.datetime.now()
    if now.month == row.get('month') and now.day == row.get('day'):
        birthday_count += 1
        birthday_list.append(row.get('name'))
        
        try:
            with open(f"{letter_filepath}\\{random.choice(letters)}", "r") as file:
                letter = file.read()
                letter = letter.replace('[NAME]', row.get('name'))
                letter =letter.replace('[YOUR NAME]', YOUR_NAME)
        except FileNotFoundError as err_message:
            print(f"Error. File {err_message} not found.")
        else:
            try:
                with smtplib.SMTP(smtp_line) as connection:
                    connection.starttls()
                    connection.login(user=email, password=password)
                    connection.sendmail(from_addr=email,
                                        to_addrs=row.get('email'),
                                        msg=f"Subject: Happy Birthday!\n\n{letter}")
            except smtplib.SMTPServerDisconnected:
                print("Error: SMTP line does not match any in records. Please add your SMTP.")
if birthday_count == 0:
    print("No one has a birthday today.")
else:
    print(f"You have automatically sent {birthday_count} birthday messages.")
    print("The following people have birthdays today:")
    for name in birthday_list:
        print(name)
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




