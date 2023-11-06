# 1) Write a Python program to create a dictionary of keys x, y, and z
# where each key has as value a list from 11-20, 21-30, and 31-40 respectively.
# Access the fifth value of each key from the dictionary.
# {'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
# 'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
# 'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
# 15
# 25
# 35
mydict={'x':[i for i in range(11,20)],'y':[i for i in range(21,30)],'z':[i for i in range(31,40)]}
print(mydict)
for i in mydict:
    print(mydict[i][4])

