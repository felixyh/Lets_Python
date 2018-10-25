#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 23、Python2 中的range 和Python3 中的range 的区别？

# Python 2 先生成所有数到内存中， Python 3 不会

# 24、实现一个整数加法计算器：
# 如：
# 	content=input('请输入内容：')#  如：5+9或5+9或5+9

# content = input("please input the content: \r\n")
# numbers = content.split("+")
# s = 0
# for number in numbers:
#     s = s + int(number)
#
# print("the sum is %d" % s)


# 25、计算用户输入的内容中有几个十进制小数？几个字母？
# 如：
# 	content=input('请输入内容：')#  如：asduiaf878123jkjsfd--‐213928

# content = input("please input the content: \r\n")
# dig = ""
# alpha = ""
# for item in content:
#     if item.isdigit():
#         dig = dig + item
#     else:
#         alpha = alpha + item
#
# print(len(dig))
# print(len(alpha))

# 26、简述int和9等数字以及str和"xxoo"等字符串的关系？


# 27、制作趣味模板程序
# 需求：等待用户输入名字、地点、爱好，根据用户的名字和爱好进行任意现实
# 如：敬爱可亲的xxx，最喜欢在xxx 地方干xxx
# name = input("please input name: \r\n")
# location = input("please input location: \r\n")
# favor = input("please input favor: \r\n")
#
# content = "敬爱可亲的{}，最喜欢在{} 地方干{}!"
# print(content.format(name, location, favor))

# 28、制作随机验证码，不区分大小写。
#     流程：
#         - 用户执行程序
#         - 给用户显示需要输入的验证码
#         - 用户输入的值
#             用户输入的值和显示的值相同时现实正确信息；否则继续生成随机验证码继续等待用户输入
#         生成随机验证码代码示例：

# while True:
#     def check_code():
#         import random
#         checkcode = ''
#         for i in range(4):
#             current = random.randrange(0, 4)
#             if current != i:
#                 temp = chr(random.randint(65, 90))
#             else:
#                 temp = random.randint(0, 9)
#             checkcode += str(temp)
#         return checkcode
#
#
#     code = check_code()
#     print(code)
#
#     usercode = input("please input the code you've seen: \r\n")
#     if usercode == code:
#         print("corret code, you've successfully login")
#         break
#     else:
#         print("wrong code, please try again!")


# 29、开发敏感词语过滤程序，提示用户输入内容，如果用户输入的内容中包含特殊的字符：
# 如"苍老师" "东京热"，则将内容替换为***
# content = input("please input the content: \r\n")
# keywords = ["苍老师", "东京热"]
# for word in keywords:
#     if content.find(word) >= 0:
#         content = content.replace(word, "***")
#     else:
#         pass
# print(content)


# 30、制作表格
# 循环提示用户输入：用户名、密码、邮箱（要求用户输入的长度不超过20 个字符，如果超过则只有前20 个字符有效）
# 如果用户输入 q 或Q 表示不再继续输入，将用户输入的内容以表格形式打印

# 字符串center 魔法函数居中显示
def centerstr(content):
    cen = str(content)
    cen = cen[0:20]
    cen = cen.center(20)
    return cen

# 字符串魔法函数format，格式化显示
def formatrow(a, b, c):
    row = "{} | {} | {}"
    printrow = row.format(centerstr(a), centerstr(b), centerstr(c))
    return printrow

# 定义空列表，存储表格每一行
table = []
while True:
    name = input("please input your name:\r\n")
    if name in ["q", "Q"]:
        break
    passwd = input("please input your password:\r\n")
    if passwd in ["q", "Q"]:
        break
    mail = input("please input your mail address:\r\n")
    if mail in ["q", "Q"]:
        break

    # row = "{} | {} | {}"
    # printrow = row.format(centerstr(name), centerstr(passwd), centerstr(mail))
    printrow = formatrow(name, passwd, mail)
    table.append(printrow)

#打印表格标题
title = formatrow("name", "passoword", "mail address")
print(title)
print("-"*62)

#循环打印每一行
for item in table:
    print(item)
    print("-"*62)


