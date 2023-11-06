# 11) create one-d array of 8 numbers and then using "slicing" concept,
# 	a) print numbers from 1 to 4
# 	b) print all the numbers from 3rd position
# 	c) print last 3 numbers

import numpy as np
array1d=np.array([1,2,3,4,5,6,7,8])

array1=array1d[0:4]
print(array1)
array2=array1d[2:]
print(array2)
array3=array1d[-3:]
print(array3)
