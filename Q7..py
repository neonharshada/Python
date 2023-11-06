# 7) accept no.of rows and no. of cols from the user , create two-d array accordingly.
# Now calculate the sum as per "axis=0" and "axis=1"
import numpy as np
row_no=int(input("Enter no. of rows:"))
clnm_no=int(input("Enter no.of columns:"))

array1=np.empty((row_no,clnm_no))

for i in range(row_no):
    for j in range(clnm_no):
        array1[i][j]=int(input(f"Enter elements value at row{i},cloumn{j}:"))
print("array:",array1)
sum_axis0=np.sum(array1,axis=0)
print("sum st axis 0:",sum_axis0)
sum_axis1=np.sum(array1,axis=1)
print("sum st axis 1:",sum_axis1)

# 7) accept no.of rows and no. of cols from the user , create two-d array accordingly. Now calculate the sum as per "axis=0" and "axis=1"
import numpy as np

row=int(input("Enter a row"))
col=int(input("Enter a col"))
ls=[]
print("elements")
for i in range(row*col):
    n=int(input("Enter a num"))
    ls.append(n)
a=np.array(ls).reshape(row,col)
print(a)
b=np.sum(a,axis=0)
print(b)
c=np.sum(a,axis=1)
print(c)

