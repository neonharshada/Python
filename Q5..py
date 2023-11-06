# 5) accept 5 names,designations and salaries and display them with DataFrame.

from pandas import *

data=[]

for i in range(0,5):
    names=input(f"enter the name{i+1}:")
    designations=input(f"Enter the designation for {names}:")
    salaries=int(input(f"Enter a salary for {names}:"))
    data.append([names,designations,salaries])

dframe=DataFrame(data,columns=['Name','Designation','Salaries'])  #give names to the colunms

print(dframe)