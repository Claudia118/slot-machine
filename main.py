#global variable
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

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

def get_lines():
    while True:
        lines = input("Please enter the number of lines to bet on (1" + str(MAX_LINES) + ")? ")
        if lines.isdigit(): # Check that user input is a number
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid number of lines.")
        else:
            print("Enter a number")
    return lines

def get_bet():
    while True:
        amount = input("What amount would you like to bet on each line? $")
        if amount.isdigit(): # Check that user input is a number
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Enter a number")
    return amount


def main():
    balance = deposit()
    lines = get_lines()

    # Check if amount bet is within their balance
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance} ")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

main()

