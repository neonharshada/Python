# 14) Write a Python program to insert a given string at the beginning of all items in a list.
# Sample list :[1,2,3,4] , string : emp
# Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
ls=[1,2,3,4]
#str1="emp"
ls1=[]
for i in ls:
    ls1.append(f"emp{i}")
print(ls1)

