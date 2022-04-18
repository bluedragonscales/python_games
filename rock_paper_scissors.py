from ASCII_art import rock_paper_scissors
import random

print("Welcome to the rock, paper, scissors game!")

# Store the user's choice of 0, 1, or 2 as an int instead of a string.
person_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

# Put the three choices into a list.
choices = [rock_paper_scissors['rock'], rock_paper_scissors['paper'], rock_paper_scissors['scissors']]

# Store the computer's random number.
comp_choice = random.randint(0, 2)


if person_choice > 2 or person_choice < 0:
  print("You chose an incorrect number. You lose!")
else:
  print(f"You chose\n {choices[person_choice]}")
  print(f"The computer chose {choices[comp_choice]}")

  if person_choice == comp_choice:
    print("It's a tie!")
  elif person_choice == 0 and comp_choice == 2:
    print("You win!")
  elif comp_choice == 0 and person_choice == 2:
    print("You lose!")
  elif comp_choice > person_choice:
    print("You lose!")
  elif person_choice > comp_choice:
    print("You win!")

