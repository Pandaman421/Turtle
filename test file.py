# TurtleTest
""" Turtle Examples """
import turtle
import math
from random import *
#since I noticed every single shape starts with this code I decided to just make it it's own function, a lot easier.
def startShape(turtl, startX, startY, rotation, colr, fillcolr):
    turtl.penup()
    turtl.goto(startX, startY)
    turtl.color(colr)
    if fillcolr:
        turtl.fillcolor(fillcolr)
        turtl.begin_fill()
    turtl.left(rotation)
    turtl.pendown()
    
def drawSquare(turtl, startX, startY, size, rotation=0, colr='black', fillcolr=''):
    startShape(turtl, startX, startY, rotation, colr, fillcolr)
    for i in range(4):
        turtl.forward(size)
        turtl.left(90)
    turtl.end_fill()
    turtl.right(rotation)
    turtl.penup()
        
def drawTriangle(turtl, startX, startY, size, rotation=0, colr='black', fillcolr=''):
    startShape(turtl, startX, startY, rotation, colr, fillcolr)
    for i in range(3):
        turtl.forward(int(size*2))
        turtl.left(120)
    turtl.end_fill()
    turtl.right(rotation)
    turtl.penup()
    
def drawRhombus(turtl, startX, startY, size, rotation=0, colr='black', fillcolr=''):
    startShape(turtl, startX, startY, rotation, colr, fillcolr)
    for i in range(2):
        turtl.forward(size)
        turtl.left(60)
        turtl.forward(size)
        turtl.left(120)
    turtl.right(rotation)
    turtl.end_fill()
    turtl.penup()

        
def drawCircle(turtl, startX, startY, size, rotation=0, colr='black', fillcolr=''):
    startShape(turtl, startX, startY, rotation, colr, fillcolr)
    turtl.circle(size)
    turtl.end_fill()
    turtl.right(rotation)
    turtl.penup()
    
    
    #so all this does is take existing coordinates, and spit out new ones based on the objects rotation.
def rotateCoords(x, y, rotation):
    
    if x == 0:
        if y == 0:
            return 0, 0
        elif y > 0 :
            angle = 90
        else:
            angle = 270
    
    elif x > 0:
        if y == 0:
            angle = 0
        elif y > 0:
            angle = math.degrees(math.atan(y/x))
        else:
            angle = math.degrees(math.atan(y/x))
    else:
        if y == 0:
            angle = 180
        if y > 0:
            angle = math.degrees(math.atan(y/x)) + 180
        else:
            angle = math.degrees(math.atan(y/x)) + 180
    angle = (angle + rotation) % 360
    radius = math.sqrt(x**2 + y**2)
    newX, newY = math.cos(math.radians(angle)) * radius, math.sin(math.radians(angle)) * radius
    return newX, newY

    #these two I just thought would be fun, I know I didn't actually need to make them...
def smileyFace(turtl, startX, startY, size, rotation=0, colr='black', fillcolr='yellow'):
    drawCircle(turtl, startX, startY, size, rotation, colr, fillcolr)
    x, y = rotateCoords(size*0.3, size*1.3, rotation)
    turtl.goto(startX+x, startY+y)
    turtl.dot((size*0.1), colr)
    x, y = rotateCoords(size*-0.3, size*1.3, rotation)
    turtl.goto(startX+x, startY+y)
    turtl.dot((size*0.1), colr)
    
    x, y = rotateCoords(size*-0.6, size, rotation)
    turtl.goto(startX+x, startY+y)
    turtl.pendown()
    turtl.color(colr)
    turtl.setheading(rotation)
    turtl.right(90)
    turtl.circle((size*0.6), 180)
    turtl.setheading(0)

def heartCoords(t):
    #So this takes a function I found online and returns x and y coordinates to draw a heart!
    #also, because the turtle doesn't actually change directions to draw the heart I will lose oints for letting it rotate, that's ok!
    return (16*(math.sin(math.radians(t))**3)), (13*math.cos(math.radians(t)) - (5*math.cos(2*math.radians(t))) - (2*math.cos(3*math.radians(t))) - (math.cos(4*math.radians(t))))

def drawHeart(turtl, startX, startY, size, rotation=0, colr='black', fillcolr='pink'):
    #Note that this changes the size so it's more close to the circle size. I just like it better that way. 
    size = size/10
    
    turtl.penup()
    turtl.goto(startX, startY)
    turtl.color(colr)
    if fillcolr:
        turtl.fillcolor(fillcolr)
        turtl.begin_fill()
    turtl.left(rotation)
    
    #BTW I run the heart coords and go there once before starting so I don't get a giant line from the center of the heart to the actual starting point.
    x, y = heartCoords(1)
    x, y = rotateCoords(x, y, rotation)
    turtl.goto(startX + (x * size), startY + (y * size))
    turtl.pendown()
    for t in range(359):
        x, y = heartCoords(t+1)
        x, y = rotateCoords(x, y, rotation)
        turtl.goto(startX + (x * size), startY + (y * size))
    turtl.end_fill()
    turtl.penup()
    turtl.setheading(0)
    
def randomColor():
    colors = ['red', 'yellow', 'blue', 'green', 'orange', 'purple', 'black', 'gray', 'pink']
    return choice(colors)
    
def randomShape(turtl, startX, startY, size, rotation, colr, fillcolr):
    shapes = [
    drawSquare,
    drawTriangle,
    drawCircle,
    smileyFace,
    drawHeart,
    drawRhombus
    ]
    x = randrange(0, 6)
    shapes [x] (turtl, startX, startY, size, rotation, colr, fillcolr)
    
def main():
    #myTurtle.color = ('yellow','red')
    myTurtle = turtle.Turtle()
    
    myTurtle.width(2)
    myTurtle.speed(10)
    for x in range(13):
        for y in range(7):  
            randomShape(myTurtle, (x*150)-900, (y*150)-450, randrange(70, 100), randrange(0, 360), randomColor(), randomColor())
            print(x*100, y*100)

'''
    if __name__ == '__main__':
        main()
        '''
main()
