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
        self.q1=Queue()
    def produce(self):
        for i in range(1,11):
            print('"Producer" Producing element', i)
            self.q.put(i)
            self.q1.put(i)
            sleep(2)
            
            
class Consumer(Producer):
    def __init__(self,p):
        self.p=p
        
    def consume(self):
        l=[]
        for i in range(1,11):
            print('"Consumer" Consuming element ',i, ' from Producer')
            l.append((self.p.q.get(i))*2)
            sleep(2)
        print('Final set for Consumer ',l,sep='\n')    

class Consumer1(Producer):
    def __init__(self,p1):
        self.p1=p1

    def consumeAgain(self):
        l=[]
        for i in range(1,11):
            print('"Consumer1" Consuming element ',i, ' from Producer')
            l.append((self.p1.q1.get(i))*3)
            sleep(2)
        print('The final set for Consumer1 ',l,sep='\n')
            
        
        
p=Producer()
c=Consumer(p)
c1=Consumer1(p)
t = Thread(target=p.produce)
t1= Thread(target=c.consume)
t2= Thread(target=c1.consumeAgain)
t.start()
t1.start()
t2.start()
t.join()
t1.join()
t2.join()  
            


