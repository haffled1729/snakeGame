### The actual interface module that user interacts with

from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scores import Score

#Initial Setup
scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor("black")
scr.title("Classic Snake Game")
scr.tracer(0)   #Tracer off, need to manually update the screen. No animation until updated

#Building the Snake's Body

# tim.resizemode(rmode="user") 
# tim.shapesize(stretch_len=3) #Can't show flexible movements with this

snake = Snake()
food = Food()
score = Score()
game_on = True

scr.listen()
while game_on:
    scr.update()    # Animate the screen, update the changes like the snake movement
    sleep(0.06)     #Slow down the update, can control the game speed
    snake.move()
    scr.onkey(key="Up", fun=snake.ups)
    scr.onkey(key="Left", fun=snake.lefts)
    scr.onkey(key="Right", fun=snake.rights)
    scr.onkey(key="Down", fun=snake.downs)

    # Food Detection
    if  snake.head.distance(food) < 13:
        food.place_food()
        snake.grow()
        score.scored()
    
    # Wall Collision Detection
    if snake.head.xcor() >= 270 or snake.head.xcor() <= -270 or snake.head.ycor() >= 270 or snake.head.ycor() <= -270:
        score.gameover()
        game_on = False
    
    #Body Collision Detection
    for b in snake.body[1:]:
        if snake.head.distance(b) < 10:
            score.gameover()
            game_on = False

scr.exitonclick()   #Screen Closes on mouseclick