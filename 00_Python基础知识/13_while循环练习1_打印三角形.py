'''
根据用户输入的数值n,打印n行三角形
'''

n = int(input("请输入行数:"))

print("----------正三角----------")
row1 = 1
while row1 <= n:
    print("*"*row1)
    row1 += 1
    
print("----------倒三角----------")
row2 = n
while row2 >= 1:
    print("*"*row2)
    row2 -= 1