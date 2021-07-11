import csv

with open("table_in.csv", encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        print(row[1].replace(" ", ""), row[0], sep=",")
