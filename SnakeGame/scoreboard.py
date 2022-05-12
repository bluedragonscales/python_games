from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Copperplate", 16, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("green")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        """
        Puts the score on the screen.
        :return: str
        """
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        """
        Updates the score whenever the snake eats the food pellet.
        :return: str
        """
        self.score += 1
        self.clear()
        self.update_scoreboard()


    def game_over(self):
        """
        Shows the game over message when appropriate.
        :return: str
        """
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)