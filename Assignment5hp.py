# 1) create a list , accept a number,name and a float value from user and store it inside the list.

# now accept one more name from user and insert it at 2nd position.

# accept a number and append it at the end of the list.
# print the entire list.
mylist = []
number = int(input("Enter a numbar:"))
name = input("Enter a name:")
float = float(input("Enter a float value:"))
mylist.append(number)
mylist.append(name)
mylist.append(float)
print("MyList", mylist)
name1 = input("Enter a name:")
mylist.insert(1, name1)
number2 = int(input("Enter a number:"))
mylist.append(number2)
print(mylist)

# 2) first create list empty. accept numbers till user enters 0 and store them inside the list. Print the list and its length.
mylist1=[]
while True:
        num=int(input("Enter the numbers:"))
        if num == 0:
            break
        mylist1.append(num)
print("Mylist" ,mylist1)
print("Mylist length",len(mylist1))

# 3) accept 5 numbers, store them inside the list and display it. Now add 3 more numbers [hardcoded] at the end of the list using "extend" method.

mylist =[]
for i in range(1,6):
    num=int(input("Enter a number:"))
    mylist.append(num)
print(mylist)
mylist1=[10,20,30]
mylist.extend(mylist1)
print(mylist)

# mylist7=[int(input("Enter a num:")) for i in range(1,6)]
# print(mylist7)  #make list using comprehension


# 4) accept a number,string,decimal,boolean value and a character from the user and store it inside the list.
# First print the list from the beginning and then from the end.
mylist=[]
num=int(input("Enter a number:"))
string=input("Enter a string:")
decimal=float(input("Enter a decimal:"))
boolean=bool(input("Enter a Boolean:"))
char=input("Enter a character:")
mylist.append(num)
mylist.append(string)
mylist.append(decimal)
mylist.append(boolean)
mylist.append(char)
print("Mylist",mylist)
print("Mylist",mylist[::-1])

# 5) accept 5 numbers, store them inside the list. now accept a number from user which he would like to remove from the list and  after removing it, display the list.
mylist = []
for i in range(1, 6):
    num = int(input("Enter a number:"))
    mylist.append(num)

print("Mylist", mylist)
num1 = int(input("Enter a number:"))
if num1 in mylist:
    mylist.remove(num1)
else:
    print("number is not from list")
print(mylist)

#2nd method
mylist7=[int(input("Enter a num:")) for i in range(1,6)]
print(mylist7)
num=int(input("enter a num"))
ls=[i for i in mylist7 if i !=num]
print(ls)

# 6) accept 5 numbers, store them inside the list. now accept a position from user ,
# remove the element from that position and  after removing it, display the list.
mylist = []
for i in range(1, 6):
    num = int(input("Enter a number:"))
    mylist.append(num)

print("Mylist", mylist)
i = int(input("Enter a number:"))
if i >= 0 and i < 6:
    mylist.pop(i)
else:
    print("number is not from list")
print(mylist)
#2nd method
mylist7=[int(input("Enter a num:")) for i in range(1,6)]
print(mylist7)
num=int(input("enter a num"))
ls=[j for i,j in enumerate(mylist7) if i !=num]
print(ls)

# 7) create a list and store string,number,character,boolean,decimal values respectively inside it.
# Now slice it in following ways:
# a) display it in reverse order
# b) list all the elements from 2nd position
# c) list the elements from 1st to 3rd position
# d) slice it from 1st to 3rd elements from the end.
mylist=[]
num=int(input("Enter a number:"))
string=input("Enter a string:")
decimal=float(input("Enter a decimal:"))
boolean=bool(input("Enter a Boolean:"))
char=input("Enter a character:")
mylist.append(num)
mylist.append(string)
mylist.append(decimal)
mylist.append(boolean)
mylist.append(char)
print("Mylist",mylist)
print(mylist[::-1])
print(mylist[2:])
print(mylist[1:4])
print(mylist[1:3])

# 8) Note: use List comprehension
#  create a list with the numbers from 1 to 20
#  create one more list which should contain only odd numbers from the first list.
mylist=[i for i in range(1,21)]
mylist1=[i for i in range (1,21)if i%2!=0]
print("My list of numbers 1-20",mylist)
print("Mylist of odd number",mylist1)

# 9) accept 5 names and store them in list. Now sort the list in ascending order display and then in descending order.
mylist = []
for i in range(1, 6):
    num = int(input("Enter a number:"))
    mylist.append(num)
print("Mylist",mylist)
mylist.sort()
print("Mtlist in ascending",mylist)
mylist.sort(reverse=True)
print("Mylist in descending",mylist)




