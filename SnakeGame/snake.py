from turtle import Turtle


MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]


    def create_snake(self):
        """
        Creates the initial snake in three turtle segments.
        :return: turtle object
        """
        x_pos = 0
        for _ in range(3):
            self.add_segment(x_pos)
            x_pos -= 20


    def add_segment(self, x_pos):
        """
        Creates a new segment and adds it to the other segments when appropriate.
        :param x_pos: int
        :return: turtle object
        """
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(x_pos, 0)
        self.snake_segments.append(snake)


    def extend(self):
        """
        Puts the newly earned snake segment onto the back of the snake tail.
        :return: turtle object
        """
        self.add_segment(self.snake_segments[-1].xcor())


    def move(self):
        """
        Moves the snake forward and all its segments in unison.
        :return: turtle object
        """
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg_num - 1].xcor()
            new_y = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)



    # These are the methods to control the snake's head.
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)