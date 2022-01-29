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
    def set_account_no(self,p_account_no):
        self.account_no =p_account_no

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

    def pr_detail(self):
        ut.print_one("account info ")
        print("account_id:{}".format(self.id))
        print("account_no:{}".format(self.account_no))
        print("account_type:{}".format(self.account_type))
        print("balance:{}".format(self.balance))
        print("date_cr:{}".format(self.cr_date))
        print("intrst_rate:{}".format(self.intrst_rate))

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
    def seek_db_by_account_no(p_account_no):
        """search the account record in database by account_no; return id if succeed

          Args:
            p_account_no (str): account_no

        Returns:
            a tuple which could have following values:
                 (1, the founded bankaccount object)  -- one found
                 (-1, 'no one found') -- fail
                 (-2, 'unknown failure') -- fail
        """

        try:
            session = Database.get_session()

            rec = session.query(BankAccount).\
                filter(BankAccount.account_no == p_account_no).\
                one()

            return (1,  rec)
        except exc.NoResultFound:
            return (-1, '1.not found')
        except Exception as e:
            print(e)
            return (-2, 'unknown failure ')


    def create_account_db(self, c_customer_no=None):

        obj_account = self
        obj_account.account_no = -1
        ut.print_one('obj_account')
        obj_account.pr_detail()


        # Get the prefix for generationg account number:  checking - 20000,  savings = 30000
        if self.account_type== 'checking':
            tmp_prefix= BankAccount.checking_account_prefix
        else:
            tmp_prefix = BankAccount.savings_account_prefix

        #create a record in database
        result = Database.new_rec_in_db(obj_account)

        # account creation in database succeeds; generate account_no and update database
        if result[0] > 0:
            tmp_account_id = result[1]
            tmp_account_no = tmp_account_id +tmp_prefix
            obj_account.set_account_no(tmp_account_no)

            try:
                Database.update_rec_in_db(BankAccount, tmp_account_id, {"account_no": tmp_account_no})
                ut.print_success("Account has been created")
                ut.print_success(" The account_no is: {} ".format(tmp_account_no))
            except Exception as e:
                ut.print_error("Account creation failed")
                ut.print_error(e)
                ut.print_error("")

        elif result[0] == -1:
            ut.print_error("Account creation failed due to duplicated account_id or account_no")
        else:
            ut.print_error("Account Creation failed. Possibly due to database errors")







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

    def __init__(self, balance):
       BankAccount.__init__(self, balance)
       self.account_type = 'checking'
       self.balance = balance

    def deposit(self, amount):
        self.balance += amount


'''
def create_account(acc_type ):
    def collect_info_for_savings():
        #c_customer_no = input("Please enter customer_no: ")
        c_balance = int(input("Please enter balance: "))
        c_intrst_rate = float(input("Please enter intrst_rate: "))

        if c_intrst_rate > SavingsAccount.max_intrst_rate:
                c_intrst_rate = SavingsAccount.max_intrst_rate

    def collect_info_for_checking():
        #c_customer_no = input("Please enter customer_no: ")
        c_balance = int(input("Please enter balance: "))

    collect_for_savings()
    o_account = SavingsAccount(c_balance, c_intrst_rate)
    o_account.set_account_no(2)


'''


#def create_account(o_account, c_customer_no):
 #   result =Database.new_rec_in_db(o_account)
  #  ut.print_one(result)



def create_checking_account():

    #c_customer_no = input("Please enter customer_no: ")
    c_balance = int(input("Please enter balance: "))
    c_account = CheckingAccount(c_balance)
    result = c_account.create_account_db()



'''
    if result[0] > 0:

            #set accout_no = 30000 + account_id
            new_account_no = BankAccount.checking_account_prefix + result[1]


            ut.print_success("account has been created")
            ut.print_success(" The account id is: {} ".format(result[1]))

    elif result[0] == -1:
            print("%%%%%%%% account with same account_no already exist. Creation failed %%%%%%%% ")
    else:
            print("%%%%%%%% Creation failed on%%%%%%%% ")

'''


if __name__ == '__main__':
    Database.initialise()


    create_checking_account()
#    s_account =  SavingsAccount(300)
 #   s_account.set_account_no(3396)


