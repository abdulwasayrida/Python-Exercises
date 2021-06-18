#Exercise 7.3 (Continued)
#The Account Class
#Rida Abdulwasay
#1/13/2018

#Import Account
from Account import Account

def main ():
    #Set the ID, Balance, and Annual Interest Rate
    account = Account(1122, 20000, 4.5)
    
    #Set The Withdrawl to $2,500
    account.withdraw (2500)
    
    #Set The Deposit to $3,000
    account.deposit (3000)
    
    #Print the Results
    print ("For Account with ID" , account.getID (), ":")
    print ("The Current Balance is: $", account.getBalance() )
    print ("The Monthly Interest Rate is:", format(account.getMonthlyInterestRate(), ".2"), "%")
    print ("The Monthly Interest is: $", format(account.getMonthlyInterest(), ".2f"))
    
main ()
