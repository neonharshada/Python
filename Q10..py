## 10) accept start, end and how many numbers to be generated and then using "linspace" create numpy array.

import numpy as np

start=int(input("Enter a start value:"))
end=int(input("Enter a end value"))
how_many=int(input("Enter how many no.you want to be generated:"))

harsha=np.linspace(start,end,how_many)
print(harsha)


