# count = 1
# sum = 0
# while count <= 100:
#     count = count + 1
#     sum = sum + count
#
# print(sum)
#
# count = 1
# while count <=100:
#     if count % 2 == 0:
#         print(count)
#     count = count + 1
#



# count = 1
# sum = count
# while count < 100:
#     count = count + 1
#     if count % 2 == 0:
#         sum = sum - count
#     else:
#         sum = sum + count
#
# print(sum)



# pass1 = "novirus"
# n = 1
# while n <= 3:
#     passwd = input("please in put your password: \n\r")
#     if passwd == pass1:
#         print("you log in successfully")
#         break
#     else:
#         print("wrong password, please input correct password again!")
#         if n == 3:
#             print("you have inputted 3 times wrong password, quit!!!")
#             break
#     n = n + 1

name = "李杰"
v = name.encode("utf-8")
v1 = name.encode("GBK")
print(len(v))