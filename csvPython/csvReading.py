# import pandas as pd
import csv
from datetime import datetime

path = "C:\Lenovo\mision TIC2022\Platzi_Py\csvPython\GoogleData.csv"
file = open(path, newline='')
reader = csv.reader(file)

header = next(reader)
data = []
for row in reader:
    date = datetime.strptime(row[0], '%m/%d/%Y')
    open_price = float(row[1])
    high = float(row[2])
    low = float(row[3])
    close = float(row[4])
    volume = int(row[5])
    adj_close = float(row[6])
    data.append([date, open_price, high, low, close, volume, adj_close])
    print(data[0])

# data = [row for row in reader]
# print(header)
# print(data[0])
# file = open(path)
# for line in file:
#     print(line)

# lines = [line for line in open(path)]
# dataset = [line.strip().split(',') for line in open(path)]
#
# print(dataset[0])
# print(dataset[1])
# print(dir(csv))
# print(lines[1])


# file = pd.read_csv()
# print(file)
# lines = [line for line in open(file)]

# lines[0]

