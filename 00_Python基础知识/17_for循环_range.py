'''
range() 可创建一个整数列表。range()相当于数学中的左闭右开区间（包含左,不包含右）
'''
arr = range(10)#包含左,不包含右,等于:(0,10)0可以省写

for a in arr:
    print(a,end="")#遍历出0~9
print()

lst = list(range(10))
print(lst,type(lst)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9] <class 'list'>

# [start, stop) 开始数值~结束数值(不包含最后一个)
for i in range(5, 10):
    print(i, end=" ")
    
print()

# [start, stop) step  开始数值~结束数值(不包含最后一个),步长
for i in range(2, 10, 2):
    print(i, end=" ")

print()

# [start, stop) step 倒序遍历;开始数值~结束数值(不包含最后一个),步长(步长为负数表示每次加负一)
for i in range(10, 0, -1):
    print(i, end=" ")

print()