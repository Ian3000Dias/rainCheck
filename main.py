import requests
from twilio.rest import Client

PARAMETERS = {
    "lat": 19.075983,
    "lon": 72.877655,
    "appid": "69f04e4613056b159c2761a9d9e664d2",
    "exclude": "current,minutely,daily"
}

account_sid = "ACbce80d193932c60e2569b4fb1ea480f9"
auth_token = "f3211adb1b23e3925628f409cc5fc43a"

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=PARAMETERS)
response.raise_for_status()
data = response.json()
# pyperclip.copy(str(data))
rain_data = [data["hourly"][x]["weather"][0]["id"] for x in range(0, 11)]
umbrella = False

verified_numbers = ["+918779829702", "+918169635219"]
for i in rain_data:
    if i < 700:
        umbrella = True
if umbrella:
    client = Client(account_sid, auth_token)
    for number in verified_numbers:
        message = client.messages \
            .create(
            body="Its going to rain today, Carry an Umbrella.☂",
            from_='+19204813084',
            to=number
        )
try:
    print(message.sid)
    print(message.status)
except:
    print("No message sent")
