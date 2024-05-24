x=input('Input city: ')

import requests
API_KEY = 'YOUR_API_KEY'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
city = x

# Make the GET request to the OpenWeatherMap API
response = requests.get(BASE_URL, params={'q': city, 'appid': API_KEY})

# Check if the request was successful (status code 200)




def temp_info(weather_data):
        # fetch required weather data
        kelvintemp=weather_data['main']['temp']
        kelvintempmax=weather_data['main']['temp_max']
        kelvintempmin=weather_data['main']['temp_min']
        
        #conversion to celsius
        celsiustemp=kelvintemp -273.15
        celsiustempmax=kelvintempmax - 273.15
        celsiustempmin=kelvintempmin - 273.15

        #conversion to fahrenheit
        fahrentemp=((kelvintemp - 273.15) * 9/5 + 32)
        fahrentempmax=((kelvintempmax - 273.15) * 9/5 + 32)
        fahrentempmin=((kelvintempmin - 273.15) * 9/5 + 32)

        cv = input(str('Reading in celsius or fahrenheit: '))
        if cv == 'celsius' or cv=='Celsius' or cv=='ce' or cv=='Cv' or cv=='C':
            print('The temperature in',x,'is',round(celsiustemp,2),'degrees celsius.')
            print('Max temperature may reach',round(celsiustempmax,2),'degrees celsius.')
            print('Min temperature may be',round(celsiustempmin,2),'degrees celsius.')

        elif cv == 'fahrenheit' or cv=='Fahrenheit' or cv=='fa' or cv=='Fa' or cv=='F' or cv=='fh' or cv=='FH' or cv=='Fh':
            print('The temperature in',x,'is',round(fahrentemp,2),'degrees fahrenheit.')
            print('Max temperature may reach',round(fahrentempmax,2),'degrees fahrenheit.')
            print('Min temperature may be',round(fahrentempmin,2),'degrees fahrenheit.')
def cast(weather_data):
    forecast=weather_data['weather'][0]['main']
    fcdetails=weather_data['weather'][0]['description']
    humidity=weather_data['main']['humidity']
    pressure=weather_data['main']['pressure']
    breeze=weather_data['wind']['speed']

    print('General skycast for',x+':',forecast)
    print('Detailed skycast for',x+':',fcdetails)
    print('Humidity:',str(humidity)+'%')
    print('Pressure:',pressure,'millibars')
    print('Windspeeds are around:',str(breeze)+'m/s')
def city_data(weather_data):
    latitude=weather_data['coord']['lat']
    longitude=weather_data['coord']['lat']
    tz=weather_data['timezone']
    country=weather_data['sys']['country']

    print('The city',x,'is in the country',country)
    print('Latitude:',latitude)
    print('Longitude:',longitude)
    print('Timezone:',tz)







if response.status_code == 200:
    # Parse the JSON response
    weather_data = response.json()

    
    reqdata = input('Enter 1 for temperature information\nEnter 2 for general skycast/weather\nEnter 3 for regional information\n')
    print('\n')
    
    if reqdata == '1':
        temp_info(weather_data)
    elif reqdata=='2':
        cast(weather_data)
    elif reqdata=='3':
        city_data(weather_data)


else:
    # Print an error message if the request was not successful
    print('Request failed with status code:', response.status_code)
