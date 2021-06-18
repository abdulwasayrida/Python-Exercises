#Ex. 1.11
#Population Project
#Rida Abdulwasay
#1/3/2018


#Assign Numbers/Equations to the Variables
population = 312032486
days = 365
hours = 24 * 365
minutes = 60 * hours
seconds = 60 * minutes
birth = seconds // 7
death = seconds // 13
immigrant = seconds // 45

#Calculate the results
year1 = population + birth - death + immigrant
year2 = year1+ birth - death + immigrant
year3 = year2 + birth - death + immigrant
year4 = year3 + birth - death + immigrant
year5 = year4 + birth - death + immigrant

#Print the results
print ("The total population after 1 year is", year1)
print ("The total population after 2 years is", year2)
print ("The total population after 3 years is", year3)
print ("The total population after 4 years is", year4)
print ("The total population after 5 years is", year5)
