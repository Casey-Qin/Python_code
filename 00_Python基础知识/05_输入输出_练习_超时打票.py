"""
超市买苹果计算金额
需求:	
●  收银员输入苹果的价格price,单位:元/斤
●  收银员输入用户购买苹果的重量weight, 单位：斤
●  计算并输出付款金额:xxx元
"""

price  = int (input("请输入苹果价格:"))
weight = int (input("请输入苹果的重量:"))

money = price * weight

print("需付款金额:",money,"元")