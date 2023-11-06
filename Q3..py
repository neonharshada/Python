# 3) accept 10 values and store them in the Series.
# Now perform following operations:
#
# a) display the entire Series
# b) extract 3rd element
# c) extract elements from 4 to 7
# d) extract elements from fourth last till the last element
# e) extract first 3 elements
# f) extract elements from the 5th position

import pandas as pd

Values=[]

for i in range(0,10):
    value=int(input(f"Enetr the values{i+1}:"))
    Values.append(value)

series=pd.Series(Values)

print("Entire series",series)

third_element=series[2]
print("third element",third_element)

subset=series[3:7]
print("elements from 4 to 7",subset)

subset1=series[-4:]
print("elements from fourth last till the last element",subset1)

subset2=series[:3]
print("extract first 3 elements",subset2)

subset3=series[4:]
print("extract elements from the 5th position",subset3)