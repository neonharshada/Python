# 13) Write a Python program to match key values in two dictionaries.
# Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y
mydict1={'key1': 1, 'key2': 3, 'key3': 2}
mydict2={'key1': 1, 'key2': 2}
# for i in mydict1:
#     if i in mydict2:
#        if mydict1[i]==mydict2[i]:
#            print(i,":",mydict1[i])

dict1={i:mydict1[i] for i in mydict1 if i in mydict2 and mydict1[i]==mydict2[i]}
print(dict1)
# for i in dict1:
#     print(i,":",dict1[i])



