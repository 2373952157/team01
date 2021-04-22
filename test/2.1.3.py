# 列表推导式

# 1.
aList = [x*x for x in range(10)]
# 等价于
aList = []
for x in range(10):
    aList.append(x*x)
# 等价于
aList = list(map(lambda x:x*x,range(10)))


# 2.
freshfruit = [' banana ',' loganberry ',' passion fruit   ']
aList = [w.strip() for w in freshfruit]
# 等价于
freshfruit = [' banana ',' loganberry ',' passion fruit   ']
aList = []
for item in freshfruit:
    aList.append(item.strip())
# 等价于
freshfruit = [' banana ',' loganberry ',' passion fruit   ']
aList = list(map(lambda x:x.strip(),freshfruit))
# 等价于
freshfruit = [' banana ',' loganberry ',' passion fruit   ']
aList = list(map(str.strip, freshfruit))

# 3.
sum([2**i for i in range(64)])

# 4.
vec = [[1,2,3],[4,5,6],[7,8,9]]
[num for elem in vec for num in elem]
# 等价于
vec = [[1,2,3],[4,5,6],[7,8,9]]
result = []
for elem in vec:
    for num in elem:
        result.append(num)

# 5.
import os
[filename for filename in os.list]


