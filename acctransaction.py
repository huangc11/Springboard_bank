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
        print("account_id:{}".format(self.account_id))
        print("account_no:{}".format(self.account_no))
        print("account_type:{}".format(self.account_type))
        print("balance:{}".format(self.balance))
        print("date_cr:{}".format(self.cr_date))
        print("intrst_rate:{}".format(self.intrst_rate))
        print("fee_limit:{}".format(self.fee_limit))

    def withdraw(self, amount):
        self.balance -= amount


    @staticmethod
    def seek_db_by_account_no(db, p_account_no):
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
            session = db.get_session()

            rec = session.query(BankAccount).\
                filter(BankAccount.account_no == p_account_no).\
                one()

            return (1, rec.account_id)
        except exc.NoResultFound:
            return (-1, '1.not found')
        except Exception as e:
            print(e)
            return (-2, 'unknown failure ')


    def new_in_db(self, p_session):
        """write this new customer to database

          Args:
            self : The first parameter.
            p_database (Database object):

          Returns:
            a tuple as follows:
                  (1, account_no), if success
                  (-1, 'account_no alread existing ; cancelled
                  (-2, 'db failure')
        """

        session = p_session

        try:
                #write this object  to database

                session.add(self)
                session.commit()


                # if succeed
                return (1, self.account_no)

        except exc.IntegrityError:
               session.rollback()
               ut.print_one('1.Fail-- record with this primary key value exists. ')
               return (-1, '1.Fail-- record with this primary key value exists. ')


        except Exception as e:
                #Other fail
                session.rollback()
                ut.print_one('2.operation failed:'.format(e))
                return (-2, 'operation failed:')



class SavingsAccount(BankAccount):
    ''' A class to represent a bank account'''
    max_intrst_rate = 0.02

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



def create_savings_account(p_db_session):

    #c_customer_no = input("Please enter customer_no: ")
    c_account_no = input("Please enter account_no: ")
    c_balance = int(input("Please enter balance: "))
    c_intrst_rate = float(input("Please enter intrst_rate: "))

    if c_intrst_rate > SavingsAccount.max_intrst_rate:
            c_intrst_rate = SavingsAccount.max_intrst_rate

    c_account = SavingsAccount(c_balance, c_intrst_rate)
    c_account.set_account_no(c_account_no)

    result = c_account.new_in_db(p_db_session)

    if result[0] > 0:
            print("%%%%%%%% account has been created %%%%%%%% ")
            print("         The account is: {} ".format(result[1]))
    elif result[0] == -1:
            print("%%%%%%%% Customer already exist. Creation failed %%%%%%%% ")
    else:
            print("%%%%%%%% Creation failed on%%%%%%%% ")




def create_checking_account(p_db_session):
    c_fee_limit = 0

    #c_customer_no = input("Please enter customer_no: ")
    c_account_no = input("Please enter account_no: ")
    c_balance = int(input("Please enter balance: "))
    c_fee_limit = float(input("Please enter  fee limit: "))

    c_account = CheckingAccount(c_balance, c_fee_limit)
    c_account.set_account_no(c_account_no)

    result = c_account.new_in_db(p_db_session)

    if result[0] > 0:
            print("%%%%%%%% account has been created %%%%%%%% ")
            print("         The account is: {} ".format(result[1]))
    elif result[0] == -1:
            print("%%%%%%%% Customer already exist. Creation failed %%%%%%%% ")
    else:
            print("%%%%%%%% Creation failed on%%%%%%%% ")


def test_1():

    chk_account = CheckingAccount(500)
    chk_account.set_account_no(20036)
    chk_account.pr_detail()

    result = chk_account.new_in_db(bank_db)
    ut.print_one('after new_in_db')
    chk_account.pr_detail()
    ut.print_one(result)

    '''
    
    
    result = s_account.new_in_db(bank_db)
    ut.print_one(result)
    
    #t1_res = BankAccount.seek_db_by_account_no(bank_db, 344)
    '''

if __name__ == '__main__':

    bank_db = Database()

    bank_db_session = bank_db.get_session()


    create_savings_account(bank_db_session)

#    s_account =  SavingsAccount(300)
 #   s_account.set_account_no(3396)





