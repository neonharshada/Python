# 1) create first array "overs" with 4 elements
# 5,10,15,20
# create another array "runs_scored" with 4 elements and store
# no.of runs scored at the end of each over
# e.g.  40 runs at the end of 5th over , 75 runs at the end of 10th over etc.
#
# now create a line plot to show the relationship between "overs" and "runs_scored"
import numpy as np
from matplotlib import pyplot as py

over=[5,10,15,20]
runs=[40,75,120,150]

py.plot(over,runs,color='b',linestyle='-',marker='*',lw=2)

py.xlabel('Overs')
py.ylabel('Runs')
py.title('Overs Vs Runs Scored')

py.grid(True)
py.show()

