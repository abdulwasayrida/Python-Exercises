#Ex. 2.25
#Turtle: draw a rectangle
# Rida Abdulwasay
#1/4/2018

#import the turtle module
import turtle

x , y = eval (input ( "Please enter the coordinates for the center of the rectangle:"))
width = eval (input ("Please enter the width of the rectangle:"))
height =  eval (input ("Please enter the height of the rectangle:" ))

#Go to the  first side
turtle. penup ()
turtle. goto (x, y)
turtle. forward (height/2)

#Begin Drawing
turtle. pendown ()
turtle. left (90)
turtle. forward (width/2)
turtle. left (90)
turtle. forward (height)
turtle. left (90)
turtle. forward (width)
turtle. left (90)
turtle. forward (height)
turtle. left (90)
turtle. forward (width/2)
turtle. done ()

