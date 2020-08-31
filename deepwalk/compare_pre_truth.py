import numpy as np
from collections import Counter
fi = open('E:\deepwalk-master\example_graphs\_footballtruth.txt', 'r', encoding='utf-8')
fiT = open('E:\deepwalk-master\example_graphs\_football pred_community 1000times.txt', 'r', encoding='utf-8')
# 读取文档
lines = fi.readlines()
arr = []
# 外层循环：遍历所有行
for line in lines:
    # 内层循环：遍历每一行
    line = line.strip()
    temp = list(map(int, line.split(" ")))
    arr.append(temp)
li = []
for i in arr:
    li.append(i[1])
m = Counter(li)
print(m)

arr2 = []
lines2 = fiT.readlines()
for line in lines2:
    # 内层循环：遍历每一行
    line = line.strip()
    temp = list(map(int, line.split(" ")))
    arr2.append(temp)
# arr.sort(key=lambda elem: elem[1])
# print(arr)
li2 = []
for i in arr2:
    li2.append(i[1])

n = Counter(li2)

print(n)


# print(type(arr))
# print(arr[np.lexsort(arr[:, ::-1].T)])
