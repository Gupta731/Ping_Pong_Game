from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Score
from board import Board
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('My Pong Game')
screen.tracer(0)

board = Board()
r_paddle = Paddle((350, 0), 'DarkOrange')
l_paddle = Paddle((-350, 0), 'RoyalBlue1')
ball = Ball()
l_score = Score((-80, 200))
r_score = Score((80, 200))

screen.listen()
screen.onkeypress(fun=r_paddle.up, key='Up')
screen.onkeypress(fun=r_paddle.down, key='Down')
screen.onkeypress(fun=l_paddle.up, key='w')
screen.onkeypress(fun=l_paddle.down, key='s')


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect ball misses the r_paddle
    if ball.xcor() > 400:
        l_score.increase_score()
        ball.reset_position()

    # detect ball misses the l_paddle
    if ball.xcor() < -400:
        r_score.increase_score()
        ball.reset_position()

    # detect when games finishes
    if l_score.score == 5:
        game_is_on = False
        l_score.game_over()
    elif r_score.score == 5:
        game_is_on = False
        r_score.game_over()

screen.exitonclick()
