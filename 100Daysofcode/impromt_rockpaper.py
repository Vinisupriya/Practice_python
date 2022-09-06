import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game= int(input("What do you choose? Type 0 for rock,1 for paper and 2 for scissors"))
            
if game == 0:
    print(rock)
if game == 1:
    print(paper)
if game == 2:
    print(scissors)
print("Computer choose:")
    
computer = random.randint(0,2)

if computer == 0:
    print(rock)
if computer == 1:
    print(paper)
if computer == 2:
    print(scissors)

if game == computer:
    print("Draw")
elif game == 0 and computer == 2:
    print("you win")
elif game == 0 and computer == 1:
    print("you lose")
elif game == 1 and computer == 0:
    print("you lose")
elif game == 1 and computer == 2:
    print("you lose")
elif game == 2 and computer == 0:
    print("you lose")
elif game == 2 and computer == 1:
    print("you win")


