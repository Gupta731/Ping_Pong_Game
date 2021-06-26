from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 70, 'normal')
FONT2 = ('Courier', 40, 'normal')


class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color('bisque3')
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.update_score()

    def update_score(self):
        """Writes the new score everytime"""
        self.clear()
        self.write(f'{self.score}', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """increases score of the player by 1"""
        self.score += 1
        self.update_score()

    def game_over(self):
        self.clear()
        self.write(f'Wins', align=ALIGNMENT, font=FONT2)
