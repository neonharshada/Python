# 2) Write a Python program to find the list of words that are longer than n from a given list of words.
ls=["harshada","sanjay","patil","paras","monupatil"]
ls1=[i  for i in ls if len(i)>5]
print(ls1)