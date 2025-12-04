"""
主要针对类型: 字符串、列表、元组
"""
arr = [1, 2, 3, 6, 5, 4] #列表1

print(len(arr)) #获取字符串或列表的长度

print(sum(arr)) #获取列表元素的和(传列表或元组)

# 删除列表的第2号元素
del arr[2]

print(arr)

print("max:", max(arr)) #列表中的最大值
print("min:", min(arr)) #列表中的最小值

print(3 in arr) #某个数在不在列表里
print(5 in arr)

arr2 = ["a", "b", 3.14] #列表2

print(arr + arr2 )#列表1和列表2拼接

print(arr2 * 3) #重复3次列表串(和字符串很像)

arr3 = [1, 5, 3]
arr4 = [1, 2, 100]

print(arr3 > arr4) #逐个元素比较,有一个不满足将不成立(可用于比较运算符:> >= == < <=);字符串也能比较
