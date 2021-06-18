#Exercise 4.11
#Find the number of days in a month
#Rida Abdulwasay
#1/8/2018

#Prompt the user to enter the month and year
month  = eval (input ("Please enter a month [Number between 1 - 12):"))
if month <1:
    print ("That's not a real month!!")
    
if month >12:
    print ("That's not a real month!!")

if month <= 12 and month > 0:
    year = eval (input ("Please enter a year:"))

#Find the month 
if month == 1:
    Month = 'January'
elif month == 2:
    Month = 'February'
elif month == 3:
    Month = 'March'
elif month == 4:
    Month = 'April'
elif month == 5:
    Month = 'May'
elif month == 6:
    Month = 'June'
elif month == 7:
    Month = 'July'
elif month == 8:
    Month = 'August'
elif month == 9:
    Month = 'September'
elif month == 10:
    Month = 'October'
elif month == 11:
    Month = 'November'
elif month == 12:
    Month = 'December'

days = 0

#Find the number of days
if Month ==  'January' or 'March' or 'May' or 'July'  or 'August'  or 'October' or 'December':
    days = 31
    
elif Month == 'April'  or 'June' or 'September' or 'November':
    day = 30

#Find whether it is a Leap Year
LeapYear = (year % 4 == 0 and year % 100 != 0) or \
   (year % 400 == 0)

if LeapYear and Month == 'February':
    days = 29

#Display Results
print (Month, year , "has" , days, "days")
