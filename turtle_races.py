import random
from turtle import Turtle, Screen

# This is a turtle racing game. The rainbow colored turtles are moved forward by the program. You get to move the black
# turtle on your own. You might just win if press the space key fast enough!


# Screen and on/off switch set up.
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

# Make a bet on which of the program turtles will win. You cannot bet on yourself!
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Pick red, orange, yellow,"
                                                          "green, blue, purple, or black.")


# Setting up the program turtles in the colors of the rainbow.
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = -100
all_turtles = []
for color in range(len(colors)):
    racer = Turtle(shape="turtle")
    racer.color(colors[color])
    racer.penup()
    racer.goto(x=-230, y=y_pos)
    all_turtles.append(racer)
    y_pos += 30


# Setting up the turtle you can control in the color black.
    user_turtle = Turtle(shape="turtle")
    user_turtle.color("black")
    user_turtle.penup()
    screen.listen()
    user_turtle.goto(x=-230, y=100)
    def move_forward():
        user_turtle.forward(rand_distance)
    screen.onkey(key="space", fun=move_forward)


# Once you've made a bet, the race can begin.
if user_bet:
    is_race_on = True


# The race is on! Who will win?
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()