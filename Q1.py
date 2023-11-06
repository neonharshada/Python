# 1)Write a Python program to find all the values in a list are greater than a specified number.
ls=[10,20,25,11,23,18,20,22]
# for i in ls:
#     if i>15:
#         print(f"value in a list are greater than 15:{i}")

ls1=[i for i in ls if i>15]
print(ls1)


