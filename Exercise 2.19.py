#Ex. 2.19
#Financial application: calculate future investment value
# Rida Abdulwasay
#1/4/2018

#Prompt user to enter values
investment = eval (input ("Please enter investment amount:"))
AnnualInterestRate = eval (input ("Please enter annual interest rate:"))
years = eval (input ("Please enter the number of years:"))

#Calculate the Monthly Rate and Number of Months
monthlyInterestRate = AnnualInterestRate / 12
months = years * 12

#Calculate Value
value = investment * (1 + monthlyInterestRate/100) ** months

#Print Results
print ("The accumulated value is" , value )
