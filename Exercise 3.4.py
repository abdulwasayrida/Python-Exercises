#Exercise 3.4
#Geometry: area of a pentagon
#Rida Abdulwasay
# 1/5/2018

#import the math module
import math

#Prompt User to Enter side
side = eval(input( "Please enter the side of a pentagon:"))

#Assign Value to PI
PI = math. pi

#Break Operation into 3 Parts
operation1 = 5 * (side**2)

operation2 = math.tan (PI/5)

operation3 = 4 * operation2

#Calculate and Print the Area
area = operation1 / operation3
print ("The area of a pentagon with side" , side , "is" , area )
