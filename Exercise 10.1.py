#Exercise 10.1
#Assign Grades
#Rida Abdulwasay
#1/21/2018


s = input("Enter a list of numbers separated by a space:")
items = s.split()
lst = [eval (x) for x in items]

       
for i in range (len(lst)):
    if lst[i] >=max(lst) -10:
        grade = 'A'
    elif lst[i] >= max(lst) -20:
        grade = 'B'
    elif lst[i] >= max(lst) -30:
        grade = 'C'
    elif lst[i] >= max(lst) -40:
        grade = 'D'
    else:
        grade = 'F'
    print("Student", i, "has a score of", lst[i], "and a grade of", grade)
