
def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        print(balance)
        return balance
    return withdraw


wd1 = make_withdraw(50)
wd2 = make_withdraw(100)
wd1(20)
wd2(10)
wd2(10)
