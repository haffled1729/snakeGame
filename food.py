### To handle the food turtle object with which the snake is supposed to collide to grow longer

from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)    # To scale down the size of the turtle
        self.color("red")
        self.speed("fastest")             # So that the repositioning of the food object is quickly done
        self.place_food()

    
    def place_food(self):
        random_x = randint(-260, 260)           
        random_y = randint(-260, 260)           #Since the borders are drawn at 270 pixels from the axes, food object has a buffer of 10
        self.goto(random_x, random_y)           #pixels to appear, within a 260 * 260 box