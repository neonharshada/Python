# 18) Write a Python script to merge two Python dictionaries.
# mydictionary1={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
# mydictionary2={7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144}
# output:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144}
mydict1={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
mydict2={7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144}

mydict1.update(mydict2)
print(mydict1)
