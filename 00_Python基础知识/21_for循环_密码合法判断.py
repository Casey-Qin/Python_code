"""
判断登录密码hhew2383dW_fkf&E@^是否合法。
1. 密码必须是数字、字母(大小写都可以)、和下划线，否则不合法
2. 如果密码合法,就输出"密码合法"
"""
password = input("请输入密码: ")

# 1. 定义容器，保存所有的 数字 字母 _
container = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'

# 2. for循环遍历密码中每一个元素
for password_judge in password :
    if password_judge not in container:
        print("密码不合法,包含非法字符:",password_judge)
        break
else:
    print("密码合法")