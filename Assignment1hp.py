#1)	accept a number and display its table.
number = int(input("Enter the Number:"))
print(f"Multiplication table of {number}:")
for i in range (1,11):
    result = number*i
    print(f"{number} * {i}={result}")

 #2)	using switch ….case   display whether accepted character is vowel or not.\n"
char = input("Enter a character")
char = char.lower()  # Convert the character to lowercase to handle both uppercase and lowercase vowels
match char:
    case 'a', 'o', 'u', 'i', 'e':
        print(f"{char} is a Vowel")
    case _:
        print(f"{char} is not a vowel")

#3)	Display numbers  1 to 10 using  While loop
i=0
while(i<=10):
    print(i,end=" ")
    i+=1

#4)	Display numbers from 3 to 30 except number 24  using while loop.
i=3
while(i<=30):
    if(i==24):
        continue
    print(i,end=(" "))
    i+=1

#5)	accept marks from the user. Using if…….elif….  Else,  display whether result is  fail, pass, second class , first class, Distinction etc.
Marks = int(input("Enter the marks:"))
if(Marks>75 and Marks<90):
    print("Distingtion")
elif(Marks>60 and Marks<75):
    print("First class")
elif(Marks>45 and Marks<60):
    print("Second class")
elif(Marks>35 and Marks<45):
    print("pass")
else:
    print("fail")

#6) print the total of first 10 numbers.
result=0   # Initialize a variable to store the result
for i in range(1,11):
    result += i
print(f"Total of first 10 no: {result}")   #print outside for loop

#7) accept numbers till user enters 0 and display the total of all the numbers entered.
total =0  # Initialize a variable to store the total
while True:
    num = int(input("enter the number"))
    if num==0:
        break
    total += num
print("Total no of enter no:",total)

#8) accept a character and display whether it is upper case or lower case or not an alphabet.
char = input("enter the character:")
if char.isupper():
    print(f"{char} is Uppercase")
elif char.islower():
    print(f"{char}is Lowercase")
elif not char.isalpha():
    print(f"{char}is not a alphabet")
else:
    print(f"{char}is invalid")

#9) display fibonicii series of 10 numbers
a,b= 0,1
print(a, end=" ")
print(b, end=" ")
for _ in range(8):
   a,b=b,a+b;
   print(b,end=" ")


#10) display prime numbers from 3 to 30
for i in range(3, 31):
    for j in range(2,i//2):
        if i % j == 0:
            break
    else:
      print(i, end=" ")


#11) accept a number and display whether it is prime or not
num = int(input("Enter the Number:"))
for i in range(2,num//2):
    if(num%i ==0):
        print("Not a prime")
        break
else:
     print("Prime number")
"""
12) print the following pattern:
*
* *
* * *
* * * *
* * * * *
"""
n = int(input("Enter the number:"))
for i in range(0,n+1):
   for j in range(0,i+1):
      print("*",end=" ")
   print()
"""
13) print the following pattern:

* * * * * 

* * * * 

* * * 

* * 

* 
"""
a = int(input("Enter the number:"))
for i in range(0,a):
   for j in range(a,i,-1):
      print("*",end=" ")
   print()
"""
14) print the following pattern
		        *
	         *  *
          *  *  *
       *  *  *  *
    *  *  *  *  *
"""
n = int(input("Enter the Number:"))
for i in range(0,n):
   for s in range(i,n):
      print(" ",end=" ")
   for j in range(0,i):
      print("*",end=" ")
   print()





