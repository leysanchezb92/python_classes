import csv

csvPath= "/Users/lsanchez/Documents/python/python_classes/MODULO 4/ejercicio_csv/students.csv"

def write_csv(data):
    with open(data,'r', encoding ='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            print(row)

write_csv(csvPath)


