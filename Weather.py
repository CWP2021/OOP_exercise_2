while True:

    temperature = float (input ('Insert temperature today (in C°):'))

    wind_speed = float (input ('Insert wind speed today(in km/h):'))

    wind_direction = (input ('Insert wind direction (N/S/E/W):'))

    class Weather:

        def __init__(self, temperature, wind_speed, wind_direction):

            self.temperature = temperature

            self.wind_speed = wind_speed

            self.wind_direction = wind_direction

        def weather_today(self):

            print(f'Temperature: {self.temperature} C° / Wind speed: {self.wind_speed} km/h / Wind direction: {self.wind_direction}')

    weather_object1 = Weather(temperature, wind_speed, wind_direction)

    weather_object1.weather_today()

    class VerbalWeather(Weather):

        def weather_today(self):

            if temperature > 20:

                self.temperature = 'warm'

            else:

                self.temperature = 'cold'

            if wind_speed > 30:

                self.wind_speed = 'windy'

            else:

                self.wind_speed = 'not windy'

            print(f'Temperature: {self.temperature}  / Wind speed: {self.wind_speed}  / Wind direction: {self.wind_direction}')

    weather_object2 = VerbalWeather(temperature, wind_speed, wind_direction)

    weather_object2.weather_today()

