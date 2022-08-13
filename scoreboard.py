from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.sety(270)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, "center", ('Courier', 22, 'normal'))
        self.score += 1

    def game_over(self):
        self.sety(0)
        self.write("GAME OVER", False, "center", ('Courier', 40, 'normal'))
