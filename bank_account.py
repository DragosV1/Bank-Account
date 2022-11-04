class BankAccount:
    def __init__(self, balance: float, name: str):
        self.name = name
        self.balance = balance

    def withdraw(self, amount: float) -> float:
        """ You can withdraw minimum 50, if amount is greater than 1000 you'll get asked to confirm your withdrawing. """

        if amount >= 50: 
            if amount > self.balance:
                print("Insufficient balance!")
                print(f"Your balance is {self.balance}.")
            if amount <= self.balance:
                if amount >= 1000:
                    confirmation = input("You need to confirm if you are sure with this amount of money. Type yes or no: ").lower()
                    if confirmation == "yes":
                        self.balance -= amount
                        print("Withdraw successfully!")
                        print(f"Balance: {self.balance}")
                    elif confirmation == "no":
                        print("Withdraw canceled!")
        else:
            print("Error: Minium of withdraw is 50.")

    def deposit(self, amount: float) -> float:
        """ You can deposit minium 10 """

        if amount >= 10:
            self.balance += amount
            print("You have successfully added to your bank account.")
            print(f"Balance: {self.balance}")
        else:
            print("Error: Minium to deposit is 10.")
    
    def get_balance(self) -> float:
        print(f"Hello {self.name}! Your balance: {self.balance}")


if __name__ == "__main__":
    obj = BankAccount(5303.23, "Name")
    obj.get_balance()
    obj.deposit(amount = float(input("Enter the amount of money you want to deposit: ")))
    obj.withdraw(amount = float(input("Enter the amount of money you want to withdraw: ")))