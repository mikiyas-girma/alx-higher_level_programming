
def account(initial_balance):
    """this function contains another functions
        that are used to manage bank account
    """

    def deposit(amount):
        """this function adds the amount to the current balance"""
        dispatch['balance'] += amount
        return dispatch['balance']

    def withdraw(amount):
        """checks current balance and withdraw required amount"""
        if amount > dispatch['balance']:
            return 'Insufficient Funds'
        dispatch['balance'] -= amount
        return dispatch['balance']

    dispatch = {'deposit':  deposit,
                'withdraw': withdraw,
                'balance':  initial_balance}
    return dispatch


def withdraw(account, amount):
    return account['withdraw'](amount)


def deposit(account, amount):
    return account['deposit'](amount)


def check_balance(account):
    return account['balance']


mike = account(1000)
deposit(mike, 500)
print(check_balance(mike))
withdraw(mike, 700)
print(check_balance(mike))
