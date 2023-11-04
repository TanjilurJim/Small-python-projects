# Will take input from the user, their name and how much sales they made based on that will get 13% comission
#comission calculator

# Commission calculator


name = input("Please enter your name: ")


sales = None


while sales is None:
    sales_input = input("Please enter the sales you made: ")


    try:
        sales = float(sales_input)

        if sales.is_integer():
            sales = int(sales)
    except ValueError:
        print("Please enter a valid number for sales. Do not include any letters or special characters.")


commission_rate = 0.13
commission = sales * commission_rate


total_earnings = sales + commission


print(f"Congratulations {name}, you have made sales of {sales} taka this month.")
print(f"Your commission is {commission:.2f} taka, making your total earnings {total_earnings:.2f} taka.")
