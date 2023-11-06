# 5) Write a Python program to create a dictionary from two lists without losing duplicate values.
# Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
# Expected Output: {'Class-VII': {2}, 'Class-VI': {2}, 'Class-VIII': {3}, 'Class-V': {1}})
x= ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
y= [1, 2, 2, 3]
mydict={key:value for (key,value) in zip(x,y)}
print(mydict)