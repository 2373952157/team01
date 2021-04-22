def main(n):
    for i in range(n):
        print((' * ' * i ).center(n*3))
    for i in range(n,0,-1):
        print((' * ' * i ).center(n*3))
main(6)

for n in range(100,1,-1):
    for i in range(2,n):
        if n%i == 0:
            break
    else:
        print(n)
        break

for n in range(100,1,-1):
    for i in range(2,n):
        if n%i == 0:
            break
    else:
        print(n,end=' ')

import time
digits = (1, 2, 3, 4)
start =time.time()
for i in range(1000):
    result = []
    for i in digits:
        for j in digits:
            for k in digits:
                result.append(i*100 + j*10 + k)
print(time.time()-start)


import time
import math

start = time.time()
for i in range(10000000):
    math.sin(i)
print('Time Used:', time.time()-start)

loc_sin = math.sin
start = time.time()
for i in range(10000000):
    loc_sin(i)
print('Time Used:',time.time()-start)






