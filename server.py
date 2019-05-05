import time
import math
import threading
import sys
import grpc
import random
sys.path.append('/Library/Python/2.7/site-packages')
import Account, Ice
sys.path.append('./grpc')
import currency_pb2, currency_pb2_grpc

CURRENCIES = {
    'USD': currency_pb2.USD,
    'EUR': currency_pb2.EUR,
    'GBP': currency_pb2.GBP,
    'CHF': currency_pb2.CHF
}
used_currencies = {}


def make_bank_info():
    b = currency_pb2.BankInfo()
    b.otherCurrency[:] = used_currencies.keys()
    return b


def currency_service():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = currency_pb2_grpc.CurrenciesStub(channel)
        try:
            for res in stub.register(make_bank_info()):
                used_currencies[res.currency] = res.value
        except grpc._channel._Rendezvous as e:
            print(e)


class StandardAccountI(Account.StandardAccountI):

    def __init__(self, name, pesel, income, pwd, acc_type):
        self.name = name
        self.pesel = pesel 
        self.pwd = pwd
        self.income = income
        self.acc_type = acc_type
        self.balance = income * random.random() * 10

    def getBalance(self, current):
        return self.balance


class PremiumAccountI(Account.PremiumAccountI, StandardAccountI):

    # TODO
    def is_currency_supported(currency):
        return True

    def getLoan(self, amount, currency, current):
        if amount <= 0:
            raise LoanRejected(
                'Loan rejected: Negative amount.'
            )
        if not is_currency_supported:
            raise LoanRejected(
                'Loan rejected: The bank does not support this currency.'
            )
        print(str(c))
        curr = CURRENCIES[str(c)]
        return amount * used_currencies[curr]
        

class BankServiceI(Account.BankService):

    def __init__(self, interface, adapter):
        self.interface = interface
        self.adapter = adapter
        self.accounts = {}

    def generate_password():
        return 'admin1'

    def registerAccount(self, name, pesel, income, current=None):
        if pesel in self.accounts.keys():
            raise Account.RegistrationFailed(
                'Registration failed: PESEL is already in use.')
        if income < 0:
            raise Account.RegistrationFailed(
                'Registration failed: Negative income.')
        pwd = self.generate_password()
        if income > 5000:
            acc_type = Account.Type.PREMIUM
            account = PremiumAccountI(name, pesel, income, pwd, acc_type)
        else:
            acc_type = Account.Type.STANDARD
            account = StandardAccountI(name, pesel, income, pwd, acc_type)
        self.accounts[pesel] = account
        self.adapter.add(account,
            self.interface.stringToIdentity(pesel + str(acc_type)))
        print('Registered %s as %s' % (pesel, str(acc_type)))
        return Account.RegisterResponse(acc_type, pwd)

    def are_credentials_correct(self, pesel, pwd):
        if pesel in self.accounts.keys():
            if self.accounts[pesel].pwd == pwd:
                return True
        return False

    def login(self, pesel, pwd, current=None):
        if not are_credentials_correct(pesel, pwd):
            raise Account.AuthenticationFailed(
                'Authentication Failed: Wrong PESEL or password')
        acc_type = self.accounts[pesel].acc_type
        setup = current.adapter.createProxy(Ice.stringToIdentity(
            pesel + str(acc_type)))
        if(acc_type == Account.Type.PREMIUM):
            new =  Account.PremiumAccountPrx.uncheckedCast(base)
        else:
            new = Account.StandardAccountPrx.uncheckedCast(base)
        return Account.LoginResponse(acc_type, new)


if __name__ == '__main__':
    i = int(input('How many currencies do I use? '))
    while i > 0:
        c = input('Currency (%d left): ' % i)
        used_currencies[CURRENCIES[c]] = 0.0
        i -= 1
    currency_service_thread = threading.Thread(target=currency_service)
    currency_service_thread.start()

    with Ice.initialize(sys.argv) as bank_interface:
        adapter = bank_interface.createObjectAdapterWithEndpoints(
            'BankAdapter', 'default -h 127.0.0.1 -p 12345')
        bank_service = BankServiceI(bank_interface, adapter)
        adapter.add(bank_service, bank_interface.stringToIdentity('BankService'))
        adapter.activate()
        bank_interface.waitForShutdown()
