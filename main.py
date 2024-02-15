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
user_choise = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
game_images = [rock, paper, scissors]
print(game_images[user_choise])

import random
computer_choise = random.randint(0,2)
print("Computer chose:")
print(game_images[computer_choise])

if(user_choise == computer_choise):
  print("Draw")
elif(user_choise == 0 and computer_choise == 1):
  print("You lose")
elif(user_choise == 0 and computer_choise == 2):
  print("You win")
elif(user_choise == 1 and computer_choise == 0):
  print("You win")
elif(user_choise == 1 and computer_choise == 2):
  print("You lose")
elif(user_choise == 2 and computer_choise == 0):
  print("You lose")
elif user_choise == 2 and computer_choise == 1:
  print("You win")
else:
  print("You entered an invalid number. You lose!")