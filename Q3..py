# 3) create numpy double dimension array of 3*3 to store your initial and display them in a tabular form.
import numpy as np
my_array=np.array([[1,2,3],[4,5,6],[7,8,9]])
for i in my_array:
    for j in i:
        print(j,end=" ")
    print()

# 3) create numpy double dimension array of 3*3 to store your initial and display them in a tabular form.
import numpy as np
a=[[1,2,3],[4,5,6],[7,8,9]]
for i in range (a.__len__()):
    for j in range(0,a[i].__len__()):
        print(a[i][j],end=" ")
    print()