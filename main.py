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

hand = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

if user_choice < 0 or user_choice > 2:
    print("You typed an invalid number.")
else:
    print(hand[user_choice])
  
    ai_choice = random.randint(0, 2)
    print(f"Computer chose:\n{hand[ai_choice]}")
  
    if user_choice == 0 and ai_choice == 2:
        print("You win!")
    elif user_choice == 2 and ai_choice == 0:
        print("You lose!")
    elif user_choice == ai_choice:
        print("It's a tie!")
    elif user_choice > ai_choice:
        print("You win!")
    elif user_choice < ai_choice:
        print("You lose!")
