#Exercise 4.7
#Financial Application: monetary units
#Rida Abdulwasay
#1/8/2018

# Receive the amount 
amount = eval(input("Enter an amount in double:"))

# Convert the amount to cents
remainingAmount = int(amount * 100)

# Find the number of one dollars
numberOfOneDollars = int(remainingAmount / 100)
remainingAmount = int(remainingAmount % 100)

# Find the number of quarters in the remaining amount
numberOfQuarters = int(remainingAmount / 25)
remainingAmount = remainingAmount % 25

# Find the number of dimes in the remaining amount
numberOfDimes = int(remainingAmount / 10)
remainingAmount = remainingAmount % 10

# Find the number of nickels in the remaining amount
numberOfNickels = int(remainingAmount / 5)
remainingAmount = remainingAmount % 5

# Find the number of pennies in the remaining amount
numberOfPennies = remainingAmount

# Display results
print("Your amount", amount, "consists of")
if numberOfOneDollars >= 1:
    print (numberOfOneDollars, "dollars")
if numberOfQuarters >= 1:
    print (numberOfQuarters, "quarters")
if numberOfDimes >= 1:
    print (numberOfDimes,  "dimes")
if numberOfDimes >= 1:
    print (numberOfNickels, "nickels")
if numberOfPennies >= 1:
    print (numberOfPennies, "pennies")

