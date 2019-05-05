module Account {
    enum Type{
        STANDARD = 1,
        PREMIUM = 2
    };

    enum Currency{
        USD = 1,
        EUR = 2,
        GBP = 3,
        CHF = 4
    };

    exception AuthenticationFailed{
        string reason;
    };
    exception RegistrationFailed{
        string reason;
    };
    exception LoanRejected{
        string reason;
    };


    interface StandardAccount{
        float getBalance();
    };

    interface PremiumAccount extends StandardAccount{
        float getLoan(float amount, Currency currency)
            throws LoanRejected;
    };


    struct RegisterResponse{
        Type type;
        string pwd;
    };

    struct LoginResponse{
        Type type;
        StandardAccount* account;
    };

    interface BankService {
        RegisterResponse registerAccount(string name, string pesel, float income)
            throws RegistrationFailed;
        LoginResponse login(string pesel, string pwd)
            throws AuthenticationFailed;
    };

};