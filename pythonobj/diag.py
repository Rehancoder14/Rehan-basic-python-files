import turtle 
col = ('red', 'yellow', 'green', 'cyan','pink', 'white')
t= turtle.Turtle()
A= turtle.Screen()
A.bgcolor('black')
t.speed(25)
for i in range(150):
    t.color(col[i%4])
    t.forward(i*1)
    t.left(40)
    t.width(5)
    