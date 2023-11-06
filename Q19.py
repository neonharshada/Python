# 19) Write a Python function that takes two lists and returns True if they have at least one common member.
def common_member(ls1,ls2):
    set1=set(ls1)  #drop duplicates for efficient checking
    for i in ls2:
        if i in set1:
            return True
        else:
            return False
ls1=[1,2,3,4,5,6]
ls2=[4,5,5,6,7,8]
result=common_member(ls1,ls2)

if result:
    print(" they have at least one common member")
else:
    print("they dont have common number")

