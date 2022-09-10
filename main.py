import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
user_bet.lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
x = -230
y = -90
all_turtles = []

for turtle_index in range(0, 6):
    color = colors[turtle_index]
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x, y)
    y += 30
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"Sorry. You've lost. The {winning_color} turtle won. Better luck next time!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
