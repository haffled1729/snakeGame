### To handle the the borders, scorecard and the final "gameover" display using a turtle object

from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 10, 'normal')

class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.score = 0
        with open("highscore.txt", "r") as hs:
            self.highScore = int(hs.read())
        self.pencolor("white")
        self.write_score()

    def write_score(self):
        self.clear()
        self.borders()
        self.goto(-240, 280)
        self.pendown()
        self.write(f"Score: {self.score}", align="left", font=FONT)
        self.penup()
        self.goto(240, 280)
        self.pendown()
        self.write(f"High Score: {self.highScore}", align="right", font=FONT)
        self.penup()
    
    # Draw the border walls
    def borders(self):
        self.penup()
        self.goto(-270, 270)
        self.pendown()
        self.forward(540)
        self.right(90)
        self.forward(540)
        self.right(90)
        self.forward(540)
        self.right(90)
        self.forward(540)
        self.right(90)
        self.penup()

    # Print Game Over in the middle of the screen
    def gameover(self):
        self.goto(0,0)
        self.pendown()
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        self.penup()
        if self.score > self.highScore:
            self.highScore = self.score
            with open("highscore.txt", "w") as hs:
                hs.write(str(self.highScore))
        self.score = 0
    
    # Increment score and redraw the game outline
    def scored(self):
        self.score += 1
        self.write_score()