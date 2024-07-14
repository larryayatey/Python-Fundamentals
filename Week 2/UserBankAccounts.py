
class BankInfo:

    all_bank_accounts = []

    def __init__(self, given_int_rate, given_balance):
        self.int_rate = given_int_rate
        self.balance= given_balance


    def deposit(self, amount):
        if amount > 0 :
            self.balance += amount 
            # print(f"deposited ${amount} new balance ${self.balance}")
            return self


    def withdraw(self, amount):
        if amount > 0 and amount < self.balance: 
            self.balance -= amount 
            # print(f"withdrawed ${amount} new balance ${self.balance}")
            return self
        else:
            if amount > self.balance:
                self.balance -= 5
                print(f"Insufficient funds {self.balance}")
                return self


    def display_account_info(self):
        # print(f"Account information balance ${self.balance}")
        return self


    def yeild_interest(self):
        interest = self.balance * self.int_rate 
        self.balance += interest
        print(f"balance with interest {self.balance}")
        return self

    @classmethod
    def all_class(cls):
        for bank in cls.all_bank_accounts:
            print(f"Joshua made a deposit{bank.given_balance}")



class UserBankAccount:

    def __init__(self, given_name, given_email):
        self.name = given_name
        self.email = given_email
        self.account = BankInfo(given_int_rate=.2, given_balance=0)



    def make_deposit(self, amount):
        self.account.deposit(amount)
        print(f"Joshua made a deposit new balance ${self.account.balance}")
        return self

    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        print(f"Joshua made a withdraw ${amount}")
        return self

    def display_user_balance(self):
        print(f"Joshua new acocunt balance ${self.account.balance}")
        return self

range = UserBankAccount("Joshua", "Joshuademo@gmail.com")

range.make_deposit(1000)

range.make_withdraw(350)

range.display_user_balance()


