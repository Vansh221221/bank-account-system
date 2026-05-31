class BankAccount:
    def __init__(self, name, account_no,balance):
        self.name = name
        self.account_no = account_no
        self.__balance = balance
    def deposit(self, amount):
        if amount>0:
            self.__balance += amount 
            print(f"{amount} deposit ho gya")
        else:
            print("Bhai amount galat hai")
            
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            print(f"Bhai {amount} withdraw ho gyi  ")
            self.__balance -=amount
        else:
            print(f"Bhai {amount}rs account me hai hi nhi ")
           
            
    def check_balance(self):
        print(f"Bhai apka balance hai : {self.__balance}")
    
    def show_details(self):
         print(f"Name: {self.name}")
         print(f"Account No: {self.account_no}")
    
account = BankAccount("Vansh",122,10000)

while True:
    user_choice = input("what do you want to do\n 1. Deposit \n 2. Withdraw \n 3. Check Balance \n 4. Exit \n 5.show details \n:")

    if user_choice in ["deposit", "Deposit","1"]:
        depo_amount = int(input("Enter deposit amount: "))
        account.deposit(depo_amount)
    
    elif user_choice in ["withdraw", "Withdraw","2"]:
        withdraw_amount = int(input("Enter withdraw amount: "))
        account.withdraw(withdraw_amount)
    
    elif user_choice in ["check balance","3"]:
        account.check_balance()
    
    elif user_choice in ["exit","4","Exit"]:
        print("ok bye! have a nice day")
        break
    
    elif user_choice == ["show details","5"]:
        account.show_details()