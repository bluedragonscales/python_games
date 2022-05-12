from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        # These come from the Turtle super class.
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """
        When called, this method makes a new food pellet reappear at a random coordinate on the game screen.
        :return: turtle object
        """
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
