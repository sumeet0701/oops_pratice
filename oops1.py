"""
a  = 3 # it is integer object which is equal to variable
print(type(a))

l = [1,3,4,5,6,7,8,9,10,11] 
print(type(l)) # CLASS list 
"""

# Createing a Class
# lets make a software for atm Machine

class AtmMachine(object):
    # function vs methods 
    # methods are bascially a function used for in class  
    # method is special function which is written inside of a class.
    # function written in any class is called a methods.
    def __init__(self):
        # __init__ is a constructor
        # Constructor is a special method 
        # the code inside the constructor is automatically execute when we will create a class object 
        # it will automatically run when class is called 
        self.pin = ""
        self.balance = 0
        self.menu()
    def menu(self):
        user_input = input("""
            Hello, how would you like to proceed?
            1. Enter 1 to Create a pin
            2. Enter 2 to deposit 
            3. Enter 3 to withdraw
            4. Enter 4 to checkout Balance
            5. Enter 5 to Exit
                            
""")
        if user_input == "1":
           self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        else:
            print("Exiting")

    def create_pin(self):
        self.pin = input("Enter your PIN number")
        print("Pin set sucessfully")
    
    def deposit(self):
        temp = input("Enter your PIN number")
        if temp == self.pin:
            amount = int(input("Enter the Amount "))
            self.balance = self.balance + amount
            print("deposit sucessfully")
        else:
            print("Pin is Worng Try it again")
    
    def withdraw(self):
        temp = input("Enter your PIN number")
        if temp == self.pin:
            withdraw_amount = int(input("Enter the Amount to withdraw "))
            if withdraw_amount <= self.balance:
                self.balance = self.balance - withdraw_amount
                print("withdrawal amount sucessfully")
            else:
                print("Not enough funds to withdraw")
        else:
            print("invalid PIN number \n Try again")

    def check_balance(self):
        temp = input("Enter PIN number")
        if temp == self.pin:
            print(self.balance)
        
        else:
            print("invalid PIN number \n Try again")

    def exit(self):
        pass 