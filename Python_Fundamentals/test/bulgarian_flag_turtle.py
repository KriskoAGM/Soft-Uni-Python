# first time using turtle, Bulgarian flag draw test
import turtle

draw = turtle.Turtle()
draw.speed("normal")
draw.color("green")

draw.penup()
draw.left(90)
draw.forward(120)
draw.pendown()

draw.begin_fill()
draw.left(90)
draw.forward(380)
draw.backward(756)
draw.left(90)
draw.forward(230)
draw.right(90)
draw.forward(756)
draw.right(90)
draw.forward(230)
draw.end_fill()

draw.color("red")

draw.penup()
draw.backward(230)
draw.pendown()

draw.begin_fill()
draw.right(180)
draw.forward(205)
draw.right(90)
draw.backward(756)
draw.right(90)
draw.forward(205)
draw.left(90)
draw.forward(756)
draw.end_fill()

turtle.done()
