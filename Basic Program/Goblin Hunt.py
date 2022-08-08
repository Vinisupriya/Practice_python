import random
print("Welcome to the Angry Goblin Hunt")
print("An award-winning game full of adventure and excitement (!)")

player_name = input("What is your name? ")
print(player_name + ", can you find the goblin?")
print("|_||_||_||_||_|")
goblin_position = random.randint(1,5)
keep_trying = True
while keep_trying :
    guessed_position = input("Can you guess where the goblin is hiding? ")
    guessed_position = int(guessed_position)
if guessed_position == goblin_position:
  print("Well done. You've found the goblin.")
  keep_trying = False
else:
  print("No, sorry. The goblin is still hiding somewhere.")

print ( " GO TO WORK")
