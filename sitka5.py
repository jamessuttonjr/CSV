import matplotlib.pyplot as plt
import csv
from datetime import datetime


open_file = open("death_valley_2018_simple.csv", "r")
open_file2 = open("sitka_weather_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")
csv_file2 = csv.reader(open_file2, delimiter=",")

header_row = next(csv_file)
header_row2 = next(csv_file2)

print(type(header_row))
print(type(header_row2))
for index, column_header in enumerate(header_row):
    print(index, column_header)
    if column_header == "TMAX":
        TMAX = index
    if column_header == "TMIN":
        TMIN = index
    if column_header == "DATE":
        DATE = index
    if column_header == "NAME":
        NAME = index
print()
print()

for index, column_header in enumerate(header_row2):
    print(index, column_header)
    if column_header == "TMAX":
        TMAX2 = index
    if column_header == "TMIN":
        TMIN2 = index
    if column_header == "DATE":
        DATE2 = index
    if column_header == "NAME":
        NAME2 = index

# testing to convert date from string

highs = []
dates = []
lows = []

highs2= []
dates2 = []
lows2 = []

for row in csv_file:
    try:
        the_date = datetime.strptime(row[DATE], '%Y-%m-%d')
        high = int(row[TMAX])
        low = int(row[TMIN])
        Station = row[NAME]
    except ValueError:
        print(f"Missing data for {the_date}")
    else:
        highs.append(int(row[TMAX]))
        dates.append(the_date)
        lows.append(int(row[TMIN]))

for row in csv_file2:
    try:
        the_date2 = datetime.strptime(row[DATE2], '%Y-%m-%d')
        high = int(row[TMAX2])
        low = int(row[TMIN2])
        Station2 = row[NAME2]
    except ValueError:
        print(f"Missing data for {the_date2}")
    else:
        highs2.append(int(row[TMAX2]))
        dates2.append(the_date2)
        lows2.append(int(row[TMIN2]))

# plt.subplot(nrows,ncolumns,index)
fig = plt.figure()

plt.subplot(2, 1, 1)
plt.plot(dates2, highs2, c="red", alpha=0.5)
plt.plot(dates2, lows2, c="blue", alpha=0.5)
plt.fill_between(dates2, highs2, lows2, facecolor='blue', alpha=0.1)
plt.title(Station2)
fig.autofmt_xdate()

plt.subplot(2, 1, 2)
plt.plot(dates, highs, c="red", alpha=0.5)
plt.plot(dates, lows, c="blue", alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
plt.title(Station)
fig.autofmt_xdate()

plt.suptitle(f"Temperature comparison between {Station2} and {Station}")

plt.show()