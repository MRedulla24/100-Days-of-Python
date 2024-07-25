# ISS Overhead Alert
# By Marco Redulla
# Day 32 (25/07/2024)

import os
from dotenv import load_dotenv
import requests
from datetime import datetime
import smtplib

load_dotenv()

MY_LAT = float(os.getenv('MY_LAT'))
MY_LONG = float(os.getenv('MY_LONG'))
MY_EMAIL = os.getenv('EMAIL_ACCOUNT')
MY_PASS = os.getenv('EMAIL_PASSWORD')
TARGET_EMAIL = os.getenv('RECEIVER_EMAIL')

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

if time_now.hour > sunset:
    if (abs(iss_latitude - MY_LAT) < 5 or abs(iss_longitude - MY_LONG) < 5):
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASS)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=TARGET_EMAIL,
                                msg="Subject: Look Up!\n\nThe ISS is currently above you.")
    else:
        print("The ISS is not yet above you.")

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
