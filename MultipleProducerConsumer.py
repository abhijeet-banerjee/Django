'''
Producer Consumner Example
'''
from threading import *
from time import *
from queue import *
# Queue is Thread Safe

class Producer:
    def __init__(self):
        self.q=Queue()
        
    def produce(self):
        for i in range(1,11):
            print('"Producer" Producing element', i, ' for Consumer')
            self.q.put(i)
            sleep(2)
            
            
class Consumer(Producer):
    def __init__(self,p):
        self.p=p
        self.q1=Queue()
    def consume(self):
        l=[]
        for i in range(1,11):
            print('"Consumer" Consuming element ',i, ' from Producer')
            l.append((self.p.q.get(i))*3)
            sleep(2)
        print('Final set for Consumer ',l,sep='\n')    
        for i in l:
            print('"Consumer" Producing element', i, ' for Consumer1')
            self.q1.put(i)
            sleep(2)

class Consumer1(Consumer):
    def __init__(self,p1):
        self.p1=p1
        self.q2=Queue()
        
    def consumeAgain(self):
        l=[]
        for i in range(1,11):
            print('"Consumer1" Consuming element ',i, ' from Consumer')
            l.append((self.p1.q1.get(i))*10)
            sleep(2)
        print('The final set for Consumer1 ',l,sep='\n')
        for i in l:
            print('"Consumer1" Producing element', i, ' for Consumer2')
            self.q2.put(i)
            sleep(2)
            
            
class Consumer2(Consumer1):
    def __init__(self,p2):
        self.p2=p2
        
    def consumeOnceAgain(self):
        l=[]
        for i in range(1,11):
            print('"Consumer2" Consuming element ',i, ' from Consumer1')
            l.append((self.p2.q2.get(i))+2)
            sleep(2)
        print('The final set for Consumer2 ',l,sep='\n')        
        
        
p=Producer()
c=Consumer(p)
c1=Consumer1(c)
c2=Consumer2(c1)
t = Thread(target=p.produce)
t1= Thread(target=c.consume)
t2= Thread(target=c1.consumeAgain)
t3= Thread(target=c2.consumeOnceAgain)
t.start()
t1.start()
t2.start()
t3.start()
t.join()
t1.join()
t2.join()  
t3.join()             


