import json

list1 = [{"Name":"Anitha","Rollno":101}, {"Name":"Iniya","Rollno":102}]
#print(json.dumps(list1))
mylist =json.dumps(list1)

with open('test.json', 'w+', encoding='UTF-8') as s:
    s.write(mylist)

#packet loss is less
#time loss is less
