#Exercise 5.29
#Display Leap Years
#Rida Abdulwasay
#1/11/2018

print ("\t Leap Years 2001 - 2100")
print ()


NUMBER_OF_YEARS_PER_LINE = 10 #Assign Number of Years Per Line
count = 0 #Set initial Count to 0

for year in range (2001, 2101):
    LeapYear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)    #Leap Year Calulcations
    if LeapYear :
        print (year, end = ' ') #Print if Leap Year
        year += 1 #Add a Year
        count += 1 #Increase Count
        if count % NUMBER_OF_YEARS_PER_LINE == 0:
            print () #Move to next line
            
    
