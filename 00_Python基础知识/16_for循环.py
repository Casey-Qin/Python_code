'''
for 临时变量 in 列表或字符串等可迭代对象:
	执行的代码
 -------------------------------------
in和not in
in 操作符用于判断元素是否存在于容器中，如果在容器中,返回 True,否则返回 False
'''

string = "HelloWorld"

for s in string:
    print(s)    # H
                # e
                # l
                # l
                # o
                # W
                # o
                # r
                # l
                # d
print("H" in string)          #True
print("h" in string)          #False
print("lo" in string)         #True
print("ol" in string)         #False
print("FF" not in string)     #True