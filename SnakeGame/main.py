import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


# Creating the game screen.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Eats")
screen.tracer(0)

# The instances for each the snake, food, and the score.
new_snake = Snake()
food = Food()
score = Scoreboard()


# To use the arrow keys to control the snake.
screen.listen()
screen.onkey(new_snake.up, "Up")
screen.onkey(new_snake.down, "Down")
screen.onkey(new_snake.left, "Left")
screen.onkey(new_snake.right, "Right")


# The game itself inside a while loops so that the game doesn't stop until it's game over.
game_is_on = True
while game_is_on:
    screen.update()
    # Slows the snake down long enough so that you can control it.
    time.sleep(0.1)
    # Snake continues to move so long as the game is playing.
    new_snake.move()

    # When the snake collides with the food, the snake extends by one segment and the food respawns somewhere else on
    # the screen.
    if new_snake.head.distance(food) < 15:
        food.refresh()
        new_snake.extend()
        score.increase_score()

    # If the snake's head runs into any side of the screen, the game is over.
    if new_snake.head.xcor() > 290 or new_snake.head.xcor() < -290 or new_snake.head.ycor() > 290 or new_snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()

    # If the snake's head runs into any part of its own body then the game is over.
    for segment in new_snake.snake_segments[1:]:
        if new_snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()




screen.exitonclick()