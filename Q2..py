# 2) create dictionary to store player name and runs scored of at least 5 players.
# Display it. Now convert this dictionary into Series object and print it.
import pandas as pd

Player={}

for i in range(0,5):
    player_name=input(f"Enter the player name{i +1}:")
    runs=int(input(f"Enter the {player_name} runs:"))
    Player.update({player_name:runs})
print("Players",Player)

harsha=pd.Series(Player)
print(harsha)
