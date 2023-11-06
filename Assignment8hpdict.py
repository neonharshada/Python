# 1) accept 5 students name and store them in the dictionary by providing keys from 1 to 5 respectively.
mydict = {}
for i in range(1, 6):
    student_name = input(f"Enter the nae of student{i}:")
    mydict[i] = student_name
print("Student name directory:", mydict)


# 2) create a dictionary with pairs
# 	soap:100
# 	deo:300
# 	perfume:400

# now accept a product name from user (in any case, so you have to handle "ignore case") and display its price. Also , if the product is not present in the dictionary display the error message " product not available "
# 	Note:  you should not get "KeyError:" in the program.
mydict={'soap':100,'deo':300,'perfume':400}
print("Mydict",mydict)
product_name=input("Enter product name:").lower() #ignore case
if product_name in mydict:
    prize=mydict[product_name]
    print(f"Prize of {product_name} is {prize}")
else:
    print("Product not available")

