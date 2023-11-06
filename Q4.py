# 4) Write a Python program to count the number of strings where the string length is 2 or more and the first and
# last character are same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221'] """
# output
# 	aba      1221
ls = ['abc', 'xyz', 'aba', '1221']
# count=0
# for i in ls:
#     if i.__len__()>=2 and i[0]==i[-1]:
#         count+=1
# print(count)
ls1=[i for i in ls if len(i)>=2 and i[0]==i[-1]]
print(len(ls1))


