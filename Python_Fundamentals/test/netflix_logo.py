import turtle

# NETFLIX LOGO

draw = turtle.Turtle(visible=False)  # hiding the pointer
turtle.bgcolor("black")
draw.speed(6)

# Setting up starting point
draw.penup()
draw.left(90)
draw.forward(120)
draw.left(90)
draw.forward(100)
draw.left(90)
draw.pendown()

draw.fillcolor("#7a1a1a")

# Drawing and filling the first line with color
draw.begin_fill()
for i in range(2):
    draw.forward(200)
    draw.left(90)
    draw.forward(30)
    draw.left(90)
draw.end_fill()

# Setting up position for second line
draw.penup()
draw.left(90)
draw.forward(80)
draw.right(90)
draw.pendown()

# Drawing and filling the second line with color
draw.begin_fill()
for i in range(2):
    draw.forward(200)
    draw.left(90)
    draw.forward(30)
    draw.left(90)
draw.end_fill()

# Setting up position for third diagonal line
draw.penup()
draw.right(90)
draw.forward(80)
draw.left(90)
draw.left(22)
draw.pendown()

draw.fillcolor("red")

# Drawing and connecting the diagonal line with the other two lines
draw.begin_fill()
for i in range(2):
    draw.forward(217)
    draw.left(68)
    draw.forward(30)
    draw.left(112)
draw.end_fill()

turtle.done()
