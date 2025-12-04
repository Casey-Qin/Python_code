

row = 1

while row <= 5:#循环5行
    col = 1
    while col <= 5:# 每行循环5次
        print(col,end=" ")#每次循环+1,并且没有换行,即打印出:1 2 3 4 5 
        col += 1
    print()
    row += 1