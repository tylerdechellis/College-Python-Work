# Programmer:       Tyler DeChellis, Christian Lafond, Matt Cozart, Carson Hatem
# Updated:          November 9, 2023
# Program Purpose:  The purpose of this program is to allow the user to choose different
# movie seats and tickets, as well as snacks and drinks


#Algorithm
#
# A. Input
#    A. Code to display the prices for tickets, seats, snacks, and coupons
#    B. Code to define the NC state tax rate and a def function to add the tax
#       rate to the total amount. 
#
# B. Process
#    A. Code to display the menu using a print function and allow the user to select
#       what they want to choose from the menu
#
# C. Output
#    A. If and elif code that displays what the user selects and adds the totals to the
#       shopping cart based on what they select
#    B. An option to exit the program
#
# D. End

# Code to define the theater as a list of lists
theater = [['E' for _ in range(10)] for _ in range(10)]  

# Code to diplay the prices for tickets, seats, snacks, and coupons
ticket_prices = {
    "Adult": 12.00,
    "Child": 7.50,
    "Senior": 9.00
}

seat_prices = {
    "Standard": 1.50,
    "VIP": 3.00
}

snack_prices = {
    "Popcorn": 5.00,
    "Soda": 3.00,
    "Candy": 2.50
}

Coupons = {
    "10CAP": 0.10,  # 10% off total_price
    "25CAP": 0.25  # 25% off total_price
}

# Code to define the tax rate
tax_rate = 0.07

# Code for a def function to calculate the total cost with tax
def calculate_total_cost(cost):
    return cost + cost * tax_rate

# Code to initialize the shopping cart
shopping_cart = []
Final_Price = 0.00
Discounted_Total_Price = 0.0

# Code to display the menu and allow the customer to select an option
# and if functions to determine what the customer chose
while True:
    print("\nWelcome to the Movie Theater!")
    print("1. Movie Showtimes and Ticket Prices")
    print("2. Seat Prices")
    print("3. Snack and Drink Prices")
    print("4. View Shopping Cart")
    print("5. Checkout")
    print("6. Coupon")
    print("7. Exit")

    choice = input("Please select an option (1/2/3/4/5/6/7): ")

    if choice == "1":
        print("\nMovie Showtimes and Ticket Prices:")
        for ticket_type, price in ticket_prices.items():
            print(f"{ticket_type}: ${price:.2f}")
        selected_ticket = input("Select a ticket type: ")

        if selected_ticket in ticket_prices:
            while True:
                try:
                    row = int(input("Select a row (1-10): "))
                    seat = int(input("Select a seat number (1-10): "))
                    if 1 <= row <= 10 and 1 <= seat <= 10:
                        if theater[row - 1][seat - 1] == 'E':
                            theater[row - 1][seat - 1] = 'X'  
                            print(f"You have reserved Row {row}, Seat {seat}.")
                            shopping_cart.append((f"Row {row}, Seat {seat} ({selected_ticket})", ticket_prices[selected_ticket]))
                            break
                        else:
                            print("Sorry, that seat is already taken. Please choose another.")
                    else:
                        print("Invalid row or seat number. Please select values between 1 and 10.")
                except ValueError:
                    print("Invalid input. Please enter a valid row and seat number.")
        
    elif choice == "2":
        print("\nSeat Prices:")
        for seat_type, price in seat_prices.items():
            print(f"{seat_type}: ${price:.2f}")
        selected_seat = input("Select a seat type: ")

        if selected_seat in seat_prices:
            shopping_cart.append((selected_seat, seat_prices[selected_seat]))
    
    elif choice == "3":
        print("\nSnack and Drink Prices:")
        for snack, price in snack_prices.items():
            print(f"{snack}: ${price:.2f}")
        selected_snack = input("Select a snack or drink: ")

        if selected_snack in snack_prices:
            shopping_cart.append((selected_snack, snack_prices[selected_snack]))
    
    elif choice == "4":
        print("\nShopping Cart:")
        total_price = 0
        for item, price in shopping_cart:
            if item.startswith("Row"):  
                print(f"{item}: ${price:.2f}")
            else:
                print(f"{item}: ${price:.2f}")
            total_price += price
        print(f"Total Price: ${calculate_total_cost(total_price):.2f}")
    
    elif choice == "5":
        if shopping_cart:
            total_price = sum(price for _, price in shopping_cart)
            print(f"Total Price (including tax): ${calculate_total_cost(total_price):.2f}")
            shopping_cart = []
        else:
            print("Your shopping cart is empty.")

    elif choice == "6":
        print("\nCoupon:")
        print("Select the following coupon that you have: ")
        for coupon, discount in Coupons.items():
            print(f"{coupon}")

        selected_coupon = input("Enter your coupon code: ")
        if selected_coupon in Coupons:
            discount = Coupons[selected_coupon]
            total_price = sum(price for _, price in shopping_cart)
            discounted_total_price = total_price * (1 - discount)
            print(f"{discount * 100}% discount applied.")
        else:
            print("Invalid coupon code.")
    
    elif choice == "7":
        print("Thank you for visiting! Have a great time at the movies.")
        break
    
    else:
        print("Invalid choice. Please select a valid option.")


