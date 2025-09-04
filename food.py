from turtle import Turtle
import random
from snake import Snake


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.penup()
        self.p_food = 0         # can delete? yes.
        self.refresh()
        self.color('blue')
        # self.eat = False

    def refresh(self):
        # food_snake = Turtle('circle')
        # food_snake.shapesize(0.5, 0.5)
        # food_snake.speed(6)
        # food_snake.penup()
        self.p_food = (random.randint(-280, 280), random.randint(-280, 250))
        # position_of_snake = []
        # for segment_of_snake in segments_of_snake:
        #     position_of_snake.append(segment_of_snake.position())
        # while self.p_food in position_of_snake:
        #     self.p_food = (random.randint(-280, 280), random.randint(-280, 280))
        self.goto(self.p_food)

    # def eat_food(self, segments_of_snake):
    #     if segments_of_snake[0].distance(self.p_food) < 15 :
    #         self.refresh(segments_of_snake)
    #         self.eat = True
    #         print("yessss")
    #         # insert_snake()
    #         # creat_food()

    # def insert_snake():
    #     new_snake = Turtle('square')
    #     new_snake.speed(6)
    #     new_snake.penup()
    #     last_part_snake = []
    #     last_part_snake.append(all_part_of_snake[len(all_part_of_snake) - 1].position())
    #     move_snake()
    #     new_snake.goto(last_part_snake[0])
    #     new_snake.color('white')
    #     all_part_of_snake.append(new_snake)
