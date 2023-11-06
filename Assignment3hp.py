#  create 3 functions "show1()","show2()" and "show3()"
# now define a function "caller" in such a way that it can accept any function as an argument and invoke the same.
#
# invoke caller function by passing show1,show2 and show3
def show1():
     print("show1")
def show2():
     print("show2")
def show3():
     print("show3")
def caller(harsha):
     if callable(harsha):
          harsha()
     else:
          print("its not callable")
caller(show1)
caller(show2)
caller(show3)
caller(10)


# 2) define nested function and show how will you invoke it.

def mango():
    def seed():
        print("I am Mango seed")
    print("I am Mango")
    return seed
a=mango()
a()
#mango()()