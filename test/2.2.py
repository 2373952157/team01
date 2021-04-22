x = (1,2,3,4)
g = ((i+2)**2 for i in range(10))
g.__next__()   # 获取生成器对象中的元素
next(g)
