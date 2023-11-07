#not threading used
# import time

# def sqr(num):
#     for i in num:
#         time.sleep(1)
#         print(i*i)
# def cube(num):
#     for j in num:
#         time.sleep(1)
#         print(j*j*j)
# a=[1,2,3,4,5]
# t1=time.time()
# sqr(a)
# cube(a)
# print(time.time()-t1)

#threading used
# import time
# import threading
# def sqr(num):
#     for i in num:
#         time.sleep(1)
#         print("square is",i*i)
# def cube(num):
#     for j in num:
#         time.sleep(1)
#         print("cube is",j*j*j)
# a=[1,2,3,4,5]
# t1=time.time()
# thread1=threading.Thread(target=sqr,args=(a,))
# thread2=threading.Thread(target=cube,args=(a,))
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print(time.time()-t1)

from threading import*
import time
l=Lock()
def first(name,age):
    for i in range(3):
        l.acquire()
        print("hello",name)
        time.sleep(1)
        print("age is",age)
        l.release()
t1=Thread(target=first,args=("anu",43))
t2=Thread(target=first,args=("ammu",34))
t1.start()
t2.start()
