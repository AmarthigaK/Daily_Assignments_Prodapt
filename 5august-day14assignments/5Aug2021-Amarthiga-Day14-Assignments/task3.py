# import json 

# data = 'petrol.json'

# with open(data, 'r', encoding= 'UTF8') as n:
#     data_read = json.dumps(n)
#     print(data_read)

# import csv, json

# petrolfile ='petrol.csv'
# jsonpetrol = 'petrol.json'


# petrol_list = []

# with open(petrolfile, 'r', encoding='UTF8') as m:
#     P_Reader =csv.DictReader(m)

#     for data in P_Reader:
#         petrol_list.append(data)

# petrol_json =json.dumps(petrol_list)

# with open(jsonpetrol, 'w', encoding='UTF8') as f:
#     f.write(petrol_json)
    
# New_list = x for x in petrol_json if x ['rate']<="70" 
# print(New_list)
#complete =[]


# for sub in jsonpetrol:
#     if sub ['rate'] <'70':
#         print(sub)
#         #petrol_list.append(sub)
# print(petrol_list)

import json

data = open("petrol.json")
loadpetrol = json.load(data)

for n in loadpetrol:
    if n["rate"] < "70":
        print(n)
n.close()