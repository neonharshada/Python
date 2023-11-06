# 18) Write a Python program to replace the last element in a list with another list.
# Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
# Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]
ls=[1, 3, 5, 7, 9, 10]
ls1=[2, 4, 6, 8]

ls2= ls + ls1
print(ls2)

ls.extend(ls1)
print(ls)

print(ls[0:6]+ls1[0:4])