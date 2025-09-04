from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")  # Courier


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        file = open('high_score.txt')
        self.high_score = int(file.read())
        file.close()
        self.goto(0, 260)
        self.pencolor("white")
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            file = open('high_score.txt', 'w')
            file.write(f'{self.high_score}')
            file.close()
            self.score = 0
            self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def play_again(self):
        pass
