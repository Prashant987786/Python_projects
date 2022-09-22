
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

user_input = screen.textinput(title="Name", prompt="what is name you want to print on the console? :")
tim.hideturtle()
tim.penup()
tim.color("red")
tim.write(arg=user_input, move=True, align="center", font=["", 30, "bold"])
screen.exitonclick()
