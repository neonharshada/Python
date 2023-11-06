# 1) Write a Python program to count the elements in a list until an element is a tuple.
#
# Sample input : list = [10, 20, 30, (40,50), 60]
# Sample output = 3
mylist=[10, 20, 30, (40,50), 60]
count=0
for i in mylist:
    if isinstance(i,tuple):
        break
    count +=1
print("Count the element until Tuple",count)

# 2) create a tuple to store 5 numbers and then sort it in ascending and descending order.
mytuple=(10, 20, 30, 40,50, 60)
print("Sort the elements of tuple")
print(sorted(mytuple))
print("sorted in reverse order")
print(sorted(mytuple,reverse=True))

# 3) Write a Python program to find the repeated items of a tuple.
mytuple=(1,2,3,3,4,5,6,7,7,8,8,9,6,7,2)
i_count={}
i_reapeted=[] #creating list for reapeted items

for i in mytuple:
    if i in i_count:
        i_count[i]+=1
        if i not in  i_reapeted:
            i_reapeted.append(i)
    else:
        i_count[i]=1

print("reapeted numbers in tuple:",i_reapeted)

#2nd method
my_tuple = (1, 2, 2, 3, 4, 4, 5, 6, 6)
ls=[i for i in my_tuple if my_tuple.count(i)>1]
ls1=list(set(ls))
print(ls)
