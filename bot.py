import os
import random
import requests
from datetime import datetime
import time

# Load environment variables (Render or .env)
BOT_TOKEN = os.getenv("8104700736:AAHPuLcYBd4H-LkpJhxu0T3IZ--YSBs7iY0")

def generate_prediction(period_number):
    bet = random.choice(["SMALL", "BIG"])
    message = f"""
Hi I'm Emon:
{period_number:03}

SMM PANEL:
HGZY-Win VIP Hack Prediction! 🤑

Game :: Wingo 1 Min
Period Number :: {period_number:03}
Bet :: {bet}

Maintain 7-Level Funds to Minimize Losses! 💰
"""
    return message

def send_prediction_to_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    response = requests.post(url, data=data)
    return response

def main():
    period_number = 1  # Start from 001
    while True:
        msg = generate_prediction(period_number)
        print(f"Sending prediction for period {period_number:03}")
        send_prediction_to_telegram(msg)
        period_number += 1
        time.sleep(60)  # Wait 1 minute before sending next prediction

if __name__ == "__main__":
    main()
