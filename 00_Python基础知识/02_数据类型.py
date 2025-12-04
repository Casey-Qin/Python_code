'''
变量定义,基本数据类型
'''
# 字符串类型str
name = "肖志杰"
#整数类型int
age = 18
#浮点数类型 float
height = 185.5
#布尔类型 bool
handsome = True
#复数
compl = -3+4j

print("height:",height,"age:",age)
print(type(name))
print(type(height))
print(type(age))

print("-"*50)

""" 非法变量名
1. 只能由数字、字母、_(下划线)组成
2. 不能以数字开头
3. 不能是关键字
4. 区分大小写
"""
#不同大小写,是不同的变量
user_name = "xiao"
userName  = "zhi"
USERNAME  = "jie"

print(user_name)
print(userName)
print(USERNAME)
# 不同大小写,是不同的变量,但是不要这样使用,容易搞混

print("-"*50)

a = 5
b = 2

print("a + b  = ",a + b)
print("a - b  = ",a - b)
print("a * b  = ",a * b)
print("a / b  = ",a / b)  #得到float
print("a // b = ",a // b) #取整
print("a % b  = ",a % b)  #取模
print("a ** b = ",a ** b) #幂运算(a的b次方)

#字符串拼接
str1 = "hello"
str2 = "world"
print(str1 +str2)

# 字符串可以和数字相乘，重复a次
print(user_name * a)
