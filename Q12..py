# 12) create 2 d array (4*3) with following values:
# [[10,20,30,40],[50,60,70,80],[90,100,110,120]]
#
# now using array slicing concept display following values
# 	a) display   50  60  70  80
# 	b) display 100 and 110
# 	c) display 30 70 and 110
# 	d) display 50  60  90 and 100
import numpy as np
array_2d=np.array([[10,20,30,40],[50,60,70,80],[90,100,110,120]])

array1=array_2d[1:2]
print(array1)
array2=array_2d[2:3,1:3]
print(array2)
array3=array_2d[:,2:3]
print(array3)
array4=array_2d[1:,:2]
print(array4)