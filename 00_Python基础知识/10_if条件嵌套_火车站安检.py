#import sys #使用sys.exit()函数需导入sys头文件;sys.exit()函数是用在条件不满足的情况下及时返回,代码不再往下执行了
"""
需求：
1. 定义布尔型变量 has_ticket 表示是否有车票
2. 定义整型变量 knife_length 表示刀的长度，单位：厘米

3. 首先检查是否有车票，如果有，才允许进行 安检
4. 安检时，需要检查刀的长度，
5. 判断是否超过 20 厘米
  a 如果不超过 20 厘米，安检通过
  b. 如果超过 20 厘米，提示刀的长度，不允许上车
6. 如果没有车票，不允许进门
"""
has_ticket = input('是否有火车票("是"或"否"):')
if has_ticket == '是':
  knife_length = int(input('是否携带刀具并输入长度(无携带输入0)'))
  if knife_length <= 20:
    print(f"通过安检")
  else:
    print(f"不允许上车,携带刀具长度:{knife_length}cm")
else:
  print("没有火车票,不允许进站")