#Exercise 6.11
#Financial Application: Compute Commissions
#Rida Abdulwasay
#1/12/2018

#Create Function
def computeCommission(salesAmount):
    if salesAmount <= 5000:
        commission = sales * 0.08
        return (commission)

    if salesAmount <= 10000 and salesAmount > 5000:
        commission = 5000 * 0.08 + (salesAmount- 5000) * 0.10
        return (commission)
    
    if salesAmount >10000:
        commission = 5000 * 0.08 + 5000 * 0.10 + (salesAmount -10000) * 0.12
        return (commission)
    
    if salesAmount <= 0:
        print ("Wrong number")

 #Create Function Main   
def main ():
    salesAmount = 5000
    print ("Sales Amount \tCommission")
    for salesAmount in range (10000, 105000, 5000):
        print (salesAmount, " \t \t", computeCommission(salesAmount))
 
    
 #Call the Main Function   
main ()
