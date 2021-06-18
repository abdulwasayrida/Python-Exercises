#Exercise 5.17
#Display the ASCII Character table
#Rida Abdulwasay
#1/10/2018

count = 0 #Set Initial Count
characters= 0
print ("\tASCII Character Table") #Display Title
for characters in range (33, 127):
     Character = chr(characters) #Convert Number to Character
     print (Character, end = " ") #Print Character
     characters += 1
     count += 1
     if count % 10 == 0:
          print ()
    

     
