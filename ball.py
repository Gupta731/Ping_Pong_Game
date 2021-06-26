from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__('circle')
        self.color('firebrick2')
        self.penup()
        self.move_speed = 0.1
        self.x_move = 10
        self.y_move = 10

    def move(self):
        """Moves the ball across the screen"""
        self.goto(self.xcor()+self.x_move, self.ycor()+self.y_move)

    def bounce_y(self):
        """Bounces the ball when it hits the wall"""
        self.y_move *= -1

    def bounce_x(self):
        """Bounces the ball when it hits the paddles"""
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """Resets ball position when it goes off the screen"""
        self.home()
        self.move_speed = 0.1
        self.bounce_x()
