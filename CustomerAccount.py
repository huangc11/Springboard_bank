import datetime as dt
from sqlalchemy import Column,  INTEGER, VARCHAR, FLOAT, DATETIME, or_, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base

from utility import Utility as ut
from database import Database
from customer import Customer
import bankaccount as m_ba

Base = declarative_base()



class CustomerAccount(Base):
    ''' A class to represent a bank account transaction'''

    __tablename__ = 'a_customer_account'

    id = Column(INTEGER, primary_key=True)
    customer_id  = Column(INTEGER)
    account_id = Column(INTEGER)
    cr_datetime = Column(DATETIME)


#recipe_id = Column(Integer, ForeignKey('recipes.id'))
    def __init__(self, customer_id , account_id):
        self.account_id=account_id
        self.customer_id = customer_id
        self.cr_datetime= dt.datetime.now()

    @staticmethod
    def connect_customer_account( customer_id, account_id):

            if  Customer.f_seek_db_by_id(customer_id)==None:
                ut.log_info("Customer-account connection: ({}, {}) failed-- customer_id not found".
                            format(customer_id, account_id))
                return None

            if  m_ba.BankAccount.seek_db_by_account_id(account_id)==None:
                ut.log_info("Customer-account connection: ({}, {}) failed-- account_id not found".
                            format(customer_id, account_id))
                return None

            record = CustomerAccount(customer_id, account_id)

            db_result= Database.new_rec_in_db(record)

            print( db_result)

            # db creaton succeeds
            if db_result!=None:
                msg ="Customer-account connection: ({}, {}) created.".format(customer_id,account_id)
                print(msg)
                ut.log_info("Customer-account connection: ({}, {}) created.".format(customer_id,account_id))

            # db creaton fails
            else:
                ut.log_info("Customer-account connection: ({}, {}) failed.".format(customer_id, account_id))


if __name__ =="__main__" :

    Database.initialise()
    CustomerAccount.connect_customer_account(customer_id=101,account_id =104)
    #ut.print_success('succ!')

