import requests
import matplotlib.pyplot as plt

print("==== Weather App with 5-Day Forecast ====")

city = input("Enter city name: ")

api_key = "YOUR_API_KEY_HERE"

url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

temperatures = []
dates = []

print("\n----- 5 Day Forecast -----\n")

# API gives data every 3 hours, so pick every 8th (24 hours)
for i in range(0, 40, 8):
    
    temp = data["list"][i]["main"]["temp"]
    date = data["list"][i]["dt_txt"]
    weather = data["list"][i]["weather"][0]["description"]
    
    temperatures.append(temp)
    dates.append(date.split()[0])
    
    print("Date:", date.split()[0])
    print("Temperature:", temp, "°C")
    print("Condition:", weather)
    print("------------------------")

# Plot Graph
plt.figure()
plt.plot(dates, temperatures, marker='o')

plt.title(f"5-Day Weather Forecast - {city}")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()