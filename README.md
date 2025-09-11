SMS Bomb (Python + Twilio)

This project is a Python script that uses the Twilio API
 to send repeated SMS messages to a target number.

⚠️ Disclaimer: This script is for educational purposes only.
Misusing it to spam, harass, or flood someone’s phone is against the law and Twilio’s Acceptable Use Policy
.
Use responsibly, only with numbers you own or have explicit permission to message.

Features

Send SMS messages via Twilio.

Loop-based sending (with option to stop).

Basic error handling.

Requirements

Python 3.7+

Twilio account
 (free trial available).

A Twilio phone number.

Installation

Clone this repository:

git clone https://github.com/your-username/sms-bomb.git
cd sms-bomb


Install required package:

pip install twilio


Update the script (sms_bomb.py) with your Twilio credentials:

account_sid = "your_account_sid"
auth_token = "your_auth_token"
from_number = "+1234567890"  # Your Twilio number
to_number = "+1234567890"    # Target number

Usage

Run the script:

python sms_bomb.py


The script will begin sending SMS messages.

Type stop and press Enter to manually stop.

It also stops automatically after 1 minute.

Disclaimer

This code is a proof of concept for learning how to interact with Twilio’s SMS API.
Do not use it for malicious purposes. Misuse may result in:

Suspension of your Twilio account

Legal consequences

Permanent bans from telecom providers
