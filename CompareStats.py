from playerstats import allstars_2021, instruction_list
from operator import itemgetter


def instructions():
    print(" ")
    comp = str(input("Would you like to 'View' or 'Compare' or see the 'List' of players?: "))
    print(" ")
    return comp


def sort_points(a_list):
      """Sorts in descending order."""
      for index in range(1, len(a_list)):
            value = a_list[index][1]
            pos = index - 1
            while pos >= 0 and a_list[pos][1] < value:
                  a_list[pos + 1] = a_list[pos]
                  pos -= 1
            a_list[pos + 1] = value


print("Welcome to the NBA All Star Stat Comparison Program")
print("Programmed by Michael Morriss")
print(" ")
print("In this program, you will be able to compare the stats from the 2021 NBA Players that were "
      "selected to be apart of the 2021 NBA All Star Game. ")
print("The current features allow you to either view individual player stats, or compare the stats of "
      "two different players.")

print("If you would like to view an individual player's stats, then type in 'View'.")
print("If you would like to compare the stats of two players, then type in 'Compare'.")
print("If you would like to see the full list of player names, then type in 'List'.")
print("If you would like to see the full list of usable instructions, then type 'Instructions'.")

while True:
      comp_type = instructions()

      if comp_type.lower() == 'instructions':
            for i in instruction_list:
                  print(i)

      if comp_type.lower() == 'sort points':
            allstars_2021.sort(key = itemgetter(1), reverse = True)
            for i in allstars_2021:
                  print(i[0] + ":", i[1], "PPG")
      if comp_type.lower() == 'sort rebounds':
            allstars_2021.sort(key = itemgetter(2), reverse = True)
            for i in allstars_2021:
                  print(i[0] + ":", i[2], "RPG")
      if comp_type.lower() == 'sort assists':
            allstars_2021.sort(key = itemgetter(3), reverse = True)
            for i in allstars_2021:
                  print(i[0] + ":", i[3], "APG")
      if comp_type.lower() == 'sort blocks':
            allstars_2021.sort(key = itemgetter(4), reverse = True)
            for i in allstars_2021:
                  print(i[0] + ":", i[4], "BPG")
      if comp_type.lower() == 'sort steals':
            allstars_2021.sort(key = itemgetter(5), reverse = True)
            for i in allstars_2021:
                  print(i[0] + ":", i[5], "SPG")
      if comp_type.lower() == 'sort fg%':
            allstars_2021.sort(key = itemgetter(6), reverse = True)
            for i in allstars_2021:
                  print(i[0] + ":", i[6], "FG%")
      if comp_type.lower() == 'sort 3pt%':
            allstars_2021.sort(key = itemgetter(7), reverse = True)
            for i in allstars_2021:
                  print(i[0] + ":", i[7], "3PT%")
      if comp_type.lower() == 'sort tov':
            allstars_2021.sort(key = itemgetter(8), reverse = True)
            for i in allstars_2021:
                  print(i[0] + ":", i[8], "TOV")
      if comp_type.lower() == 'sort minutes':
            allstars_2021.sort(key = itemgetter(9), reverse = True)
            for i in allstars_2021:
                  print(i[0] + ":", i[9], "MPG")

      if comp_type.lower() == 'list':
            for i in allstars_2021:
                  print(i[0])

      num_len = range(0, len(allstars_2021))

      if comp_type.lower() == 'awards':
            play_award = str(input("Enter the player name you would like to view awards for: "))
            print(" ")
            for i in num_len:
                  if play_award.lower() in allstars_2021[i][0].lower():
                        print(allstars_2021[i][0] + "'s", "Awards: ")
                        print(allstars_2021[i][10])

      if comp_type.lower() == 'compare':
            comp_p1 = str(input("Please enter the name of the first player you want to compare: "))
            comp_p2 = str(input("Please enter the name of the second player you want to compare: "))
            print(" ")
            for num in num_len:
                  if comp_p1.lower() in allstars_2021[num][0].lower():
                        print(allstars_2021[num][0] + ":", allstars_2021[num][1], "PPG,",
                              allstars_2021[num][2], "RPG,",allstars_2021[num][3], "APG,",
                              allstars_2021[num][4], "BPG,", allstars_2021[num][5], "SPG,",
                              allstars_2021[num][6], "FG%,", allstars_2021[num][7], "3PT%,",
                              allstars_2021[num][8], "TOV,", allstars_2021[num][9], "MPG")
                  if comp_p2.lower() in allstars_2021[num][0].lower():
                        print(allstars_2021[num][0] + ":", allstars_2021[num][1], "PPG,",
                              allstars_2021[num][2], "RPG,",allstars_2021[num][3], "APG,",
                              allstars_2021[num][4], "BPG,", allstars_2021[num][5], "SPG,",
                              allstars_2021[num][6], "FG%,", allstars_2021[num][7], "3PT%,",
                              allstars_2021[num][8], "TOV,", allstars_2021[num][9], "MPG")

            print(" ")

            for num in num_len:
                  if comp_p1.lower() in allstars_2021[num][0].lower():
                        print(allstars_2021[num][0] + "'s Awards:", allstars_2021[num][10])
                  if comp_p2.lower() in allstars_2021[num][0].lower():
                        print(allstars_2021[num][0] + "'s Awards:", allstars_2021[num][10])




      if comp_type.lower() == 'view':
            view_player = str(input("Enter the name of a player to view their stats: "))
            print("")
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
                        print("")