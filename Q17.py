# 17) Write a Python program to sum all the items in a dictionary.
dict1={1:10,2:27,3:30}
a=0
b=0
for i,j in dict1.items():
    a+=i
    b+=j
print("sum all the items in a dictionary",a+b)