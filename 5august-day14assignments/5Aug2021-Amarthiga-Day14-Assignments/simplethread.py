#thread -single process/ individual process

import threading,time

def printNumbers():
    for n in range(1,19):
        time.sleep(3)
        print(n)

def printHello():
    for i in range(1,4):
        time.sleep(3)
        print("Hello")


#creating a thread
# t1 = threading.Thread(target =printNumbers)   #target is a keyword 
# t2= threading.Thread(target =printHello)
# t1.start()
# t2.start()
# t1.join()        #it will let the programme 1st and then thread will execute
# t2.join()
# print(".....")    #asynchronous -background


#THREAD USED TO RUN THE PROGRAMMES FASTLY
# WE CAN CREATE 'N' NO OF THREAD, it will perfome concurrently

#list

def findsquare(list1):
    for i in list1:
        time.sleep(3)
        print(i*i)
def findcube(list1):
    for i in list1:
        time.sleep(3)
        print(i*i*i)
mylist =[3,5,6,5,8]
t1=threading.Thread(target=findsquare, args=(mylist,))
t2=threading.Thread(target=findcube, args=(mylist,))
t1.start()
t2.start()
t1.join()
t2.join()