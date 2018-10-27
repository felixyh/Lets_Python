#!/usr/bin/env python
# -*- coding:utf-8 -*-
# print("hello, world!")


tu = (1, 2)
v1 = tu[0]

info = {
    1: "v1",
    "K2": "v2",
    # True: "123"
    "k3": (11, 22),
}
for k, v in info.items():
    print(k, v)

print(info.items())
print(info.keys())
print(info.values())




