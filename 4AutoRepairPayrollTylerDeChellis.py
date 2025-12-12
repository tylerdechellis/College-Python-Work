# named constants to represent the base hours and
# the overtime multiplier of time and a half

Base_hours=40
OT_Multiplier=1.5

# Get the hours worked and the hourly pay rate

hours=float(input("Enter the number of hours worked: "))
pay_rate=float(input("Enter the hourly pay rate: "))

# Calculate and display the gross pay
if hours>Base_hours:
                  # Calculate the gross pay with overtime
                  overtime=hours-Base_hours

                  # Calculate the amount of overtime pay
                  overtime_pay=overtime*pay_rate*OT_Multiplier

                  # Calculate the gross pay
                  gross_pay=Base_hours*pay_rate+overtime_pay

else:
    # Calculate gross pay without overtime
    gross_pay=hours*pay_rate

print(f"The gross pay is ${gross_pay:,.2f}.")
