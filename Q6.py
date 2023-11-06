# 6) create two one-d arrays and then find out:
# 	a) common elements of both the array
# 	b) unique elements of first array
# 	c) unique elements of second array
import numpy as np
array1=np.array([1,2,3,4,5,6])
array2=np.array([1,2,3,7,8,9])
array3=np.intersect1d(array1,array2)
print("common ele of aaray1 and array2:",array3)
array4=np.setdiff1d(array1,array2)
print("unique elements of first array",array4)
array5=np.setdiff1d(array2,array1)
print("unique elements of second array",array5)

##################################
# 6) create two double dimension array and arrange (stack) them using "axis=0" "axis=1" and  "axis=2".
import numpy as np

arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2=np.array([[1,2,3],[14,15,16],[17,18,19]])

a=np.intersect1d(arr1 ,arr2)
print(a)
b=np.setdiff1d(arr1 ,arr2)
print(b)
c=np.setdiff1d(arr2 ,arr1)
print(c)






