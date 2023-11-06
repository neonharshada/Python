# 8) declare two 2d arrays and calculate the sum as per "axis=0" "axis=1" and "axis=2"
import numpy as np
array1=np.array([[1,2,3],[4,5,6]])
array2=np.array([[6,7,8],[9,10,11]])

sum_axis0=np.sum((array1,array2),axis=0)
print("sum_axis0",sum_axis0)
sum_axis1=np.sum((array1,array2),axis=1)
print("sum_axis1",sum_axis1)
sum_axis2=np.sum((array1,array2),axis=2)
print("sum_axis2",sum_axis2)