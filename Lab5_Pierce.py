'''
Date: Sep 18, 2023
@author: Benjamin Pierce
This program allows the user to create an initial deposit to open a bank account.
They can then navigate the menu to deposit more cash, withdraw cash, or check their balance at any time.
'''
#create a global balance variable
balance = 0

#open a bank account
def open_account():
    global balance 
    print('Please make an initial deposit to finalize account creation.')    #welcome user
    initial_deposit = float(input('Enter initial deposit amount: $'))
    balance = initial_deposit
    print(f'You now have ${balance:.2f} in your Gamestop bank account.')    #print variable before returning to main code block
    
#deposit money
def deposit():
    global balance
    deposit_amount = float(input('Enter the amount you would like to deposit: $'))
    balance += deposit_amount
    print(f'You deposited ${deposit_amount:.2f}.  Current balance: ${balance:.2f}')
    
#withdraw money
def withdraw():
    global balance
    withdraw_amount = float(input('Enter the amount you would like to withdraw: $'))
    if withdraw_amount <= balance:
        balance -= withdraw_amount
        print(f'You withdrew ${withdraw_amount:.2f}.  Current balance: ${balance:.2f}')
    else:
        print('Insufficient funds.')
        
#check balance
def check_balance():
    global balance 
    print(f'Your current balance is: ${balance:.2f}')
        
def main():
    while True:    
        print('Welcome to the Bank of Gamestop menu.  Please select option "1" to open an account and make an initial deposit if you have not already. \n1. open account\n2. deposit\n3. withdraw\n4. balance\n5. Exit')
        try: 
            choice = input('Enter you choice (1, 2, 3, 4, or 5 to quit): ')
            if choice == '1':   #runs open_account function
                open_account()
            elif choice == '2':    #runs deposit function
                deposit()
            elif choice == '3':    #runs withdraw function
                withdraw()
            elif choice == '4':    #runs check_balance function
                check_balance()
            elif choice == '5':    #exits
                print('Thank you for banking with Gamestop.  Have a great day diamond hands!')
            else:
                print('Invalid choice. Please select a valid option.')
        except ValueError:
            print('User entered incorrect choice.')
            
    while True:
        another_choice = input('Enter another choice (1, 2, 3, 4, or 5 to quit): ')    #opportunity to select another option)
        if another_choice == '5':
            break    #Exit loop
    
#call main function
if __name__ == "__main__":
    main()