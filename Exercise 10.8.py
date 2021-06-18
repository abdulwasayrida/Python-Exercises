#Exercise 10.8
#Find the index of the smallest element
#Rida Abdulwasay
#1/21/2018

def indexOfSmallestElement (lst):
    return (lst.index(min(lst)))

def main ():
    s = input("Enter a list of numbers separated by a space:")
    items = s.split()
    if len(items) ==1:
        print ("There is only one number in the list:", items)
    else:
        lst = [eval (x) for x in items]
        print ("The smallest number is", min(lst), ", and its index position in the list", lst, "is", indexOfSmallestElement (lst))

main ()

