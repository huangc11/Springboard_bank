import datetime as dt
from sqlalchemy import Column,  INTEGER, VARCHAR, FLOAT, DATETIME, or_, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base

from utility import Utility as ut
from database import Database
from customer import Customer
from bankaccount import BankAccount

Base = declarative_base()

'''
students_classes_association = Table('students_classes', Base.metadata,
    Column('student_id', INTEGER, ForeignKey('students.id')),
    Column('class_id', INTEGER, ForeignKey('classes.id'))
)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    classes = relationship("Class", secondary=students_classes_association)

class Class(Base):
    __tablename__ = 'classes'
    id = Column(Integer, primary_key=True)
'''

CustomerAccount_association = Table('customer_account1', Base.metadata,
    Column('customer_id', INTEGER, ForeignKey('customer.id')),
    Column('account_id', INTEGER, ForeignKey('bankaccount.id'))
)

class CustomerAccount(Base):
    ''' A class to represent a bank account transaction'''

    __tablename__ = 'customer_account'

    id = Column(INTEGER, primary_key=True)
    customer_id  = Column(INTEGER, ForeignKey('customer.id'))
    account_id = Column(INTEGER, ForeignKey('bankaccount.id'))
    cr_datetime = Column(DATETIME)


#recipe_id = Column(Integer, ForeignKey('recipes.id'))
    def __init__(self, customer_id , account_id):
        self.account_id=account_id
        self.customer_id = customer_id
        self.cr_datetime= dt.datetime.now()

    @staticmethod
    def connect_customer_account( customer_id, account_id):

           # search_result = Customer.seek_db_by_id(customer_id)

            record = CustomerAccount_association(customer_id, account_id)

            db_result= Database.new_rec_in_db(record)

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

