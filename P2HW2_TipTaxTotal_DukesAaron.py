# CTI-110 
# P2HW2 - Tip Tax Total 
# Aaron Dukes
# 2/18/2018

foodcharge = float( input("please enter the charge of the food:"))

tip = 0.18 * foodcharge

salesTax = 0.07 * foodcharge

total = foodcharge + tip + salesTax

print("foodcharge: $" + format( foodcharge,",.2f"), "Tip: $" + \
format( tip, ",.2f"), "Sales Tax: $" + format(salesTax, ",.2f"), \
"Total: $" + format(total, ",.2f"))
