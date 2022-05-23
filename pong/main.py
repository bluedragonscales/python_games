import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# The creation of the game screen.
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)
screen.listen()


# The objects needed for the game: the left and right paddles, the ball, and the scoreboard.
paddle_right = Paddle(360)
paddle_left = Paddle(-360)
pong_ball = Ball()
scoreboard = Scoreboard()

# The right paddle controls.
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")

# The left paddle controls.
screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")


# While the game is on, keep the game going.
game_is_on = True
while game_is_on:
    time.sleep(pong_ball.move_speed)
    screen.update()
    pong_ball.move()

    # If the ball hits the top or the bottom of the screen, it will bounce with the bounce method created in the
    # Ball class.
    if pong_ball.ycor() > 280 or pong_ball.ycor() < -275:
        pong_ball.bounce()

    # If the ball hits the right paddle, it will be deflected with the deflect method from the Ball class. The ball will
    # also increase in speed.
    if pong_ball.distance(paddle_right) < 50 and pong_ball.xcor() > 330:
        pong_ball.deflect()

    # If the ball hits the left paddle, it will be deflected with the deflect method from the Ball class. The ball will
    # also increase in speed.
    if pong_ball.distance(paddle_left) < 50 and pong_ball.xcor() < -330:
        pong_ball.deflect()

    # If the ball hits the right side of the screen because the right paddle missed it, the left player score will be
    # increased by one and the ball will revert back to the center of the screen.
    if pong_ball.xcor() > 380:
        pong_ball.reset_position()
        scoreboard.l_point()

    # If the ball hits the left side of the screen because the left paddle missed it, the right player score will be
    # increased by one and the ball will revert back to the center of the screen.
    if pong_ball.xcor() < -380:
        pong_ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()