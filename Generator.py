import time

def Stream(num):
    
    for num in range(num):
        yield num
        time.sleep(0.1)
        
num = 20

for n in Stream(num):
    print(n)
