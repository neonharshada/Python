# 12) Write a Python program to map two lists into a dictionary.
# e.g.
# given
# prnnos=[1,2,3,4,5,6]
# names=['abc','def','pqr','lmn','xyz','uvw']
# output:
# {1: 'abc', 2: 'def', 3: 'pqr', 4: 'lmn', 5: 'xyz', 6: 'uvw'}
prnnos=[1,2,3,4,5,6]
names=['abc','def','pqr','lmn','xyz','uvw']
mydict=dict(zip(prnnos,names))
print(mydict)

