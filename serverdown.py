import os
from twilio.rest import Client
from urllib.request import urlopen
from urllib.error import *
 
 
username = "#########"
password = "#########"
account_sid = os.environ['TWILIO_ACCOUNT_SID'] = "#"
auth_token = os.environ['TWILIO_AUTH_TOKEN'] = "#"
client = Client(account_sid, auth_token)

# try block to read URL
try:
    html = urlopen("http://*.*.*.*") # public IP address
    
except HTTPError as e:
    print("HTTP error", e)
     
except URLError as e:
    numbers_to_message = ['########', '#########', '##########'] # phone numbers to send sms to
    for number in numbers_to_message:
        client.messages.create(
            body='The server is down. If not restored in 10min, this message will appear again. Smartec Salvi-Rwanda.',
            from_='+13862726689',
            to=number
        )