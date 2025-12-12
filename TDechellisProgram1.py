# Programmer:       Tyler DeChellis
# Updated:          September 7, 2023
# Program Purpose:  The purpose of this program is a toy order program 
#                   that will display the toy name and the total price with tax


#Algorithm
#
# A. Input
#    A. Get the toy name
#    B. Get the quantity or number of toys they want to order
#    C. Get unit price of the toy
#
# B. Process
#    A. Compute the total amount by multiply price times quantity
#        total = price * quantity
#    B. Compute the total amount with NC State tax of 7%
#        totalwithtax = total * .07 + total
#
# C. Output
#    A. Print  The total amount of your order, the toy name and total with tax.
#
# D. End



# The lines below allow the user to input their product information
# the toy name, quantity and price
toy = input("Type in the toy name you want to buy ")
price = float(input("Enter in the price "))
qty = float(input("Enter in the quantity you want to order "))


# The calculation below computes the total amount ordered
total = float(price) * float(qty)

# The calculation below computes the total with tax
totalwithtax = (total * .07) + total

# Print the toy name and total amount with tax
print (" The total amount of your order for the toy, with tax is " , "${:,.2f}".format(totalwithtax)) 

