# Multi Processes
from multiprocessing import Process

def showSquare(num = 2):
    print(num ** 2)
    for i in range(100000): pass
procs = []

for i in range(5):
    procs.append(Process(target = showSquare()))
for proc in procs:
    proc.start()
print("Hello")

for proc in procs:
    proc.join()