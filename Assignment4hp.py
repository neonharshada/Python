# 1) write a function to accept a number and return its square using
# 	a) normal function
def fun():
    a=int(input("Enter a number:"))
    return a*a
hp=fun()
print(hp)
# 	b) lambda
a=int(input("Enter a number:"))
(lambda x: print(x*x))(a)



#
# 2) write a function to display "Hello World" using
# 	a) normal function
def fun():
    print("hello World")
fun()
# 	b) lambda
(lambda :print("hello World"))()
#
# 3) write a function with 2 arguments , second argument should be "default argument" and display them. Using
# 	a) normal function
def fun(var1, var2=10):
    print(var1, "\t", var2)
def disp():
    fun(10)
    fun(100, 200)
    fun(300, )
disp()

# 	b) lambda
(lambda a,b=20:print(a,b))(12)
#
# 4) write a function with variable no. of arguments and display them. Using
# 	a) normal function
def fun(*var):
    print(var)
fun(10, 20, 4, True)

# 	b) lambda
(lambda *var:print(var))(10,27,34,45,0,True,'a')
