# 15) Write a Python program to iterate over two lists simultaneously.
ls1=[1,2,3,4]
ls2=["harshada","paras","monu","sahil"]
for i,j in zip(ls1,ls2):
    print(i,j)