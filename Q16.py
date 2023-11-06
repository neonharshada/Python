# 16) Write a Python program to remove spaces from dictionary keys.
# Students={'d 01':'Abc','d 0 2':'Xyz','d0 3':'Pqr'}
# output:
# {'d01': 'Abc', 'd02': 'Xyz', 'd03': 'Pqr'}
Students={'d 01':'Abc','d 0 2':'Xyz','d0 3':'Pqr'}
new_Students={key.replace(" ",""):value for key ,value in Students.items()}
print(new_Students)