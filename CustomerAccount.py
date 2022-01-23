import datetime as dt
from sqlalchemy import Column,  INTEGER, VARCHAR, FLOAT, DATETIME, or_
from sqlalchemy.ext.declarative import declarative_base

from utility import Utility as ut
from database import Database
from bankaccount import BankAccount

Base = declarative_base()

class CustomerAccount(Base):
    ''' A class to represent a bank account transaction'''

    __tablename__ = 'customer_account'

    id = Column(INTEGER, primary_key=True)
    customer_id  = Column(INTEGER)
    account_id = Column(INTEGER)
    cr_datetime = Column(DATETIME)

    def __init__(self, customer_id , account_id):
        self.account_id=account_id
        self.customer_id = customer_id
        self.cr_datetime= dt.datetime.now()

    @staticmethod
    def connect_customer_account( customer_id, account_id):

            customer_acc_record = CustomerAccount(customer_id, account_id)

            db_result= Database.new_rec_in_db(customer_acc_record)

            # db creaton succeeds
            if db_result[0]==1:
                ut.print_success("Customer-account connection created.")
                ut.print_success("         The id is: {} ".format(db_result[1]))

            # db creaton fails
            else:
                ut.print_error("Customer-account connection failed.")

if __name__ =="__main__" :

    Database.initialise()
    CustomerAccount.connect_customer_account(customer_id=100,account_id =200 )
    #ut.print_success('succ!')

