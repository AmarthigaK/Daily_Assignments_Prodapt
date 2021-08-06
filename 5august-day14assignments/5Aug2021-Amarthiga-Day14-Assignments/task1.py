import csv, json

petrolfile ='petrol.csv'
jsonpetrol = 'petrol.json'


petrol_list = []

with open(petrolfile, 'r', encoding='UTF8') as m:
    P_Reader =csv.DictReader(m)

    for data in P_Reader:
        petrol_list.append(data)

petrol_json =json.dumps(petrol_list)

with open(jsonpetrol, 'w', encoding='UTF8') as f:
    f.write(petrol_json)
    

