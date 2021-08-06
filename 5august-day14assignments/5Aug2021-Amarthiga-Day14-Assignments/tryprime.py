import math
import threading,time
# l=2
# u=10

# def prime(l,u):
#     for i in range(l,u+1):
#         if i>1:
#             for n in range(2,int(math.sqrt(i))):
#                 if (i%n)==0:
#                     break
#             else:
#                     print(i)
# # l=2
# # u=500
            
# s1 = threading.Thread(target=prime, args=(l,u,))
# s1.start()
# s1.join()
# print(".......")

# def prime(a):
#     a=[i for i in range(2,500) if 0 not in [i%n for n in range(2,int(math.sqrt(i)))]]
#     print(a)

# s1 = threading.Thread(target=prime, args=())
# s1.start()
# s1.join()
# print(".......")
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

p1=threading.Thread(target=prime, args=(l,u,))
p2=threading.Thread(target=polindrome, args=(min,max,))
p1.start()
p2.start()
p1.join()
print("Prime numbers are printing")
p2.join()
print("Polindrome numbers are printing")
print(".......")