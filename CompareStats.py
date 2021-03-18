from playerstats import allstars_2021

print("                  Hello, and Welcome to the Stat Comparison Program Created by Michael Morriss")
print(" ")
print("In this program, you will be able to compare the stats from the 2021 NBA Players that were "
      "selected to be apart of the 2021 NBA All Star Game. ")
print("The current features allow you to either view individual player stats, or compare the stats of two different players.")
print(" ")
print("If you would like to view an individual player's stats, then type in 'View'.")
print("If you would like to compare the stats of two players, then type in 'Compare'.")

comp_type = str(input("Would you like to 'View' or 'Compare'?: "))
print(" ")

if comp_type == 'yes':
      for i in allstars_2021:
            print(i[0])

if comp_type.lower() == 'view':
      print("Please enter the name of the player whose stats you want to view.")
      print("If you would like to see the full list of player names, then type in 'Player list'.")
      print(" ")
      view_player = str(input("Enter the name of a player to view their stats: "))

      if view_player.lower() == 'list':
            for i in allstars_2021:
                  print(i[0])
      num_len = range(0, len(allstars_2021))
      for num in num_len:
            if view_player.lower() in allstars_2021[num][0].lower():
                  print(allstars_2021[num][0] + ":")
                  print("PPG:", allstars_2021[num][1])
                  print("RPG:", allstars_2021[num][2])
                  print("APG:", allstars_2021[num][3])
                  print("BPG:", allstars_2021[num][4])
                  print("SPG:", allstars_2021[num][5])
                  print("FG%:", allstars_2021[num][6])
                  print("3P%:", allstars_2021[num][7])
                  print("TOV:", allstars_2021[num][8])
                  print("MPG:", allstars_2021[num][9])
                  print("Awards:", allstars_2021[num][10])