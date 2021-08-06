#Find prime numbers between 2 and 500

import time,multiprocessing

l = 2
u = 500

#print("Prime numbers between", 2, "and", 500, "are:")
def prime(l,u):
    for n in range(l, u + 1):
        if n > 1:
            for i in range(2, n):
                if (n % i) == 0:
                    break
            else:
                print(n)

min =10
max = 500

def polindrome(min,max):
    for num in range(min, max + 1):
        temp = num
        reverse = 0
        
        while(temp > 0):
            Reminder = temp % 10
            reverse = (reverse * 10) + Reminder
            temp = temp //10
        if(num == reverse):
            print("%d " %num, end = '  ')


if (__name__)=="__main__":
    
    p1=multiprocessing.Process(target=prime, args=(l,u,))
    p2=multiprocessing.Process(target=polindrome, args=(min,max,))
    p1.start()
    p2.start()
    p1.join()
    print("Prime numbers are printing")
    p2.join()
    print("Polindrome numbers are printing")
    print(".......")
           # all prime numbers are greater than 1