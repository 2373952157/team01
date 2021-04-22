# 列表常用方法

# 以下属于原地操作
x=[1,2,3]
id(x)  # 查看对象内存地址

x.append(4)
x.insert(0,0)
x.extend([5,6,7])  # 添加至尾部

x + [4]
x = x * 2  # 列表元素重复

x = [1,2,3,4,5,5,6]
x.pop()  # 弹出并返回尾部元素
x.pop(1)  # 弹出并返回指定位置的元素
x.clear()

x = [1,2,3,3,4,2]
x.remove(2)  # 删除首个值为2的元素

x = [1,2,2,3,4,4,3,3,45,5]
x.count(3)
x.index(45)  # 元素45在列表中首次出现的索引

x = list(range(11))
import random
random.shuffle(x)
x
x.sort(key=lambda item:len(str(item)), reverse=True)
x.reverse()
x.sort(key=str)  # 按转换为字符串后的大小排序
x.sort()  # 按照默认规则

# 使用 sorted(x) 和 reversed(x) 返回新列表
sorted(x)


gameresult = [['Bob',95.0,'A'],
              ['Alan',86.0,'C'],
              ['Mandy',83.5,'A'],
              ['Rob',89.3,'E']]
from operator import itemgetter
sorted(gameresult, key=itemgetter(2))  # 按照第3个元素进行升序排列
sorted(gameresult, key=itemgetter(2,0))  # 按照第3个元素升序，然后按照第1个元素升序
sorted(gameresult, key=itemgetter(2,0), reverse=True)

list1 = ["what","I'm","sorting","by","22"]
list2 = ["somthing","else","to","sort"]
pairs = zip(list1,list2)  # 把两个列表中对应位置元素配对
[item[1] for item in sorted(pairs, key=lambda x:x[0], reverse=True)]
x = [[1,2,3],[2,1,4],[2,2,1]]
sorted(x,key=lambda item:(item[1], -item[2]))  # 以第2个元素升序，第3个元素降序排序
x = ['aaaaa','bc','d','b','ba']
sorted(x,key=lambda item:(len(item), item))      # 先按长度排序，长度一样正常排序

x = list(range(11))
import random
random.shuffle(x)
x
list(zip(x,[1]*11))   # 多列表元素重新组合
list(zip(range(1,4)))  # zip()函数也可以用于一个序列或迭代对象
list(zip(['a','b','c'],[1,2]))   # 如果两个列表不等长，以短为准

enumerate(x)    #  枚举列表元素，返回enumerate对象
list(enumerate(x))    #  enumerate对象可迭代

list(map(str,range(5)))  # map()可将一个函数依次作用到序列或者迭代器对象上的每一个元素
def add5(v):
    return v+5
list(map(add5,range(10)))

def add(x,y):
    return x + y
list(map(add, range(5), range(5,10)))
list(map(lambda x,y : x+y, range(5), range(5,10)))
[add(x,y) for x,y in zip(range(5),range(5,10))]

from functools import reduce
seq = [1,2,3,4,5,6,7,8,9]
reduce(add,range(10))
reduce(lambda x,y:x+y,seq)
seq = ['foo','x41','?!','****']
def func(x):
    return x.isalnum()   # 测试是否为字母或数字
filter(func,seq)
list(filter(func,seq))
seq  # 不对原列表做任何修改
[x for x in seq if x.isalnum()]  # 用列表推导式实现相同功能
list(filter(lambda x:x.isalnum(), seq))  # 使用lambda表达式实现相同功能
list(filter(None,[1,2,3,0,0,0,4,0,5]))  # 制定函数为None，返回序列中等价于True的元素

import random
x = [random.randint(1,10) for i in range(10)]
list(map(lambda i : i+5,x))
import operator
y = [random.randint(1,10) for i in range(10)]
sum(map(operator.mul, x ,y))    # 向量内积
sum((i*j for i ,j in zip(x,y)))
list(map(operator.add,x,y))   # 两个等长的向量对应元素相加
list(map(lambda i,j : i+j ,x,y))
