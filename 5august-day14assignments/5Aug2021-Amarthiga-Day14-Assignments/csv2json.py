#csv to json convertion
import csv, json

myfile ='D:/Amarthiga/Python_Iprimed/Day13/student.csv'
jsonfile ='student.json'

student_list=[]

with open(myfile, 'r',encoding='UTF8') as i:
    #dataReader=csv.DictReader(i)
    dataReader=csv.reader(i)

    for data in dataReader:
        student_list.append(data)

# convert list to json

student_list_json=json.dumps(student_list)

with open(jsonfile, 'w', encoding='UTF8') as n:
    n.write(student_list_json)

#task:
