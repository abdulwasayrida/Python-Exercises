#Exercise 5.3
#Conversion from kilograms to pounds
#Rida Abdulwasay
#1/10/2018

print ("Kilograms    Pounds")
print ("-----------------------------------------------")

kilogram = 1
pound = 0

for kilogram in range (1, 200, 2):          #Set a range for the data
    pound = kilogram * 2.2 #Calculation for pounds
    print (format (str(kilogram),"<5s") , format(pound,">15.1f"))         #Printing Results and Rounding the pounds

