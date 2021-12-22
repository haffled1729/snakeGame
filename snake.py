### To handle drawing of the actual snake, positioning and extension of its length along with control of movements

from turtle import Turtle, position


POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE = 20  # Since the length of each turtle square is 20px

class Snake: 
    def __init__(self) -> None:
        self.body = []
        self.create_snake()
        self.head = self.body[0]
        
    def create_snake(self):
        for i in POSITIONS:
            self.add_part(i)
    
    def add_part(self, position):       # The snake is a list of 3 turtle objects initially, places next to each other
        sss = Turtle()
        sss.penup()
        sss.shape("square")
        sss.color("white")
        sss.setposition(position)
        self.body.append(sss)

    def move(self):                 # Each turtle object goes to the geometric position of the preceding object to achieve smooth movement
        for i in range(len(self.body) - 1, 0 , -1):  
            new = self.body[i-1].position()
            self.body[i].setposition(new)
        self.body[0].forward(MOVE)  # The first object has to move on its own, since it has no predecessor

    #Take 0 degree for facing right, 90 for up, 180 for left and 270 for down
    def ups(self):
        if self.head.heading() != 270:   #So that the snake doesn't move backwards
            self.head.setheading(90)
    
    def lefts(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def rights(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
    
    def downs(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    
    def grow(self):                             # A new turtle object is appended to the list and is placed at the position of the last
        self.add_part(self.body[-1].position())  # object to simulate a growing snake
    
    def kill(self):
        for i in self.body:
            i.hideturtle()