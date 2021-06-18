#Exercise 7.5
#Geometry: n-sided regular polygon
#Rida Abdulwasay
#1/14/2018

import math

#Create a Class named RegularPolygon
class RegularPolygon:
    def __init__(self, n = 3, side = 1, x = 0, y = 0):
        self.__n = n
        self.__side =  side
        self.__x = x
        self.__y = y

#Create a function to the number of side (n)
    def getN(self):
        return self.__n
    
#Create a function to get the length of the side
    def getSide(self):
        return self.__side

#Create a function to get the X coordinate of the center
    def getX(self):
        return self.__x

#Create a function to get the Y coordinate of the center
    def getY(self):
        return self.__y

#Create a function to get the Perimeter
    def getPerimeter(self):
        perimeter = self.__n * self.__side
        return perimeter

#Create a function to get the Area
    def getArea(self):
         n = self.__n
         side = self.__side
         areaPart1 = n * (side **2)
         areaPart2 =  4 * math.tan ( math.pi / n )
         area = areaPart1 / areaPart2
         return area

 #Create a function to set the number of sides       
    def setN(self, n):
         self.__n = n

#Create a function to set the side length
    def setSide(self, side):
         self.__side = side
         
#Create a function to set the center coordinates
    def setXY(self, x, y):
        x , y = self.__x , self.__y
        
         
