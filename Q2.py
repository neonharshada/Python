# 2) Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}
mydict={0:10,1:20}
print("before adding",mydict)
mydict.update({2:30})
print("after adding",mydict)
