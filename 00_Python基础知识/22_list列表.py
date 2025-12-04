"""
list列表
列表可以增加新的元素，删除元素，修改元素。还可以对列表进行排序等操作
"""
# 以701宿舍成员为例
# 列表初始化
name_list = ["邹国弘", "肖志杰", "覃桂喜", "汪明茁"]

# 10月29汪明茁搬出宿舍
# 删除元素 Remove
name_list.remove("汪明茁")

# 10月30徐文杰搬进宿舍
# 添加元素 Create
name_list.append("徐文杰")

# 假设弘哥毕业,舍管搞错性别安排进来个大美女
# 修改元素 Update
name_list[0] = "大美女"

# 查询
print("-----------------------列表查询")
print(name_list)#查询全部
print(name_list[0])#查询单个
for name in name_list:#for循环遍历
    print(name)

print("-----------------------列表的排序")
lst = [2 ,5, 1, 3, 22, 12]
lst.sort()  # 排序
lst.sort(reverse=True)  # 倒序
print(lst)

print("-----------------------列表的嵌套")
students = [
    ['流川枫', "佐助", "柯南"],
    ["周杰伦", "自来也"]
]
print(students[0][1])
print(students[0][2])
# print(students[1][6]) # IndexError: list index out of range
#-----------------------列表索引超出范围