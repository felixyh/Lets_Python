#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 22、请用代码实现：
# 	a.利用下划线将列表的每一个元素拼接成字符串，li＝"alexericrain"
# 	b.利用下划线将列表的每一个元素拼接成字符串，li＝['alex','eric','rain']（可选）

li = "alexericrain"
v = li[0]
for i in li:
    v = v + "_" + i
print(v)


