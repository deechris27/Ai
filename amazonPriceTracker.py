# Track a specific products price and emails you when the price touches or goes does a target price

import requests
from bs4 import BeautifulSoup
import smtplib
import schedule
import time
from dotenv import load_dotenv
import os

PRODUCT_URL = 'https://amzn.in/d/f2TQGLg'
TARGET_PRICE = 2500

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

load_dotenv(override=True)
sender_email = os.getenv('EMAIL_SENDER')
sender_email_password = os.getenv('EMAIL_PASSWORD')
receiver_email = os.getenv('EMAIL_RECEIVER')

def get_price():
    response = requests.get(PRODUCT_URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'lxml')

    try:
        #Adjust based on amazon layout
        title = soup.find(id='productTitle').get_text(strip=True)
        price_str = soup.find('span', {'a-price-whole'})
        if not price_str:
            print("Price not found. Check selector.")
            return None
        price = int(price_str.get_text().replace(',', '').strip())
        return title, price
  
    except Exception as e:
        print("Error parsing price: ", e)
        return None
    

def send_email(subject, body):
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(sender_email, sender_email_password)
        message = f"Subject:{subject}\n\n{body}"
        connection.sendmail(send_email, receiver_email, message)
        print("Email sent!")


def check_price():
    result = get_price()
    if result:
        title, price = result
        print(f"[{time.strftime('%H:%M:%S')}] Price check: '{title}' at ₹{price}")
        if price <= TARGET_PRICE:
            send_email(
                "🎯 Price Drop Alert!",
                f"{title}\nNow ₹{price} (Target ₹{TARGET_PRICE})\n{PRODUCT_URL}"
            )
    else:
        print("Failed to retrieve product price.")

##Scheduler##
        
    schedule.every(1).hours.do(check_price)
    print("📦 Amazon Price Tracker started. Checking hourly...\n")

while True:
  schedule.run_pending()
  time.sleep(1)

