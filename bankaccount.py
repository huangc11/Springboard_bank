import datetime as dt
from utility import Utility as ut
from sqlalchemy import Column,  INTEGER, VARCHAR, FLOAT, DATE, or_
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from sqlalchemy.ext.declarative import declarative_base
from  database import Database
Base = declarative_base()

class BankAccount(Base):
    ''' A class to represent a bank account'''

    __tablename__ = 'bankaccount'

    account_id = Column(INTEGER, primary_key=True)
    account_no = Column(INTEGER)
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




    @staticmethod
    def seek_by_account_no(db, p_account_no):
        """search the account record in database by account_no; return account_id if succeed

          Args:
            db (Database): a Database object
            p_account_no (str): account_no

        Returns:
            a tuple which could have following values:
                 (1, acount_no)  -- one found
                 (-1, 'no one found') -- fail
                 (-2, 'unknown failure') -- fail
        """

        try:
            session = db.get_session()

            rec = session.query(BankAccount).\
                filter(BankAccount.account_no == p_account_no).\
                one()

            return (1, rec.account_id)
        except NoResultFound:
            return (-1, '1.not found')
        except Exception as e:
            print(e)
            return (-2, 'unknown failure ')

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

    bank_db = Database()

        #bank_db.get_session()

    print('**********************************')

    result = BankAccount.seek_by_account_no(bank_db, 34456)
    ut.print_one(result)



