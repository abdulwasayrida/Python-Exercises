#Exercise 3.9
#Financial application : payroll
#Rida Abdulwasay
#1/5/2018

#Prompt User to Enter Data

name = input ("Please enter employee's name:")
numberOfHour = eval(input ("Please enter the number of hours worked in a week:"))
hourlyPay = eval(input ("Please enter pay rate:"))
federalTaxRate = eval(input ("Please enter federal tax withholding rate:"))
stateTaxRate = eval(input ("Please enter state tax withholding rate:"))

#Calculations
federalTax = federalTaxRate * 100
stateTax = stateTaxRate * 100
grossPay = (numberOfHour * hourlyPay)
federalWithholding = federalTaxRate * grossPay
stateWithholding = stateTaxRate * grossPay
totalDeduction = federalWithholding + stateWithholding
netPay = grossPay - totalDeduction

#Format
grossPay = format (grossPay, ".2f") 
federalWithholding = format (federalWithholding, ".2f")
stateWithholding = format(stateWithholding, ".2f")
totalDeduction = format (totalDeduction, ".2f")
netPay = format (netPay, ".2f")

#Print Payroll
print ()
print ("Employee's name:" , name)
print ("Hours worked:" , numberOfHour )
print ("Pay Rate: $" , hourlyPay)
print ("Gross Pay: $", grossPay )
print ("Deductions:")
print ("\t Federal Withholding (", federalTax , "%) : $", federalWithholding , "\n",
    "\t State Withholding (", stateTax , "%) : $", stateWithholding , "\n",
    "\t Total Deduction: $" , totalDeduction , "\n")
print ("Net Pay: $" , netPay)
