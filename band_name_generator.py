# The band name generator puts together your hometown and pet name to make your new band name.
from ASCII_art import guitar

print(guitar)
print("Welcome to the Band Name Generator.")

city = input("What's the name of the city you grew up in?\n")
pet = input("What's the name of your pet?\n")

band_name = city + " " + pet
print("Your new band name: " + band_name)