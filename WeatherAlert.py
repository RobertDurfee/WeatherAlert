import urllib2
import json
import time
from twilio.rest import Client

client = Client('<TWILIO_ACCOUNT_ID>', '<TWILIO_AUTHENTICATION_TOKEN>')

appid = '<OPEN_WEATHER_MAP_APPLICATION_ID>'

city = raw_input("City: ")
temperature = float(raw_input("Maximum Temperature: "))

url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=imperial&appid=' + appid

while True:

    response = urllib2.urlopen(url)
    html = response.read()

    data = json.loads(html)

    if float(data['main']['temp']) > temperature:

        client.messages.create(to='<PHONE_NUMBER>', from_='<TWILIO_PHONE_NUMBER>', body='The temperature in ' + city +
                                                                             ' is now higher than ' + str(temperature) +
                                                                             ' degrees. (' + str(data['main']['temp']) +
                                                                             ' degrees)')

        exit(0)

    time.sleep(600)  # Do not remove this otherwise your IP will be blocked!
