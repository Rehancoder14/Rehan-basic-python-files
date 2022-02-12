import turtle 
turtle.pensize(2)
turtle.speed(15)
turtle.bgcolor("black")
for i in range(10):
    for colours in ["#00adef", "blue","cyan","#00adef","blue","cyan"]:
        turtle.color(colours)
        turtle.circle(100)
        turtle.left(10)
turtle.hideturtle()