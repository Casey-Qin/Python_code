'''
需求:
●  在控制台依次提示用户输入:姓名name、公司com、职位title、电话telephone、邮箱email
●  按照以下格式输出：
******************************
    公司名称
    姓名(职位)
    电话:电话
    邮箱:邮箱
******************************
'''

name      = input("请输入您的姓名:")
com       = input("请输入您的公司:")
title     = input("请输入您的职位:")
telephone = input("请输入您的电话:")
email     = input("请输入您的邮箱:")

print("*"*30)
print()

print(com)
print(f"{name}({title})")#可以使用f"{}"拼接,大括号内放参数,冒号范围内可以加括号即可显示出__括号包裹的参数
print(telephone)
print(email)

print()
print("*"*30)
