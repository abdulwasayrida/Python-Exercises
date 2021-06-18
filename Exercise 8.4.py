#Exercise 8.4
#Occurrences of a specified character
#Rida Abdulwasay
#1/14/2018
  
           
def main ():
    s = input ("Please enter a string :").strip()
    ch = input ("Please enter the character you want to search for:").strip()
    
    if count(s, ch) ==0:
        print ("The character", ch, "does not appear in the string", s)
    elif count(s, ch) == 1:
        print("The character", ch, "appears once in the string", s)
    else :
        print ("The character", ch, "appears", count(s, ch), "times in the string", s)
             
def count(s, ch):
    numberOfTimes = 0
    for x in range(0, len(s)):
        if s[x] is ch:
            numberOfTimes +=1
    return (numberOfTimes)

main ()


            
        
    
    
