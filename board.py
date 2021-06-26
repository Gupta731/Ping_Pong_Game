from turtle import Turtle


class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.color('green3')
        self.hideturtle()
        self.penup()
        self.pensize(3)
        self.make_board()

    def make_board(self):
        """Makes dashed borders around the screen"""
        self.setpos(-380, -288)
        self.horizontal_line()
        self.setpos(-380, 295)
        self.horizontal_line()
        self.setheading(90)
        self.setpos(-395, -280)
        self.vertical_line()
        self.setpos(0, -280)
        self.vertical_line()
        self.setpos(388, -280)
        self.vertical_line()

    def dashed_line(self):
        """Makes dashed line"""
        self.pendown()
        self.forward(15)
        self.penup()
        self.forward(20)

    def horizontal_line(self):
        """Makes horizontal dashed line"""
        for i in range(22):
            self.dashed_line()

    def vertical_line(self):
        """makes vertical dashed line"""
        for i in range(17):
            self.dashed_line()
