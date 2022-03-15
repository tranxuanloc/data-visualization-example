import csv
import matplotlib.pyplot as plt
from datetime import datetime


# file_name = 'data/sitka_weather_07-2018_simple.csv'
file_name = 'data/sitka_weather_2018_simple.csv'
with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index, column in enumerate(header_row):
        print(index, column)

    dates, highs, lows = [], [], []
    for row in reader:
        lows.append(int(row[6]))
        highs.append(int(row[5]))
        dates.append(datetime.strptime(row[2], '%Y-%m-%d'))

    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    fig.autofmt_xdate()
    ax.plot(dates, highs, c='red', alpha=0.5)
    ax.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
    plt.title('Daily high and low temeratures - 2018', fontsize=24)
    plt.xlabel('', fontsize=16)
    plt.ylabel('Temperature (F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()
