# 15) Write a Python program to remove a key from a dictionary.
dict1={1:10,2:20,3:30}
n=int(input("Enter a key"))
if n in dict1:
    del dict1[n]
else:
    print("key is not present here")
print(dict1)
