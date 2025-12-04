"""
打印99乘法表
"""
# 正序
row = 1
while row <= 9 :
    col = 1
    while col <= row :
        print("%d x %d = %-2d" %(col, row, col*row),end="  " )
        col += 1
    print()
    row += 1
    
print("-"*100)

# 倒序
row = 9
while row >= 1 :
    col = 1
    while col <= row:
        print("%d x %d = %-2d" %(col, row, col*row),end="  " )
        col += 1
    print()
    row -= 1