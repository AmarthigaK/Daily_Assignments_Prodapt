import time,multiprocessing

def findsquare(list1):
    for i in list1:
        time.sleep(3)
        print(i*i)
def findcube(list1):
    for i in list1:
        time.sleep(3)
        print(i*i*i)

if (__name__)=="__main__":
    mylist =[3,5,6,5,8]
    p1=multiprocessing.Process(target=findsquare, args=(mylist,))
    p2=multiprocessing.Process(target=findcube, args=(mylist,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(".......")