from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position, colour):
        super().__init__('square')
        self.color(colour)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        """Makes the paddle go upwards"""
        if self.ycor() < 250:
            new_y = self.ycor() + 25
            self.goto(self.xcor(), new_y)

    def down(self):
        """Makes the paddle go downwards"""
        if self.ycor() > -250:
            new_y = self.ycor() - 25
            self.goto(self.xcor(), new_y)
