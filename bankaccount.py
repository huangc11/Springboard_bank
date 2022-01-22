import datetime as dt
from utility import Utility as ut
from sqlalchemy import Column,  INTEGER, VARCHAR, FLOAT, DATE, or_
from sqlalchemy import exc
    #NoResultFound, MultipleResultsFound, IntegrityError

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
    def set_account_no(self,p_account_no):
        self.account_no =p_account_no

    def pr_detail(self):
        ut.print_one("account info ")
        print("account_no:{}".format(self.account_no))
        print("account_type:{}".format(self.account_type))
        print("balance:{}".format(self.balance))
        print("date_cr:{}".format(self.cr_date))
        print("intrst_rate:{}".format(self.intrst_rate))
        print("fee_limit:{}".format(self.fee_limit))

    def withdraw(self, amount):
        self.balance -= amount


    @staticmethod
    def seek_db_by_account_no(db_class, p_account_no):
        """search the account record in database by account_no; return account_id if succeed

          Args:
            db (Database): a Database object
            p_account_no (str): account_no

        Returns:
            a tuple which could have following values:
                 (1, acount_id)  -- one found
                 (-1, 'no one found') -- fail
                 (-2, 'unknown failure') -- fail
        """

        try:
            session = db_class.get_session1()


            rec = session.query(BankAccount).\
                filter(BankAccount.account_no == p_account_no).\
                one()

            ut.print_one(rec)
            return (1, rec.account_id)
        except exc.NoResultFound:
            return (-1, '1.not found')
        except Exception as e:
            print(e)
            return (-2, 'unknown failure ')


    def new_in_db(self, p_database):
        """write this new customer to database

          Args:
            self : The first parameter.
            p_database (Database object):

          Returns:
            a tuple as follows:
                  (1, None), if success
                  (-1, 'customer already exist so action cancelled
                  -2, other failure
        """

        try:
                #write this object  to database
                session = p_database.get_session()
                session.add(self)
                session.commit()

                # if succeed
                return (1, None)

        except exc.IntegrityError:
               session.rollback()
               return (-1, '1.Operation failed -- Account_no already existed. ')


        except Exception as e:
                #Other fail
                session.rollback()
                ut.print_one('2.1.Operation failed -- Unkown error. ')
                return -2



class SavingsAccount(BankAccount):
    ''' A class to represent a bank account'''

    def __init__(self, balance, intrst_rate=0):
       BankAccount.__init__(self, balance)
       self.balance = balance
       self.intrst_rate =intrst_rate
       self.account_type = 'savings'

    def calc_interest(self, n_period=1):
        return self.balance*((1+ self.intrst.rate)**n_period-1)

class CheckingAccount(BankAccount):
    ''' A class to represent a bank account'''

    def __init__(self, balance, fee_limit=0):
       BankAccount.__init__(self, balance)
       self.account_type = 'checking'
       self.balance = balance
       self.fee_limit = fee_limit


if __name__ == '__main__':

    bank_db = Database()
    ut.print_one(Database.get_session1())
    t1_res = BankAccount.seek_db_by_account_no(Database, 20001)

    ut.print_one(t1_res)

#    s_account =  SavingsAccount(300)
 #   s_account.set_account_no(3396)

'''
    chk_account =  CheckingAccount(1999)
    chk_account.set_account_no(20002)
    chk_account.pr_detail()

    result = chk_account.new_in_db(bank_db)


  
   

    result = s_account.new_in_db(bank_db)
    ut.print_one(result)
  '''







