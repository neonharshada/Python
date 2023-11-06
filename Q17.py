# 17) Write a Python program to remove duplicates from a list.
ls=[1,2,2,3,4,5,5,5,6,7]
uniqels=[]
for i in ls:
    if i not in uniqels:
        uniqels.append(i)
print(uniqels)

ls1=list(set(ls))
print(ls1)

uniqels1=[]
[uniqels1.append(i) for i in ls if i not in uniqels1 ]
print(uniqels1)
