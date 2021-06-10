
from loguru import logger

logger.add("debug.log", format="{time} {level} \n{message}", level="DEBUG")


class BankAccount():

    nextAccountNum = 1
    depos = 0
    withd = 0

    def __init__(self, name, bal):
        self.__name = name
        self.__balance = bal
        self.__accountNumber = BankAccount.nextAccountNum
        BankAccount.nextAccountNum +=1

    def __str__(self):
        output = "Name: " + str(self.__name) + "\n"
        output += "AccNum: " + str(self.__accountNumber) + "\n"
        output += "Deposit:" + str(self.depos) + "\n"
        output += "Withdraw:" + str(self.withd) + "\n"
        output += "Balance:" + str(self.__balance) + "\n"
        return output

    def deposit(self, add):
        max = 10000
        self.add = add
        self.depos = add

        if max >= add :
            self.__balance += add
        else:
            print("Максимальна сумма за одну операцію 10000")

    def withdraw(self, amount):
        self.withd = amount
        self.__balance -= amount




account1 = BankAccount("Slava", 12000)
account2 = BankAccount("Vova", 1000)

account1.deposit(7000)
account1.withdraw(20000)
print(account1)

account2.deposit(1000)
account2.withdraw(2000)
print(account1)


logger.debug(account1)
logger.debug(account2)