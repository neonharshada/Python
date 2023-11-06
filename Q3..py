# 3) create a piechart to show popularity of various modules (Java,Python etc.)
import matplotlib.pyplot as py

module=['Java','Python','R-programming','Bash']
Popularity=[20,15,25,40]

py.pie(Popularity,labels=module,autopct='%0.1f%%',colors=['red','blue','green','yellow'])

py.legend(bbox_to_anchor=(0.9,0.9),title='legend')
py.title("Modules Popolarity")
py.show()
