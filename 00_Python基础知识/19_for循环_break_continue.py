"""
break和continue是专门在循环中使用的关键字
break:某一条件满足时,不再执行循环体中后续代码,并退出循环
continue:某一条件满足时,不再执行本次循环体中后续代码,但进入下一次循环判断

"""
# break
for i in range(5):
    if i == 3:#如果i==3,满足条件,执行break跳出,后续代码将不会执行
        break
    print(i)
    
print("-"*50)
    
# continue
for i in range(5):
    if i == 3:#如果i==3,满足条件,执行continue跳出单次,单次后续代码不会执行,下次条件不满足3,后续代码会执行
        continue
    print(i)