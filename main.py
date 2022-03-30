import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

twilio_SID_key: str
twilio_auth: str
weather_api_key: str

LAT = 38.424030
LON = -121.363490

api_URL = f"https://api.openweathermap.org/data/2.5/onecall"

parameters = {
    "lat": LAT,
    "lon": LON,
    "appid": weather_api_key,
    "exclude": "current,minutely,daily"
}
response = requests.get(url=api_URL, params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False

for item in data["hourly"][:12]:
    if item["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {"https": os.environ["http-proxy"]}

    client = Client(twilio_SID_key, twilio_auth, http_client=proxy_client)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring a jacket!",
        from_="+14707307976",
        to="+18317373286"
    )
    print(message.status)
    message = client.messages.create(
        body="It's going to rain today holmes. Remember to bring a jacket!",
        from_="+14707307976",
        to="+19165331837"
    )
    print(message.status)
    message = client.messages.create(
        body="It's going to rain today, wifey. Remember to bring a jacket!",
        from_="+14707307976",
        to="+14082235542"
    )
    print(message.status)

print(data["hourly"])
# rain alert -- Send SMS's when it's about to rain

