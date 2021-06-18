#Exercise 4.23
#Geometry: point in a rectangle?
#Rida Abdulwasay
#1/8/2018

import turtle

#Prompt the user to enter a point
x , y = eval(input("Please enter a point with two coordinates:"))

#Draw the rectangle
turtle. color ("blue")
turtle. penup ()
turtle. forward (2.5)
turtle. left (90)
turtle. pendown()
turtle. forward (5)
turtle. left (90)
turtle. forward (5)
turtle. left (90)
turtle. forward (10)
turtle. left (90)
turtle. forward (5)
turtle. left (90)
turtle. forward (5)

#Draw the point
turtle. pendown ()
turtle. color ("red")
turtle. begin_fill ()
turtle. penup ()
turtle. goto (x , y)
turtle.pendown ()
turtle. circle (2)
turtle. end_fill ()
turtle. hideturtle ()

#Display the status of the point

x2, y2 = x , y
x1, y1 = 0, 0

distance = ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)) ** 0.5

if distance <= 10 and distance >= 5.0/2:
    print ("Point (" , x , "," , y, ") is inside of the rectangle")

else:
    print ("Point (", x , ",",  y , ") is outside the rectangle")
