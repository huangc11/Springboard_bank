import datetime as dt
from sqlalchemy import Column,  INTEGER, VARCHAR, FLOAT, DATE, or_
from sqlalchemy.ext.declarative import declarative_base
import database as db
Base = declarative_base()

class BankAccount(Base):
    ''' A class to represent a bank account'''

    __tablename__ = 'bankaccount'

    account_no = Column(INTEGER, primary_key=True)
    account_type = Column(VARCHAR(30), nullable=False)
    balance = Column(FLOAT)
    intrst_rate = Column(FLOAT)
    fee_limit = Column(FLOAT)
    cr_date = Column(DATE)

    def __init__(self, balance):
        self.balance=balance
        self.cr_date= dt.datetime.today()

      #  self.account_type =''

    def withdraw(self, amount):
        self.balance -= amount


class SavingsAccount(BankAccount):
    ''' A class to represent a bank account'''

    def __init__(self, balance, intrst_rate):
       BankAccount.__init__(balance)
       self.intrst_rate =intrst_rate
       self.account_type = 'savings'

    def calc_interest(self, n_period=1):
        return self.balance*((1+ self.intrst.rate)**n_period-1)



class CheckingAccount(BankAccount):
    ''' A class to represent a bank account'''

    def __init__(self, balance, fee_limit):
       BankAccount.__init__(balance)
       self.fee_limit =fee_limit
       self.account_type = 'checking'

    def deposit(self, amount):
        self.balance += amount


    def withdraw(self, amount, fee=0):
        if fee<=self.fee_limit:
            amount1 =amount-fee
        else:
            amount1 =amount -- self.fee_limit

        BankAccount.withdraw(self,amount1)



if __name__ == '__main__':

    db_url = "mysql+pymysql://chu:tree@localhost:3306/bank"
    bank_db = Database(db_url)




