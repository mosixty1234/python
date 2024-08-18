# how again() function is commented 

# Define again() function to ask user if they want to use the calculator again
def calculate():
    # This is where your calculation logic would go
    print("Performing a calculation...")
    # After the calculation, ask the user if they want to calculate again
    again()

def again():
    # Take input from user
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    # If user types Y, run the calculate() function
    if calc_again.upper() == 'Y':
        calculate()

    # If user types N, say good-bye to the user and end the program
    elif calc_again.upper() == 'N':
        print('See you later.')

    # If user types another key, run the function again
    else:
        again()

# Start the calculation process
calculate()
