#!/usr/bin/python3
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

#Write your code below this line 👇
images = [rock, paper, scissors]

you = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors\n"))
if you >= 3 or you < 0:
    print("You typed and invalid number, you lose!")
else:
    print(images[you])
    
    computer = random.randint(0, 2)
    print("Computer Choose: {}".format(computer))
    print(images[computer])
    
    if you == computer:
        print("It's a tie! Try again")
    elif you == 0 and computer == 2:
        print("You win!")
    elif you == 1 and computer == 0:
        print("You win!")
    elif you == 2 and computer == 1:
        print("You win!")
    else:
        print("You lose!")