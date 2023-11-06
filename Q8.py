# 8) Write a Python program access the index of a list.
# 	output : all the elements along with their index
ls=[i for i in range(11,20)]
for i,j in enumerate(ls):
    print(f"{i}:{j}")
