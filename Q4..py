# 4) accept 5 values in a Series and perform the following operations:
# 	a) display their sum
# 	b) add the value accepted from the user
# 	c) subtract the value accepted from the user
# 	d) multiply the value accepted from the user
# 	e) add the value accepted from the user
import pandas as pd

Values=[]

for i in range(0,5):
    value=int(input(f"Enter a number{i +1}:"))
    Values.append(value)

series=pd.Series(Values)
print("Original Series:",series)

sum_series=sum(series)
print("sum of series",sum_series)

a=int(input("Enter a number:"))

add_value=series + a
print("add a to the series",add_value)

sub_value=series - a
print("sub a from the series",sub_value)

mul_value=series * a
print("Multiplication of ato series",mul_value)

div_value=series / a
print("division of series",div_value)




