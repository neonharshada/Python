# 5) create two double dimension array and arrange (stack) them using "axis=0" "axis=1" and  "axis=2".
import numpy as np
array1=np.array([[1,2,3],[4,5,6]])
array2=np.array([[6,7,8],[9,10,11]])
array3=np.stack((array1,array2),axis=0)
print("stack axis 0",array3)
array4=np.stack((array1,array2),axis=1)
print("stack axis 1",array4)
array5=np.stack((array1,array2),axis=2)
print("stack axis 2",array5)

