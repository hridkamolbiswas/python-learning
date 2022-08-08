import time 
import threading
from datetime import datetime 

x = [1,2,3,4,5]

def get_square(item):
    time.sleep(1)
    return item**2

t1 = datetime.now()

l = []
for item in x:
    item_square = get_square(item=item)
print(l)

t2 = datetime.now()

r = (t2-t1).total_seconds()
print(f"required_time = {r} seconds")

