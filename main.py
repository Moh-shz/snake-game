from turtle import Screen, exitonclick
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Welcome to Snake Game")
screen.tracer(0)

snake = Snake()


def screen_listen():
    screen.listen()
    screen.onkey(snake.up, 'w')
    screen.onkey(snake.down, 's')
    screen.onkey(snake.left, 'a')
    screen.onkey(snake.right, 'd')


screen_listen()

food = Food()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # food.creat_food(snake.segments)

    # Detect collision with food
    if snake.head.distance(food) < 15:
        snake.extend_snake()
        scoreboard.increase_score()
        food.refresh()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280:
        snake.head.goto(-snake.head.xcor(), snake.head.ycor())
    if snake.head.ycor() > 260:
        snake.head.goto(snake.head.xcor(), -280)
    if snake.head.ycor() < -280:
        snake.head.goto(snake.head.xcor(), 260)

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            if screen.textinput(title='GAME OVER', prompt='Play again? yes or no').lower() == 'yes':
                scoreboard.reset()
                snake.reset()
                screen_listen()
            else:
                scoreboard.reset()
                game_is_on = False

exitonclick()
