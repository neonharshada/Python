# 1) create a list, accept 5 numbers , store them in the list and finally convert that list to numpy array.
import numpy as np
Mylist=[]
for i in range(0,5):
    num = input("Enter a Number:")
    Mylist.append(num)
disp=np.array(Mylist)
print("numpy of Mylist:",disp)
