# User deposit function
def deposit():
    while True:
        amount = input("Please enter amount you would like to deposit. $")
        if amount.isdigit(): # Check that user input is a number
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Enter a number")
    return amount

deposit()