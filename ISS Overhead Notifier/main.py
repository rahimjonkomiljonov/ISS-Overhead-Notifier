import requests
from datetime import datetime
import smtplib

import time


MY_LAT = 37.566536 # Your latitude
MY_LONG = 126.977966 # Your longitude
EMAIL = "smth.n.m.1@gmail.com"
PASSWORD = "ricfgyckeoaatbcw"
ISS_API_URL = "https://api.open-notify.org/iss-now.json"
SUNRISE_SUNSET_API_URL = "https://api.sunrise-sunset.org/json"
SMTP_SERVER = "smtp.gmail.com"

def is_overhead():
    try:
        response = requests.get(url=ISS_API_URL, timeout=5)
        response.raise_for_status()
        data = response.json()

        iss_latitude = float(data["iss_position"]["latitude"])
        iss_longitude = float(data["iss_position"]["longitude"])

        if (
                MY_LAT - 5 <= iss_latitude <= MY_LAT + 5
                and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
        ):
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error fetching ISS data: {e}")
        return False

def is_night():
    try:
        parameters = {
            "lat": MY_LAT,
            "lng": MY_LONG,
            "formatted": 0,
        }

        response = requests.get(url=SUNRISE_SUNSET_API_URL, params=parameters, timeout=5)
        response.raise_for_status()
        data = response.json()
        # Extract sunrise and sunset times
        sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

        # Get current hour in UTC
        now = datetime.utcnow().hour

        # Check if it's nighttime
        if now >= sunset or now <= sunrise:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error fetching sunrise/sunset data: {e}")
        return False

def send_email():
    try:
        with smtplib.SMTP(SMTP_SERVER) as connection:
            connection.starttls()  # Secure the connection
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=EMAIL,
                msg="Subject: Look Up! 👆\n\nThe ISS is overhead!",
            )
        print("Email notification sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

# Main loop
while True:
    if is_overhead() and is_night():
        send_email()
    time.sleep(60)  # Check every 60 seconds



