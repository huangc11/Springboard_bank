import datetime as dt
from utility import Utility as ut
from sqlalchemy import Column,  INTEGER, VARCHAR, FLOAT, DATE, or_
from sqlalchemy import exc
    #NoResultFound, MultipleResultsFound, IntegrityError

from sqlalchemy.ext.declarative import declarative_base
from  database import Database
from customer import Customer
import CustomerAccount as m_ca
Base = declarative_base()

class BankAccount(Base):
    ''' A class to represent a bank account'''

    checking_account_prefix =20000
    savings_account_prefix =30000

    __tablename__ = 'bankaccount'

    id = Column(INTEGER, primary_key=True)
    account_no = Column(INTEGER)
    account_type = Column(VARCHAR(30), nullable=False)
    balance = Column(FLOAT)
    intrst_rate = Column(FLOAT)
   # fee_limit = Column(FLOAT)
    cr_date = Column(DATE)

    def __init__(self, balance):
        self.balance=balance
        self.cr_date= dt.datetime.today()

      #  self.account_type =''
    '''def set_account_no(self,p_account_no):
        self.account_no =p_account_no'''

    def __repr__(self):
        return ("BankAccount({id}, {acc_no}, '{acc_type}', {balance})".
                format(id=self.id, acc_no=self.account_no, acc_type=self.account_type, balance=self.balance))

    def withdraw(self, p_amount):
        """ withraw month from this account

          Args:
            p_amount(float): amount to withdraw


        Returns:
            a tuple (a,b)
                 a: amount that being withdrawn
                 b: account's new balance
        """
        if p_amount<=0:
            return (0, self.balance)

        amt = min(self.balance, p_amount)
        self.balance -= amt
        return (amt, self.balance)

    def deposit(self, p_amount):
        """ deposit money to  this account
          Args:
            p_amount(float): amount to deposit. if p_amount<0 set p_amount = 0

          Returns:
            a tuple (a,b)
                 a: amount that being withdrawn
                 b: account's new balance

            if p
        """
        if p_amount>0:
            self.balance += p_amount
            return(p_amount, self.balance)

        else:
            return(0, self.balance)


    @staticmethod
    def get_prefix(p_acc_type='c'):
        if p_acc_type== 'c' or p_acc_type=='C' :
            return BankAccount.checking_account_prefix
        elif p_acc_type=='s' or p_acc_type=='s':
            return BankAccount.savings_account_prefix
        else:
            return 80000

    @staticmethod
    def seek_db_by_account_no(p_account_no):
        """search the account record in database by account_no; return id if succeed
          Args:
            p_account_no (str): account_no

        Returns:
            account object (if found) or None (not found)
        """
        try:
            session = Database.get_session()
            rec = session.query(BankAccount).\
                filter(BankAccount.account_no == p_account_no).\
                one()
            return rec

        except Exception as e:
            return None

    @staticmethod
    def seek_db_by_account_id(p_account_id):
        """search the account record in database by account_id;
          Args:
            p_account_no (str): account_id

        Returns:
            account object (if found) or None (not found)
        """
        try:
            session = Database.get_session()
            rec = session.query(BankAccount).\
                filter(BankAccount.id == p_account_id).\
                one()
            return rec
        except Exception as e:
            ut.log_exeption(e)
            return None

class SavingsAccount(BankAccount):
    ''' A class to represent a bank account'''
    max_intrst_rate = 0.02

    def __init__(self, balance=0, intrst_rate=0):
       BankAccount.__init__(self, balance)
       self.balance = balance
       self.intrst_rate =intrst_rate
       self.account_type = 'savings'

    def calc_interest(self, n_period=1):
        return self.balance*((1+ self.intrst.rate)**n_period-1)

class CheckingAccount(BankAccount):
    ''' A class to represent a bank account'''

    def __init__(self, balance=0):
       BankAccount.__init__(self, balance)
       self.account_type = 'checking'
       self.balance = balance

    def deposit(self, amount):
        self.balance += amount






def create_account(p_customer_id, p_account_type, p_balance=0, p_intrs_rate=0.01):
    """create account

      Args:
        p_customer_id(int): customer id
        p_balance(float): balance of the account
        p_account_type(str):   account type, ['checking', 'savings']

      Returns:
              Account id, if success
              None, if failure
    """
    o_customer = Customer.f_seek_db_by_id(p_customer_id)

    if o_customer ==None:
            ut.log_info('account creationng fails -- customer_id {}not found.'.format(p_customer_id))
            return None

        # Get the prefix for generationg account number:  checking - 20000,  savings = 30000
    o_account = CheckingAccount(p_balance) if p_account_type == 'c' else SavingsAccount(p_balance,p_intrs_rate)

    #create a record in database
    new_account = Database.new_rec_in_db(o_account)

        # account creation in database succeeds; generate account_no and update database
    if new_account == None: #if last step failed
        ut.log_info('Account creation fails -- save to db failed')
        return None

    #set account no
    new_account_no=new_account.id + BankAccount.get_prefix(p_account_type)


    result_upd =Database.update_rec_in_db(BankAccount, o_account.id, {"account_no": new_account_no})

    if result_upd == Database.const_fail:
        ut.log_info('Account creation failed -- update account_no at DB failed')
        return None

    o_cust_acc= m_ca.CustomerAccount(o_customer.id,  o_account.id)

    result_cust_acc = Database.new_rec_in_db(o_cust_acc)

    if result_cust_acc == None:
        ut.log_info('Account creation failed -- customer-account assignment failed')
        return None

    ut.log_info('Account (id ={}) successfully created and assgined to customer (id={}).'
                .format(o_account.id, o_customer.id))
    ut.log_info('\t {}'.format(o_account))
    ut.log_info('\t {}'.format(o_customer))
    return o_account



if __name__ == '__main__':
    Database.initialise()

    new_acc =create_account(100, 'c', 400)



  #  res =create_account(100, 's', 20000, 0.1)
   # print(res)#    s_account =  SavingsAccount(300)



 #   s_account.set_account_no(3396)


