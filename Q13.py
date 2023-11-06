# 13) Write a Python program to find the index of an item in a specified list.
ls=[11,21,31,41,51,61,71,81,91]
item=71
if item in ls:
    index=ls.index(71)
    print(index)
else:
    print("item is not in the list")