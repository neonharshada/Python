# 8) Write a Python program to count number of items in a dictionary value that is a list
# sample data
# mydictionary1={'Names':['Rohit','Ganesh','SRK','Akshay'],'age':40,'addresses':['Mumbai','Delhi','Kolkara','Banglore'],
# 'emails':['actor.gmail.com','movie.gmail.com']}
# output: 10
mydictionary1={'Names':['Rohit','Ganesh','SRK','Akshay'],'age':40,'addresses':['Mumbai','Delhi','Kolkara','Banglore'],
               'emails':['actor.gmail.com','movie.gmail.com']}
count=0
for i in mydictionary1:
    if (type(mydictionary1[i])==list):
        count+=len(mydictionary1[i])
print(count)




