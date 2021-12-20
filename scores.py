### To handle the the borders, scorecard and the final "gameover" display using a turtle object

from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 10, 'normal')

class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.pencolor("white")
        self.borders()
        self.goto(0, 280)
        self.pendown()
        self.score = 0
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

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
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    
    # Increment score and redraw the game outline
    def scored(self):
        self.score += 1
        self.clear()
        self.borders()
        self.goto(0, 280)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)