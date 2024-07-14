class BankAccounts:

    def __init__(self, given_int_rate, given_balance):
        self.int_rate = given_int_rate
        self.balance= given_balance


    def deposit(self, amount):
        if amount > 0 :
            self.balance += amount 
            print(f"deposited ${amount} new balance ${self.balance}")
            return self


    def withdraw(self, amount):
        if amount > 0 and amount < self.balance: 
            self.balance -= amount 
            print(f"withdrawed ${amount} new balance ${self.balance}")
            return self
        else:
            if amount > self.balance:
                self.balance -= 5
                print(f"Insufficient funds {self.balance}")
                return self


    def display_account_info(self):
        print(f"Account information balance ${self.balance}")
        return self


    def yeild_interest(self):
        interest = self.balance * self.int_rate 
        self.balance += interest
        print(f"balance with interest {self.balance}")
        return self


my_account = BankAccounts(.1, 1000).deposit(150).deposit(250).deposit(350).withdraw(550).display_account_info().yeild_interest()

larry = UserBankAccount("larry", "larryayetey@gmail.com")
print(larry.email)


