#Exercise 7.5 (Continued)
#Geometry: n-sided regular polygon
#Rida Abdulwasay
#1/14/2018

#Import the class Regular Polygon
from RegularPolygon import RegularPolygon

def main ():
    
#Use default for first polygon
    regularPolygon1 = RegularPolygon()
    perimeter = regularPolygon1.getPerimeter()
    area = regularPolygon1.getArea()
    print ("Polygon 1 has a perimeter of", format(perimeter, ".2f"), "and an area of", format(area,".2f"))

#Set the number of sides and side length for second polygon
    regularPolygon2 = RegularPolygon (6,4)
    perimeter2 = regularPolygon2.getPerimeter()
    area2 = regularPolygon2.getArea()
    print ("Polygon 2 has a perimeter of", format(perimeter2, ".2f"), "and an area of", format(area2, ".2f"))

#Set the number of sides, side length, x , and y for the third polygon
    regularPolygon3 = RegularPolygon (10,4, 5.6, 7.8)
    perimeter3 = regularPolygon3.getPerimeter()
    area3 = regularPolygon3.getArea()
    print ("Polygon 3 has a perimeter of", format(perimeter3, ".2f"), "and an area of", format(area3, ".2f"))
    
    
main ()
