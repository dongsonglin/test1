import csv
from matplotlib import pyplot as plt
from datetime import datetime


filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    highs = []
    dates = []
    lows = []
    for row in reader:
        high = int(row[1])
        highs.append(high)
        current_date = datetime.strptime(row[0],"%Y-%m-%d")
        dates.append(current_date)
        low = int(row[3])
        lows.append(low)
    print(highs)
    print(dates)
#fig = plt.figure(dpi= 255,figsize=(10,3))
plt.plot(dates,highs,c='red')
plt.plot(dates,lows,c = 'blue')
plt.fill_between(dates,highs,lows,facecolor = 'blue',alpha = 0.4)
plt.title('Date_and_temperature')
plt.xlabel('date')
plt.ylabel('temperature')
plt.show()