import csv

path = 'C:\Lenovo\mision TIC2022\Platzi_Py\csvPython\SURA1.csv'
lines = [line for line in open(path)]
print(lines[1])
# print(lines)

dataset = [line.strip().split('""') for line in open(path)]
dataset = [line.strip().split(":") for line in open(path)]
dataset = [line.strip().split('""') for line in open(path)]
print(dataset[1])

returns_path = 'C:\Lenovo\mision TIC2022\Platzi_Py\csvPython\PreubaSura.csv'
file = open(returns_path, 'w')
writer = csv.writer(file)
writer.writerow(dataset)
# lines[1].strip().split(':')


# file = open(path, newline='')
# reader = csv.reader(file)
#
# header = next(reader)
# data = [row for row in reader]
# data[1].strip().split('"')
#
# print(header)
# print(data[1])

# file = open(path, newline='')
# reader = csv.reader(file)
# header = next(reader)
# print(file)