import urllib2
import json
import winsound
import time

appid = '<ENTER_YOUR_APP_ID_HERE>'

city = raw_input("City: ")
temperature = float(raw_input("Maximum Temperature: "))

while True:

    try:

        url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=imperial&appid=' + appid

        while True:

            response = urllib2.urlopen(url)
            html = response.read()

            data = json.loads(html)

            if float(data['main']['temp']) > temperature:

                while True:

                    for i in xrange(5):

                        winsound.Beep(800, 990)

                    time.sleep(5)

            time.sleep(600)  # Do not remove this otherwise your IP will be blocked!

    except:

        continue
