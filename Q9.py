# 9) create two-d array ,display it.
# Now accept a number from user and perform all arithmetic operations on each and
# every element of the array using that number.
import numpy as np
array1=np.array([[1,2,3],[4,5,6]])
print("2d array:",array1)

x=int(input("Enter a NUmber:"))

add_array=array1 + x
sub_array=array1 - x
multi_array=array1 * x
div_array=array1 / x

print("addition",sub_array)
print("subtraction",sub_array)
print("multiplication",multi_array)
print("division",div_array)

# 9) create two-d array ,display it. Now accept a number from user and
# perform all arithmetic operations on each and every element of the array using that number.
import numpy as np

np.random.seed(6)
ar=np.random.randint(1,50,9).reshape(3,3)
print(ar)
n=int(input("ebter a num"))
a=ar *n
print(a)
b=ar /n
print(b)
c=ar + n
print(c)
d=ar -n
print(d)

# 9) create two-d array ,display it. Now accept a number from user and
# perform all arithmetic operations on each and every element of the array using that number.
import numpy as np

np.random.seed(6)
ar=np.random.randint(1,50,9).reshape(3,3)
print(ar)
n=int(input("ebter a num"))
a=ar.__add__(n)
print(a)
b=ar.__sub__(n)
print(b)
c=ar.__mul__(n)
print(c)
d=np.divide(ar,n)
print(d)
e=ar.__truediv__(n)
print(e)



