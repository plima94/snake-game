from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.high_score = 0
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game Over", align=ALIGNMENT, font=FONT)

