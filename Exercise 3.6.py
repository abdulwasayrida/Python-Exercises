#Exercise 3.6
#Find the character of an ASCII code
#Rida Abdulwasay
# 1/5/2018

#Prompt the user for a character
ASCII = eval(input ("Please enter an ASCII code (integer between 0 and 127):"))

#Convert it to a Character
Character = chr(ASCII)

#Display Results
print ("The character for the ASCII code" , ASCII , "is" , Character)
