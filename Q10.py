# 10) Write a Python program to check whether the n-th element exists in a given list.
ls=[1,2,3,4,5,6,6,7,8,9,2]
n=int(input("enter a number"))
if n<=len(ls):
    print(f"{n} element exist:",ls[n])
else:
    print(" element dose not exit")