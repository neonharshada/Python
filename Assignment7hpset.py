# 1) accept 10 values from user and add them inside the set.
# now accept one more value from user and if it is present in the set,remove
# it. Make sure program doesn't give any error if number is not there inside the set.
myset=set()
for i in range(1,11):
    num=int(input("Enter a number:"))
    myset.add(num)
print("Myset",myset)
num1=int(input("Enter a number:"))
if num1 in myset:
    myset.remove(num1)
else:
    print("number is not from set")
print("Myset",myset)

#2nd method
my_set = {int(input("Enter a value: ")) for _ in range(10)}
value= int(input("Enter a value to check:"))

if value in my_set:
    my_set.remove(value)
else:
    print(f"{value} is not present in the set.")
print(my_set)
