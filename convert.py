import json
import csv
import pandas

pandas.read_json("output.json").to_excel("output.xlsx")

with open("output.json", encoding="utf-8") as json_file:
    jsondata = json.load(json_file)

data_file = open("output.csv", "w", newline="", encoding="utf-8")
csv_writer = csv.writer(data_file)

count = 0
for data in jsondata:
    if count == 0:
        header = data.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(data.values())

data_file.close()


print("Convertion Complete")
