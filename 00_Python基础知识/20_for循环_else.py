"""
循环也可以像if语句一样结合else。
else 中的语句会在循环正常执行完(即没有通过 break或其他异常情况中断循环)的情况下执行,
while循环也是如此
"""

for i in range(10):
    if i == 3:
        break  # 如果i==3,满足条件,执行break跳出,后续代码将不会执行
    print("媳妇, 我错了", i)
else:
    print("顺利完成, 原谅我了")

# else的代码只在正常循环完毕时执行, 出现break则不再执行
print("---------------------------")

for i in range(10):
    if i % 2 == 0:
        continue  # 如果i==3,满足条件,执行continue跳出单次,单次后续代码不会执行,下次条件不满足3,后续代码会执行
    print("媳妇, 我错了", i)
else:
    print("顺利完成, 原谅我了")
