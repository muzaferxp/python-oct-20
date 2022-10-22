# Python program to draw square
# using Turtle Programming
#https://www.geeksforgeeks.org/turtle-programming-python/
#https://docs.python.org/3/library/turtle.html

import turtle
skk = turtle.Turtle()

for i in range(6):
	skk.forward(50)
	skk.right(360/6)
	
skk.forward(150)

for i in range(4):
	skk.forward(50)
	skk.right(90)
	
turtle.done()
