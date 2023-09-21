'''here we are making a program for atm machine'''

'''class name ATM
data/variable name - pin and balance

function/methords- 1. Create pin
2. change pin
3. check balance
4. deposit
5. withrow
6. exit
'''
class Atm():


    def __init__(self):
        self.pin='1234'
        self.balance=1000

        self.menu()


    def menu(self):
        user_input=input('''
    Hello, How wolud you like to Proceed Sir
    1. Enter 1 for create ATM pin
    2. Enter 2 for change your pin
    3. Enter 3 for Check balance
    4. Enter 4 for deposit
    5. Enter 5 for withrow
    6. Enter 6 for Exit\n\nPlease Sir Enter a number: ''')
        
        if user_input=='1':
            self.createpin()
            # print("Please Create Your pin")
        elif user_input=='2':
            self.changeatmpin()
            # print("Please Enter your old pin")
        elif user_input=='3':
            self.checkbalance()
            # print("Please enter you pin")
        elif user_input=='4':
            self.deposit()
            # print("Please enter deposit")
        elif user_input=='5':
            self.withrow()
            # print("Please enter you withrow")
        else:
            self.exit()
            # print("EXIT")        


    #here i create methods for performing different-2 task 

    def createpin(self):
        self.pin=int(input("Please Create a your ATM pin:"))
        print("your pin has created")

    #now make a function for change Atm pin
    def changeatmpin(self):
        temp=int(input("please enter you old password:"))
        if temp==int(self.pin):
            new_pin=input("Please Enter your new ATM pin:")
            self.pin=new_pin
            print("Pin has changed....")
        else:
            print("you have entered Wrong Pin...Please try again")
    
    #make a method for chack bank balance
    def checkbalance(self):
        temp=int(input("Please Enter your PIN:"))
        if temp==int(self.pin):
            print(f'Your bank balance is {self.balance} Rs....!')
        else:
            print("you have entered Wrong Pin Plase try again....!")
    

    #make a function for deposit
    def deposit(self):
        temp=int(input("Please Enter Your PIN:"))
        if temp==int(self.pin):
            deposit_money=int(input("How much money Wolud you like to Deposit Sir:"))
            self.balance+=deposit_money
            print(f"Your balance is {self.balance}Rs....!")
        else:
            print("You have Entered Wrong Password Sir, Please try again")


    #Make a methods for withrow

    def withrow(self):
        temp=int(input("Please Enter Your PIN:"))
        if temp==int(self.pin):
            withrow_money=int(input("How much money Wolud you like to withrow Sir:"))
            self.balance-=withrow_money
            print(f"Your balance is {self.balance}Rs....!")
        else:
            print("You have Entered Wrong Password Sir, Please try again")

    
    def exit(self):
        exit
        print("Thank You Sir.....!")
    


my_atm=Atm()