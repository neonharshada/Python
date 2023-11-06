# 3) Write a Python script to check whether a given key already exists in a dictionary.
# mydict={'a':120,'b':210,'c':320}
#
# for i in mydict:
#     n = input("enter a key")
#     if n in mydict:
#         print("key is exists")
#     else:
#         print("key not exists")
#     break
mydict={'a':120,'b':210,'c':320}
n =input("enter a key")
print("key exist") if(n in mydict) else print("key dose not exist")
