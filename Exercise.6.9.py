 #Exercise 6.9
#Conversions between feet and meters
#Rida Abdulwasay
#1/12/2018

#Create a Function for the Conversion
def footToMeter (foot):
    meter = format (0.305 * foot, "9.3f")
    return meter
    
#Create a Function for the Conversion
def meterToFoot (meter):
    foot = format ((meter) / 0.305,  "9.3f")
    return foot

#Create a Function called Main to create a table and the values
def main():
    print("Feet \t  Meters \t |  Meters \t   Feet")
    print ("--------------------------------------------------------------------------")
    foot = 1
    meter = 20
    for foot in range(1, 11):
        print (format(foot, ".1f"), "\t" , footToMeter (foot), "\t | ", format(meter, ".1f"), " \t\t", meterToFoot(meter))
        meter += 5
#Call Main
main ()


                          
 

        
