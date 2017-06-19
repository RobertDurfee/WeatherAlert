# WeatherAlert
A simple python script for sending an SMS message when it reaches a certain temperature at a certain location.

### Disclaimer
This is not production-worthy code! View this simply as a proof-of-concept. Preconditions are implicit. No error checking exists.

### Initialization
You first must create an account with Twilio and Open Weather Map to gain free API keys.

Once you have created these accounts, fill in your `<TWILIO_ACCOUNT_ID>`, `<TWILIO_AUTHENTICATION_TOKEN>`, `<OPEN_WEATHER_MAP_APPLICATION_ID>`, and `<TWILIO_PHONE_NUMBER>`. Also, supply the phone number you wish to receive the notifications in the `<PHONE_NUMBER>` field.

### Usage
When the script is run, simply specify the city you wish to monitor and the maximum temperature at which you would like to be alerted. When this temperature is reached (the current temperature is greater than or equal to), an SMS message will be sent to your supplied phone number.
