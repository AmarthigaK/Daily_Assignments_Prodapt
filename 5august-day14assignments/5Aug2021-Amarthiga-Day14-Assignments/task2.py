import csv, json

dieselfile ='diesel.csv'
jsondiesel = 'diesel.json'


diesel_list = []

with open(dieselfile, 'r', encoding='UTF8') as n:
    D_Reader =csv.DictReader(n)

    for data in D_Reader:
        diesel_list.append(data)

diesel_json =json.dumps(diesel_list)

with open(jsondiesel, 'w', encoding='UTF8') as f:
    f.write(diesel_json)