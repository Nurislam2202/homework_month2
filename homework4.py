class Stock:
    pass

class Bond:
    pass

class SavingAccount:
    pass

class CheckingAccount:
    pass

class RealEstate:
    pass

class Security(Stock, Bond):
    pass

class BankAccount(SavingAccount, CheckingAccount):
    pass

class InterestBearingItem(Security, BankAccount):
    pass

class Asset(RealEstate, BankAccount, Security):
    pass

class InsurableItem(BankAccount, RealEstate):
    pass
