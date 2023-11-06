# 4) create one-d numpy array of 12 elements , accept 12 numbers and display them.
# Now convert this one-d array into (4*3) two-d array and display it in a tabular form.
import  numpy as np
my_array=np.empty(12)  #create one-d numpy array of 12 elements
for i in range(12):
    num= input(f"Enter a Number{i+1}:")
    my_array[i]=num
print("1d array:",my_array)
array_2d=my_array.reshape(4,3)
print("2d array:",array_2d)
for i in array_2d:
    for j in i:
        print(j,end="\t")
    print()

###################################
import numpy as np

list=[]
for i in range(0,12):
    n=int(input("enter a num"))
    list.append(n)
b=np.array(list)
print(b)
for i in b:
    for j in i:
        print(j,end="")

