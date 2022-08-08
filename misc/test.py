from datetime import datetime 
t1 = datetime.now()

res = 0
for item in range(1000000000):
    res+=item

print(res)
t2 = datetime.now()
print((t2-t1).total_seconds())
