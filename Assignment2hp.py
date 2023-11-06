
# 1) define 3 functions "add()","modify()" and "delete()" with just a print message.
# now accept input from user as a number. if the number entered is 1, call "add()"
# if it is 2, call "modify()" if it is 3, call "delete()" [ hint: use "match... case" ]
def add():
    print("add value")
def modify():
    print("modify value")
def delete():
    print("delete value")
num = int(input("Enter a number"))
match num:
    case 1:
        add()
    case 2:
        modify()
    case 3:
        delete()

# 2) define a function which accepts a number and return its square.
def myfun():
    num = int(input("Enter a number:"))
    return num * num
a = myfun()
print(a)


# 3) define a function which accepts character,int,string and display them.
def disp():
    char=(input("Enter a character:"))[0]
    num=int(input("Enter a number:"))
    string=input("Enter a string:")
disp()
print("char")
print("num")
print("string")

# 4) define "myfun1()" with a print statement. now define "myfun2()" which should invoke "myfun1()" function.
 #invoke myfun2()

def myfun1():
    print("myfun1")
def myfun2():
    print("myfun2")
    myfun1()
myfun2()

# 5) define a function to accept a number. This function should return 1 if a number passed is more than 0
# return -1 if a number passed is less than 0 , else it should return 0.
def fun(num):
    if num>0:
        return 1
    elif num<1:
        return -1
    else :
        return 0
num = int(input("Enter a number:"))
a =fun(num)
print(a)

# 6) define a function which accepts a character and return toggle of it.
def toggle(ch):
    a=ord(ch)
    if a >= 65 and a <=90:
        a=a+32
        print(chr(a))
    else:
        a=a-32
        print(chr(a))
toggle('a')
toggle('A')

# 7) define a function which accepts a string , toggle and return it.
# 	[ hint :  use "swapcase()" function of string ]
def swapcase(ch):
    str1 = ch.swapcase()
    print(str1)

swapcase('Harshada')
swapcase('Patil')

# 8) write a function to accept minimum 3 characters and maximum 5 characters.
#  	# [ use default arguments method ]
def disp(*varg):
    if (varg.__len__()>=3 and varg.__len__()<=5):
        print(varg)
    else:
        print("invalid argument")
disp(1,2,3)
disp()
disp(1,2,3,4,5,6)
disp(0,1,True)

# 9) define a function in such a way that it can accept n number of values and print their sum. [ variable number of arguments]
def fun(*harsha):
    sum =0
    for i in harsha:
        sum += i
    print(sum)
fun(1,2,3,4,5,6,7)