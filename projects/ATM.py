import sys
import time

# ATM Machine Simulation

print('Welcome to the ATM Machine')
#first we will check if the card is inserted
a = input('Please insert your card: ')
if a == 'yes':
    print('Card accepted')
    # Card accepted, now we will ask for the language selection
    print('choose the language: ')
    print('1. English')
    print('2. telugu')
    print('3. Kannada')
    language = input('Please select a language (1, 2, or 3): ')
    if language == '1':
        print('You have selected English')
        #Successfully selected English, now we will ask for the PIN
        print('Please enter your PIN')
        pin = int(input('Enter PIN: ') )
        if pin == 1234:
            print('PIN accepted')
            # Successfully entered PIN, now we will show the account options
            print('Welcome to your account')
            print('Choose the following options:')
            print('1. Check Balance')
            print('2. Deposit Money')
            print('3. Withdraw Money')

            option = input('Please select an option (1, 2, or 3): ')
            if option == '1':
                print('Your balance is 100000')
                # this point is clear, we are just displaying the balance


            elif option == '2': 
                print('How much would you like to deposit?')
                deposit = input('Enter amount: ')
                # Check if the deposit amount is valid i.e, multiples of 100 or not
                if int(deposit) % 100 != 0:
                    print('Invalid deposit amount. Please enter a valid amount in multiples of 100.')
                    sys.exit()
                else:
                    if int(deposit) < 0:
                        print('Invalid deposit amount. Please enter a positive number.')
                        sys.exit()
                    elif int(deposit) > 10000:
                        print('Deposit amount exceeds limit. Please enter a smaller amount.')
                        sys.exit()
                    else:
                        print('Processing your deposit...')
                        time.sleep(2)
                        print('You have deposited', deposit)
                        # After deposit, we can check the current balance
                        # Assuming the initial balance is 100000 for this simulation
                    check_current_balance = input('Do you want to check your current balance? (yes/no): ')
                    if check_current_balance.lower() == 'yes':
                        print('Your current balance is', 100000 + int(deposit))
                    else:
                        print('Thank you for using the ATM Machine')


            elif option == '3':
                print('How much would you like to withdraw?')
                withdraw = input('Enter amount: ')
                # Check if the withdrawal amount is valid i.e, multiples of 100 or not
                if int(withdraw) % 100 != 0:
                    print('Invalid withdrawal amount. Please enter a valid amount in multiples of 100.')
                    sys.exit()
                else:
                    if int(withdraw) < 0:
                        print('Invalid withdrawal amount. Please enter a positive number.')
                        sys.exit()
                    elif int(withdraw) > 100000:
                        print('Insufficient funds. You cannot withdraw more than your current balance.')
                        sys.exit()
                    else:
                        
                        print('Processing your withdrawal...')
                        time.sleep(2)
                        print('You have withdrawn', withdraw)
                    # After withdrawal, we can check the current balance

                    check_current_balance = input('Do you want to check your current balance? (yes/no): ')
                    if check_current_balance.lower() == 'yes':
                        print('Your current balance is', 100000 - int(withdraw))
                    else:
                        print('Thank you for using the ATM Machine')
        
                    # End of withdrawal and balance check process
        else:
            print('Incorrect PIN. Please try again.')
            exit() 
        # End of PIN validation i.,f the PIN is incorrect, we exit the program

    elif language == '2' or language == '3':
        print('You have selected Telugu/Kannada, Currently this language is not supported')
        #if user selects Telugu or Kannada, we will exit the program, because we are not supporting these languages in this simulation
    else:
        print('Invalid selection. Please try again.')
        sys.exit()

    

    
else:
    print('Please insert a valid card')
    # If the card is not inserted, we ask the user to insert a valid card


print('Thank you for using the ATM Machine')
# End of ATM Machine Simulation