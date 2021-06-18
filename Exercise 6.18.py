#Exercise 6.18
#Display a matrix of 0s and 1s
#Rida Abdulwasay
#1/12/2018


def printMatrix(n):     #Create a function
    from random import randint
    for side1 in range (n):
        for side2 in range (n):
            print(randint(0, 1), end=" ") #randint generates the random number sequence
        print(" ")
        
            

#Prompt the user to enter a number
def main ():
    number = eval (input ("Please enter a number: "))
    printMatrix(int(number))
    if number <= 0:
        print ("That is not a valid number:")
        
main () #Call the main function
