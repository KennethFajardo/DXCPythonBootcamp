pin = 1234
balance = 1000.00
chances = 3
restart = 'Y'

while chances > 0:
    input_pin = int(input('\nPlease enter your 4-digit PIN: '))
    if pin == input_pin:
        print('PIN verified\n')
        while restart not in ('n', 'N', 'NO','no'):
            print('******* M E N U *******')
            print('Type 1 to check your balance\nType 2 to quit\n')
            option = int(input('What would you like to choose?'))
            if option == 1:
                print('Your balance is ', balance, '\n')
                restart = input('Would you lke to go back to the menu? Type y for yes and n for no\n')
                if restart in ('n', 'N', 'NO','no'):
                    print('Thank you for choosing K bank.')
                    break
            elif option == 2:
                print('Please wait while your card is returned.\n')
                print('Thank you for your service.')
                break
            else:
                print('Please enter a correct number \n')
                restart('y')
    else:
        chances = chances - 1
        print('Wrong PIN. Try again. Retry attempts: ', chances, '\n')
        if chances == 0:
            print('There are no more attempts left. Goodbye.')
            break