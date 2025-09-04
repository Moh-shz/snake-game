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
        self.p_food = 0
        self.refresh()
        self.color('blue')

    def refresh(self):
        self.p_food = (random.randint(-280, 280), random.randint(-280, 250))
        self.goto(self.p_food)
