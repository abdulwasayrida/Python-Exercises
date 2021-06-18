#Ex. 2.5
#Financial Application: Calculate Tips
# Rida Abdulwasay
#1/4/2018

#Prompt User for subtotal and gratuity rate
subtotal, gratuityRate = eval(input("Please enter a subtotal and gratuity rate:"))

#Calculate Gratuity and Total
gratuity = (gratuityRate/100) * subtotal
total = gratuity + subtotal

#Print Results
print ("The gratuity is" , gratuity , "and the total is" , total )
