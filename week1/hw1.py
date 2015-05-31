# pylint: skip-file

"""
Home work 1
"""

# Question 1
print(type(3.14159))

# Question 3
print(90 % 60)

# Question 5
string = 'Hello world!'
print(string[len(string) - 1])

# Question 7
val1 = [1, 2, 3]
val2 = val1[1:]
val1[2] = 4
print(val2[1])

# Question 8
dictionary = {False: 1}
print(dictionary)


# Question 9
def appendsums(lst):
    """
    Repeatedly append the sum of the current last three elements of lst to lst.
    """
    i = 0
    while i != 25:
        i += 1
        lst.append(lst[-1] + lst[-2] + lst[-3])

sum_three = [0, 1, 2]
appendsums(sum_three)
print(sum_three[20])


# Question 10
class BankAccount:
    """ Class definition modeling the behavior of a simple bank account """
    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        self._account = initial_balance
        self._fees = 0

    def deposit(self, amount):
        """Deposits the amount into the account."""
        self._account += amount

    def withdraw(self, amount):
        """
        Withdraws the amount from the account.  Each withdrawal resulting in a
        negative balance also deducts a penalty fee of 5 dollars from the balance.
        """
        self._account -= amount
        if self._account < 0:
            self._account -= 5
            self._fees += 5

    def get_balance(self):
        """Returns the current balance in the account."""
        return self._account

    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        return self._fees

my_account = BankAccount(10)
my_account.withdraw(5)
my_account.deposit(10)
my_account.withdraw(5)
my_account.withdraw(15)
my_account.deposit(20)
my_account.withdraw(5)
my_account.deposit(10)
my_account.deposit(20)
my_account.withdraw(15)
my_account.deposit(30)
my_account.withdraw(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(50)
my_account.deposit(30)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5)
my_account.deposit(20)
my_account.withdraw(15)
my_account.deposit(10)
my_account.deposit(30)
my_account.withdraw(25)
my_account.withdraw(5)
my_account.deposit(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(10)
my_account.withdraw(15)
my_account.deposit(10)
my_account.deposit(30)
my_account.withdraw(25)
my_account.withdraw(10)
my_account.deposit(20)
my_account.deposit(10)
my_account.withdraw(5)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5)
my_account.withdraw(15)
my_account.deposit(10)
my_account.withdraw(5)
print(my_account.get_balance(), my_account.get_fees())
