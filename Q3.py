# 3) Write a Python program to get the largest number from a list.

ls=[10,5,25,20,2]
# max_no=max(ls)
# print(max_no)
largest_no=ls[0]
for i in ls:
    if i>largest_no:
        largest_no=i
print(largest_no)