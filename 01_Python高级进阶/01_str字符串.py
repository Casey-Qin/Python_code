string = "hello"
print(string[1])

print("---------------------------判断")
print("abCD".isalpha())  # 纯字母
print("123".isdecimal()) # 是否数字 isdigit
print("一二三456".isnumeric()) # 支持汉字数字

print("abc".startswith("ab"))#是否已("xx")开头的
print("abc".startswith("c"))

print("---------------------------查找")
print("abcdef".find("cd"))# 找到内容，返回第一个数的索引 2
print("abcdef".find("x")) # 找不到的内容，返回-1
print("www.itheima.com".rfind(".")) # right从右往左找 11
print("abcdef.bcom".replace("b", "B", 2))# 替换(被替换的字母,替换后的字母,替换个数)替换个数不写,默认全部替换

print("----------------------------切割")
name_list = "张三|李四光|王大拿".split("|")#以字符"|"进行切割
print(name_list, type(name_list))
ss = "0123456789"
print(ss[4:7])#取出从4到7的数,取前不取尾

name_list = """张三\t李四\n王五\r\n赵六"""
print(name_list.split())

print("--------------------------去空白")
print("  abc     ".strip())
