from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 15, 'normal')
FONT_GAME_OVER = ('Courier', 35, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 280)
        self.high_score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score {self.score}. High Score {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", False, align=ALIGNMENT, font=FONT_GAME_OVER)

    def increase_score(self):
        self.score = self.score + 1
        self.update_scoreboard()
