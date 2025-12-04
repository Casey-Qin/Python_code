import random


"""
需求：
1. 从控制台输入要出的拳 —— 
    石头(1)/剪刀(2)/布(3)/
2. 电脑 随机 出拳 —— 先假定电脑只会出石头，完成整体代码功能
3. 比较胜负并输出结果
"""
# 1:石头,2:剪刀,3:布

my = int(input("请输入你要出什么?:"))
computer = random.randint(1, 3)


if(my == 1 and computer == 2) or (my == 2 and computer == 3) or (my == 3 and computer == 1):
    print("我赢了,我出",my,",电脑出",computer)
elif my == computer :
    print("平局,我出",my,",电脑出",computer)
else :
    print("我输了,我出",my,",电脑出",computer)