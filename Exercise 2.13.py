#Ex. 2.13
#Split Digits
# Rida Abdulwasay
#1/4/2018

#Prompt User to Enter a Four Digit Integer
number = eval(input("Please enter a four digit integer: " ))

#Separate the Ones
ones = number % 10

#Separate the Tens
number2 = number // 10
middledigits = number2 %100
tens = middledigits % 10

#Separate the Hundreds
hundreds = middledigits // 10

#Separate the Thousands
thousands = number // 1000

print (ones)
print (tens)
print (hundreds)
print (thousands)
