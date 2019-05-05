import Ice
import Account

CURRENCIES = {
    'USD': Account.Currency.USD,
    'EUR': Account.Currency.EUR,
    'GBP': Account.Currency.GBP,
    'CHF': Account.Currency.CHF
}

class LoggedUser():

    def __init__(self, acc_type, setup):
        if acc_type == Account.Type.PREMIUM:
            self.account = Account.PremiumAccountPrx.checkedCast(setup)
        else:
            self.account = Account.StandardAccountPrx.checkedCast(setup)

    def balance(self):
        balance = self.account.getBalance()
        print('Your balance is %.2f' % (balance))

    def loan(self):
        try:
            cur = input('What currency do you want to take loan in? ')
            cur_enum = CURRENCIES[cur]
            amount = input('How much do you want to loan? ')

            res = self.account.getLoan(float(amount), cur_enum)
            print('%s %s will cost %.2f PLN' % (amount, cur, res))

        except Exception as e:
            print(e)

    def start(self):
        while True:
            a = input('What do you want to do? ')
            if a == 'balance':
                self.balance()
            if a == 'loan':
                self.loan()
            if a == 'quit':
                return


def login(proxy):
    try:
        pesel = input('PESEL: ')
        pwd = input('Password: ')

        res = proxy.login(pesel, pwd)
        user = LoggedUser(res.type, res.account)
        user.start()

    except Exception as e:
        print(e)


def register(proxy):
    try:
        name = input('Name: ')
        pesel = input('PESEL: ')
        income = float(input('Income (per month): '))

        res = proxy.registerAccount(name, pesel, income)
        print('{} account registered! Your password: {}'.format(str(res.type), res.pwd))

    except Exception as e:
        print(e)


def hmihy(proxy):
    while True:
        a = input('How may I help you?' )
        if a == 'register':
            register(proxy)
        if a == 'login':
            login(proxy)
        if a == 'quit':
            return


if __name__ == '__main__':
    with Ice.initialize() as account_interface:
        bank_meta = 'BankService:default -h 127.0.0.1 -p 12345'
        bank_setup = account_interface.stringToProxy(bank_meta)
        bank_proxy = Account.BankServicePrx.checkedCast(bank_setup)
        hmihy(bank_proxy)