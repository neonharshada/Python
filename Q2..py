# 2) create a Bar plot to show how many people like "Action","Romance","Comedy" or "Drama" movies.
from matplotlib import pyplot as py

movies=["Action","Romannce","Comedy","Drama"]
likes=[40,50,60,70]

py.bar(movies,likes,color='blue')
py.xlabel('Movies')
py.ylabel('likes')
py.title('Movies vs Likes')
py.show()