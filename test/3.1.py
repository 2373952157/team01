if 3:
    print(5)

a = [1,2,3]
if a:
    print(a)

a = []
if a:
    print(a)
else:
    print('empty')

i=s=0
while i <= 10:
    s += i
    i += 1
print(s)

i=s=0
while True:
    s += i
    i += 1
    if i > 10:
        break
print(s)

s = 0
for i in range(0,11,1):
    s += i
print(s)

print(1<2<3)

3 and 5   # and 自左向右扫描，都为真，则最后； or 返回第一个
3 or 5
0 and 5
0 or 5
not 3
not 0

def Join(chList,sep=None):  # sep必须是字符串
    return (sep or ',').join(chList)
chTest = ['1','2','3','4','5']
Join(chTest)
Join(chTest,':')
Join(chTest,' ')

def Join(chList,sep=',,'):  # sep必须是字符串
    return sep.join(chList)

x = input('Input two numbers:')
a,b = map(int,x.split())
if a>b:
    a,b = b,a
print(a,b)

if True:print(3);print(5)

a = 5
print(6) if a >3 else print(5)
print(6 if a>3 else 5)
b= 6 if a >13 else 9
b

import  math
import random
x = math.sqrt(9) if 5>3 else random.randint(1,100)
x

x=3
(1 if x>2 else 0) if x>5 else ('a' if x<5 else 'b')

def func(score):
    if score > 100:
        return 'wrong score.must <= 100.'
    elif score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    elif score >= 0:
        return 'E'
    else:
        return 'wrong score.must > 0'
func(120)
func(99)
func(3)
func(-10)