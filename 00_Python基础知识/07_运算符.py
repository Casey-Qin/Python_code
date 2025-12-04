'''
赋值运算符
=	赋值
+=	加等于
-=	减等于
*=	乘等于
/=	除等于
//=	整除等于
%=	模等于
**=	幂等于
--------------------
比较运算符
==	等于
!=	不等于
>	大于
<	小于
>=	大于等于
<=	小于等于
--------------------
逻辑运算符
and	逻辑与
or	逻辑或
not	逻辑非
'''

#-------------------赋值运算符
a = 5
b = 2

a += b
print(a) # 7
a -= b
print(a) # 5
a *= b
print(a) # 10
a /= b
print(a) # 5.0(除法运算后类型为float)
a //= b
print(a) # 2.0
a **= b
print(a) # 4.0
a %= b
print(a) # 0.0
print("-"*30)
#-------------------比较运算符
a = 5
b = 2
c = a == b
print(c) #False
c = a != b
print(c) #True
c = a > b
print(c) #True
c = a < b
print(c) #False
c = a >= b
print(c) #True
c = a <= b
print(c) #False
print("-"*30)
#-------------------逻辑运算符

print("True and False: ", True and False) # 逻辑与----False
print("True and True: ", True and True) # 逻辑与----True

print("True or False: ", True or False) # 逻辑或----True
print("False or False: ", False or False) # 逻辑或----False

print("not True: ", not True)# 逻辑非----False
print("not False: ", not False)# 逻辑非----True