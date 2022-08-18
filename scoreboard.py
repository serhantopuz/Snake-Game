from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        # reading high score from .txt file for still getting the high score after closing game
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.hideturtle()
        self.color("white")
        self.sety(270)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", False, "center", ('Courier', 22, 'normal'))

    def reset_scoreboard(self):
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
            # updating the high score
            with open("data.txt", mode="w") as set_high:
                set_high.write(f"{self.high_score}")
        self.score = 0
        self.write_score()


    def increase_score(self):
        self.score += 1
