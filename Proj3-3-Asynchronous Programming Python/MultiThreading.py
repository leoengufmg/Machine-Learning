# Multi Threading
from threading import Thread

def square(n):
    print("square is", n**2)
def cube(n):
    print("cube is", n**3)
t1 = Thread(target = square, args = (4,))
t2 = Thread(target = cube, args = (3,))

t1.start()
t2.start()
print("Hello")

t1.join()
t2.join()

from queue import Queue
def producer(q):
    for i in range(5):
        q.put(i)
        print("Publisher",i)
def consumer(q):
    while True:
        data = q.get()
        print("consumed",data)
        
q = Queue()

producer_thread = Thread(target = producer, args = (q,))
consumer_thread = Thread(target = consumer, args = (q,))

consumer_thread.start()
producer_thread.start()