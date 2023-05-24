from turtle import Screen, Turtle
import time
from random import randint

s=Turtle()
screen=Screen()
screen.setup(width=1000,height=700)
screen.bgcolor("lightgreen")
screen.bgpic("background.gif")
s.penup()
s.hideturtle()
s.goto(x=-170, y=100)
while True:
    your_color=screen.textinput("Color","Hello, what color do you want your car to be?")
    colors=["red","orange","yellow","green","blue","purple"]
    if your_color.lower() not in colors:
        s.write("Wrong color, try again",font=("Courier", 20, "bold"))
        time.sleep(1)
        screen.clear()
        screen.bgcolor("lightgreen")
        screen.bgpic("background.gif")
    else:
        break
colors=["red","orange","yellow","green","blue","purple"]
jimmy=Turtle(shape="turtle")
jimmy.penup()
jimmy.color(your_color)
jimmy.goto(-450,-140)
colors.remove(your_color)
x1=-450
y1=-90
list_of_turtles=["a","b","c","d","e"]
for i in range(len(colors)):
    list_of_turtles[i]=Turtle(shape="turtle")
    list_of_turtles[i].color(colors[i])
    list_of_turtles[i].penup()
    list_of_turtles[i].goto(x=x1,y=y1)
    y1=y1+50

s.goto(x=-120,y=316)
for i in range(1,4):
    s.write(f"{4-i}...",font=("Courier", 20, "bold"))
    time.sleep(1)
    s.forward(70)
s.write("Go !!!", font=("Courier", 20, "bold"))
def go():
    jimmy.forward(5)
screen.onkey(key="space",fun=go)
screen.listen()
z=0
while True:
    for i in list_of_turtles:
        i.forward(randint(1,6))
        if i.xcor()>=480 or jimmy.xcor()>=480:
            z=z+1
            break
    if z==1:
        break

jimmy.hideturtle()
for j in list_of_turtles:
    j.hideturtle()

s.goto(-90,0)
if jimmy.xcor()>=480:
    s.write("You win !!!",font=("Courier", 20, "bold"))
else:
    s.write("You lose...",font=("Courier", 20, "bold"))



screen.exitonclick()