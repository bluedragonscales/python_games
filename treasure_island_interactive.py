from ASCII_art import treasure_island

# This game is a set of if/elif/else statements to lead a user, based on their choices, to an alternate ending.

# ASCII art for the opening.
print(treasure_island)

# Starts the story.
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("Pirates have captured your friend. It's time to rescue them. Now you have to search for the island they left them tied up on.\nYou're on a canoe floating down a river in the middle of a jungle.")
direction = input("You've paddled to a fork in the river. Do you go 'left' or 'right'?\n").lower()


# If the user chooses the wrong answers, they are doomed. If they choose the right answer, they are able to rescue their
# friend and escape safely.
if direction == "left":
  print("The fork you chose leads you to the beach. In the distance is an island.")
  print("Your canoe springs a leak and topples but you are able to dog paddle to the beach.")
  decision = input("Do you 'swim' to the island or do you 'fix' the canoe first?\n").lower()
  if decision == "fix":
    print("You've fixed the canoe and paddled to the island safely.")
    print("Your friend is inside a hut, behind one of three doors.")
    door = input("Which door do you choose? 'Red', 'green', or 'blue'?\n").lower()
    if door == "blue":
      print("You've untied your friend and paddle back to the mainland safely. You win!")
    elif door == "red":
      print("Here there be pirates. Game over.")
    else:
      print("You fall into a deadly booby trap. Game over.")
  else:
    print("You were attacked by a shark after swimming five yards from shore. Game over.")
else:
  print("You paddled straight to a waterfall and fell off. Game over.")