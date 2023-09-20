from concurrent.futures import thread
import threading

def calc1(input):
    currentNum=0
    while currentNum<input/3:
        currentNum+=1
    
def calc2(input):
    currentNum=0
    while currentNum<input/3:
        currentNum+=1
    
startNum=10000000
t1=threading.Thread(target=calc1(startNum/3), args=(10,))
t2=threading.Thread(target=calc2(startNum/3), args=(10,))
#t3=threading.Thread(target=calc1(startNum/3), args=(10,))

t1.start()
t2.start()
#t3.start()

t1.join()
t2.join()
#t3.join()