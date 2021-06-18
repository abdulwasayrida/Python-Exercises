#Exercise 4.17
#Game: (scissor, rock, paper)
#Rida Abdulwasay
#1/8/2018


#Import the random module
import random

#Prompt the user for their position
human_Position = eval (input ("Please choose your position: scissors (0), rock (1), paper (2):"))

#Generate the Computers Position (Random)
computer_Position = random.randint (0 , 3)

#In case of Human Winner
if computer_Position == 0 and human_Position == 1:
    print ("The computer is scissors. You are rock. You Win!!")
if computer_Position == 1 and human_Position == 2:
    print ("The computer is rock. You are paper. You Win!!")
if computer_Position == 2 and human_Position == 0:
    print ("The computer is paper. You are scissors. You Win!!")

#In case of Draw
if computer_Position == 0 and human_Position == 0:
    print ("The computer is scissors. You are scissors. Draw!")
if computer_Position == 1 and human_Position == 1:
    print ("The computer is rock. You are rock. Draw!")
if computer_Position == 2 and human_Position == 2:
    print ("The computer is paper. You are paper. Draw!")

#In case of Computer Winner
if computer_Position == 0 and human_Position == 2:
    print ("The computer is scissors. You are paper. You lost!")
if computer_Position == 1 and human_Position ==0:
    print ("The computer is rock. You are scissors. You lost!")
if computer_Position == 2 and human_Position == 1:
    print ("The computer is paper. You are rock. You lost!")
