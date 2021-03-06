# -*- coding: utf-8 -*-
# **********************************************************************
#
# Copyright (c) 2003-2017 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************
#
# Ice version 3.7.0
#
# <auto-generated>
#
# Generated from file `Account.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy

# Start of module Account
_M_Account = Ice.openModule('Account')
__name__ = 'Account'

if 'Type' not in _M_Account.__dict__:
    _M_Account.Type = Ice.createTempClass()
    class Type(Ice.EnumBase):

        def __init__(self, _n, _v):
            Ice.EnumBase.__init__(self, _n, _v)

        def valueOf(self, _n):
            if _n in self._enumerators:
                return self._enumerators[_n]
            return None
        valueOf = classmethod(valueOf)

    Type.STANDARD = Type("STANDARD", 1)
    Type.PREMIUM = Type("PREMIUM", 2)
    Type._enumerators = { 1:Type.STANDARD, 2:Type.PREMIUM }

    _M_Account._t_Type = IcePy.defineEnum('::Account::Type', Type, (), Type._enumerators)

    _M_Account.Type = Type
    del Type

if 'Currency' not in _M_Account.__dict__:
    _M_Account.Currency = Ice.createTempClass()
    class Currency(Ice.EnumBase):

        def __init__(self, _n, _v):
            Ice.EnumBase.__init__(self, _n, _v)

        def valueOf(self, _n):
            if _n in self._enumerators:
                return self._enumerators[_n]
            return None
        valueOf = classmethod(valueOf)

    Currency.USD = Currency("USD", 1)
    Currency.EUR = Currency("EUR", 2)
    Currency.GBP = Currency("GBP", 3)
    Currency.CHF = Currency("CHF", 4)
    Currency._enumerators = { 1:Currency.USD, 2:Currency.EUR, 3:Currency.GBP, 4:Currency.CHF }

    _M_Account._t_Currency = IcePy.defineEnum('::Account::Currency', Currency, (), Currency._enumerators)

    _M_Account.Currency = Currency
    del Currency

if 'AuthenticationFailed' not in _M_Account.__dict__:
    _M_Account.AuthenticationFailed = Ice.createTempClass()
    class AuthenticationFailed(Ice.UserException):
        def __init__(self, reason=''):
            self.reason = reason

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_id = '::Account::AuthenticationFailed'

    _M_Account._t_AuthenticationFailed = IcePy.defineException('::Account::AuthenticationFailed', AuthenticationFailed, (), False, None, (('reason', (), IcePy._t_string, False, 0),))
    AuthenticationFailed._ice_type = _M_Account._t_AuthenticationFailed

    _M_Account.AuthenticationFailed = AuthenticationFailed
    del AuthenticationFailed

if 'RegistrationFailed' not in _M_Account.__dict__:
    _M_Account.RegistrationFailed = Ice.createTempClass()
    class RegistrationFailed(Ice.UserException):
        def __init__(self, reason=''):
            self.reason = reason

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_id = '::Account::RegistrationFailed'

    _M_Account._t_RegistrationFailed = IcePy.defineException('::Account::RegistrationFailed', RegistrationFailed, (), False, None, (('reason', (), IcePy._t_string, False, 0),))
    RegistrationFailed._ice_type = _M_Account._t_RegistrationFailed

    _M_Account.RegistrationFailed = RegistrationFailed
    del RegistrationFailed

if 'LoanRejected' not in _M_Account.__dict__:
    _M_Account.LoanRejected = Ice.createTempClass()
    class LoanRejected(Ice.UserException):
        def __init__(self, reason=''):
            self.reason = reason

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_id = '::Account::LoanRejected'

    _M_Account._t_LoanRejected = IcePy.defineException('::Account::LoanRejected', LoanRejected, (), False, None, (('reason', (), IcePy._t_string, False, 0),))
    LoanRejected._ice_type = _M_Account._t_LoanRejected

    _M_Account.LoanRejected = LoanRejected
    del LoanRejected

_M_Account._t_StandardAccount = IcePy.defineValue('::Account::StandardAccount', Ice.Value, -1, (), False, True, None, ())

if 'StandardAccountPrx' not in _M_Account.__dict__:
    _M_Account.StandardAccountPrx = Ice.createTempClass()
    class StandardAccountPrx(Ice.ObjectPrx):

        def getBalance(self, context=None):
            return _M_Account.StandardAccount._op_getBalance.invoke(self, ((), context))

        def getBalanceAsync(self, context=None):
            return _M_Account.StandardAccount._op_getBalance.invokeAsync(self, ((), context))

        def begin_getBalance(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_Account.StandardAccount._op_getBalance.begin(self, ((), _response, _ex, _sent, context))

        def end_getBalance(self, _r):
            return _M_Account.StandardAccount._op_getBalance.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_Account.StandardAccountPrx.ice_checkedCast(proxy, '::Account::StandardAccount', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_Account.StandardAccountPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::Account::StandardAccount'
    _M_Account._t_StandardAccountPrx = IcePy.defineProxy('::Account::StandardAccount', StandardAccountPrx)

    _M_Account.StandardAccountPrx = StandardAccountPrx
    del StandardAccountPrx

    _M_Account.StandardAccount = Ice.createTempClass()
    class StandardAccount(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Account::StandardAccount', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Account::StandardAccount'

        @staticmethod
        def ice_staticId():
            return '::Account::StandardAccount'

        def getBalance(self, current=None):
            raise NotImplementedError("servant method 'getBalance' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_Account._t_StandardAccountDisp)

        __repr__ = __str__

    _M_Account._t_StandardAccountDisp = IcePy.defineClass('::Account::StandardAccount', StandardAccount, (), None, ())
    StandardAccount._ice_type = _M_Account._t_StandardAccountDisp

    StandardAccount._op_getBalance = IcePy.Operation('getBalance', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), IcePy._t_float, False, 0), ())

    _M_Account.StandardAccount = StandardAccount
    del StandardAccount

_M_Account._t_PremiumAccount = IcePy.defineValue('::Account::PremiumAccount', Ice.Value, -1, (), False, True, None, ())

if 'PremiumAccountPrx' not in _M_Account.__dict__:
    _M_Account.PremiumAccountPrx = Ice.createTempClass()
    class PremiumAccountPrx(_M_Account.StandardAccountPrx):

        def getLoan(self, amount, currency, context=None):
            return _M_Account.PremiumAccount._op_getLoan.invoke(self, ((amount, currency), context))

        def getLoanAsync(self, amount, currency, context=None):
            return _M_Account.PremiumAccount._op_getLoan.invokeAsync(self, ((amount, currency), context))

        def begin_getLoan(self, amount, currency, _response=None, _ex=None, _sent=None, context=None):
            return _M_Account.PremiumAccount._op_getLoan.begin(self, ((amount, currency), _response, _ex, _sent, context))

        def end_getLoan(self, _r):
            return _M_Account.PremiumAccount._op_getLoan.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_Account.PremiumAccountPrx.ice_checkedCast(proxy, '::Account::PremiumAccount', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_Account.PremiumAccountPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::Account::PremiumAccount'
    _M_Account._t_PremiumAccountPrx = IcePy.defineProxy('::Account::PremiumAccount', PremiumAccountPrx)

    _M_Account.PremiumAccountPrx = PremiumAccountPrx
    del PremiumAccountPrx

    _M_Account.PremiumAccount = Ice.createTempClass()
    class PremiumAccount(_M_Account.StandardAccount):

        def ice_ids(self, current=None):
            return ('::Account::PremiumAccount', '::Account::StandardAccount', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Account::PremiumAccount'

        @staticmethod
        def ice_staticId():
            return '::Account::PremiumAccount'

        def getLoan(self, amount, currency, current=None):
            raise NotImplementedError("servant method 'getLoan' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_Account._t_PremiumAccountDisp)

        __repr__ = __str__

    _M_Account._t_PremiumAccountDisp = IcePy.defineClass('::Account::PremiumAccount', PremiumAccount, (), None, (_M_Account._t_StandardAccountDisp,))
    PremiumAccount._ice_type = _M_Account._t_PremiumAccountDisp

    PremiumAccount._op_getLoan = IcePy.Operation('getLoan', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_float, False, 0), ((), _M_Account._t_Currency, False, 0)), (), ((), IcePy._t_float, False, 0), (_M_Account._t_LoanRejected,))

    _M_Account.PremiumAccount = PremiumAccount
    del PremiumAccount

if 'RegisterResponse' not in _M_Account.__dict__:
    _M_Account.RegisterResponse = Ice.createTempClass()
    class RegisterResponse(object):
        def __init__(self, type=_M_Account.Type.STANDARD, pwd=''):
            self.type = type
            self.pwd = pwd

        def __hash__(self):
            _h = 0
            _h = 5 * _h + Ice.getHash(self.type)
            _h = 5 * _h + Ice.getHash(self.pwd)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_Account.RegisterResponse):
                return NotImplemented
            else:
                if self.type is None or other.type is None:
                    if self.type != other.type:
                        return (-1 if self.type is None else 1)
                else:
                    if self.type < other.type:
                        return -1
                    elif self.type > other.type:
                        return 1
                if self.pwd is None or other.pwd is None:
                    if self.pwd != other.pwd:
                        return (-1 if self.pwd is None else 1)
                else:
                    if self.pwd < other.pwd:
                        return -1
                    elif self.pwd > other.pwd:
                        return 1
                return 0

        def __lt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r < 0

        def __le__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r <= 0

        def __gt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r > 0

        def __ge__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r >= 0

        def __eq__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r == 0

        def __ne__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r != 0

        def __str__(self):
            return IcePy.stringify(self, _M_Account._t_RegisterResponse)

        __repr__ = __str__

    _M_Account._t_RegisterResponse = IcePy.defineStruct('::Account::RegisterResponse', RegisterResponse, (), (
        ('type', (), _M_Account._t_Type),
        ('pwd', (), IcePy._t_string)
    ))

    _M_Account.RegisterResponse = RegisterResponse
    del RegisterResponse

if 'LoginResponse' not in _M_Account.__dict__:
    _M_Account.LoginResponse = Ice.createTempClass()
    class LoginResponse(object):
        def __init__(self, type=_M_Account.Type.STANDARD, account=None):
            self.type = type
            self.account = account

        def __eq__(self, other):
            if other is None:
                return False
            elif not isinstance(other, _M_Account.LoginResponse):
                return NotImplemented
            else:
                if self.type != other.type:
                    return False
                if self.account != other.account:
                    return False
                return True

        def __ne__(self, other):
            return not self.__eq__(other)

        def __str__(self):
            return IcePy.stringify(self, _M_Account._t_LoginResponse)

        __repr__ = __str__

    _M_Account._t_LoginResponse = IcePy.defineStruct('::Account::LoginResponse', LoginResponse, (), (
        ('type', (), _M_Account._t_Type),
        ('account', (), _M_Account._t_StandardAccountPrx)
    ))

    _M_Account.LoginResponse = LoginResponse
    del LoginResponse

_M_Account._t_BankService = IcePy.defineValue('::Account::BankService', Ice.Value, -1, (), False, True, None, ())

if 'BankServicePrx' not in _M_Account.__dict__:
    _M_Account.BankServicePrx = Ice.createTempClass()
    class BankServicePrx(Ice.ObjectPrx):

        def registerAccount(self, name, pesel, income, context=None):
            return _M_Account.BankService._op_registerAccount.invoke(self, ((name, pesel, income), context))

        def registerAccountAsync(self, name, pesel, income, context=None):
            return _M_Account.BankService._op_registerAccount.invokeAsync(self, ((name, pesel, income), context))

        def begin_registerAccount(self, name, pesel, income, _response=None, _ex=None, _sent=None, context=None):
            return _M_Account.BankService._op_registerAccount.begin(self, ((name, pesel, income), _response, _ex, _sent, context))

        def end_registerAccount(self, _r):
            return _M_Account.BankService._op_registerAccount.end(self, _r)

        def login(self, pesel, pwd, context=None):
            return _M_Account.BankService._op_login.invoke(self, ((pesel, pwd), context))

        def loginAsync(self, pesel, pwd, context=None):
            return _M_Account.BankService._op_login.invokeAsync(self, ((pesel, pwd), context))

        def begin_login(self, pesel, pwd, _response=None, _ex=None, _sent=None, context=None):
            return _M_Account.BankService._op_login.begin(self, ((pesel, pwd), _response, _ex, _sent, context))

        def end_login(self, _r):
            return _M_Account.BankService._op_login.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_Account.BankServicePrx.ice_checkedCast(proxy, '::Account::BankService', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_Account.BankServicePrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::Account::BankService'
    _M_Account._t_BankServicePrx = IcePy.defineProxy('::Account::BankService', BankServicePrx)

    _M_Account.BankServicePrx = BankServicePrx
    del BankServicePrx

    _M_Account.BankService = Ice.createTempClass()
    class BankService(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Account::BankService', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Account::BankService'

        @staticmethod
        def ice_staticId():
            return '::Account::BankService'

        def registerAccount(self, name, pesel, income, current=None):
            raise NotImplementedError("servant method 'registerAccount' not implemented")

        def login(self, pesel, pwd, current=None):
            raise NotImplementedError("servant method 'login' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_Account._t_BankServiceDisp)

        __repr__ = __str__

    _M_Account._t_BankServiceDisp = IcePy.defineClass('::Account::BankService', BankService, (), None, ())
    BankService._ice_type = _M_Account._t_BankServiceDisp

    BankService._op_registerAccount = IcePy.Operation('registerAccount', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0), ((), IcePy._t_float, False, 0)), (), ((), _M_Account._t_RegisterResponse, False, 0), (_M_Account._t_RegistrationFailed,))
    BankService._op_login = IcePy.Operation('login', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0)), (), ((), _M_Account._t_LoginResponse, False, 0), (_M_Account._t_AuthenticationFailed,))

    _M_Account.BankService = BankService
    del BankService

# End of module Account
