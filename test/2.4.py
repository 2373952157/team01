a = {3,5}
type(a)

import random
import time

x = list(range(10000))
y = set(range(10000))
z = dict(zip(range(1000),range(10000)))
r = random.randint(0,9999)

start = time.time()
for i in range(999999):
    r in x
print('list,time used:',time.time()-start)

start = time.time()
for i in range(999999):
    r in y
print('set,time used:',time.time()-start)

start = time.time()
for i in range(999999):
    r in z
print('dict,time used:',time.time()-start)

s = {1,2,3}
s.add(3)
s.update({3,4})  # 更新（添加）
s.discard(4)   # 删除，不存在则忽略
s.remove(5)  # 删除，不存在则报错
s.pop()  # 删除并返回一个元素


a_set = set([8,9,10,11,12,13])
b_set = {0,1,2,3,7,8}
a_set | b_set  # 并集
a_set.union(b_set)   # 并集
a_set & b_set  # 交集
a_set.intersection(b_set)  # 交集
a_set.difference(b_set)  # 差集
a_set - b_set  # 差集
a_set.symmetric_difference((b_set))  # 对称差集
a_set ^ b_set  # 对称差集

x = {1,2,3}
y = {1,2,5}
z = {1,2,3,4}
x.issubset(y)  # 测试是否为子集,False
x.issubset(z)  # True

from enum import Enum
class Color(Enum):  # 创建自定义枚举类
    red = 1
    blue = 2
    green = 3
Color.red   # 访问枚举的对象
type(Color.green)  # 查看枚举的类型
isinstance(Color.red,Color)
