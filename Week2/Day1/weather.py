import random
def weather_simulator():
    conditions=["Sunny","Cloudy","Rainy","Windy"]
    temp=random.randint(20,40)
    weather=random.choice(conditions)
    print(f"Weather: {weather}, Temp: {temp}°C")
weather_simulator()
