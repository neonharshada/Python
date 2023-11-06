# 14) # Write a Python program to print a dictionary line by line.
# Players={'Rohit':{'runs':10000,'centuries':15},'Virat':{'runs':12000,'centuries':18}}
# expected output:
# Rohit
# runs :	 10000
# centuries :	 15
# Virat
# runs :	 12000
# centuries :	 18
Players={'Rohit':{'runs':10000,'centuries':15},'Virat':{'runs':12000,'centuries':18}}

for player,data in Players.items():
    print(player)
    # for i in data:
    #     print(i,":",data[i])
    for i,j in data.items():
        print(f"{i}:{j}")



