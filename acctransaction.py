import datetime as dt
from sqlalchemy import Column,  INTEGER, VARCHAR, FLOAT, DATE, or_
from sqlalchemy.ext.declarative import declarative_base

from database import Database
from bankaccount import BankAccount

from utility import Utility as ut


Base = declarative_base()

class AccountTransaction(Base):
    ''' A class to represent a bank account transaction'''

    __tablename__ = 'acc_transaction'

    id = Column(INTEGER, primary_key=True)
    account_no = Column(INTEGER)
    type = Column(VARCHAR(30), nullable=False)
    amount = Column(FLOAT)
    cr_date = Column(DATE)

    def __init__(self, account_no, type, amount):
        self.account_no=account_no
        self.type=type
        self.amount=amount
        self.cr_date= dt.datetime.today()

        def deposit_to_account(p_account_no, p_amount):

            o_account = BankAccount.get_by_account_no(p_account_no)

            # if account not found
            if o_account == None:
                ut.logger_app.info("Deposit transaction failed -- account not found.")

            deposit_result = o_account.deposit(p_amount)

            new_trans = AccountTransaction(account_no=p_account_no, type='deposit', amount=p_amount)
            db_result = Database.new_rec_in_db(new_trans)

            if new_trans == None:
                log_app_info('Deposit transaction failed -- can not create transaction record')
                return None

                # new transsation in database succeed
            log_app_info('Deposit transaction succeeded')
            log_app_info("Transaction id: {}; amount deposited: {}; account balance: {} ". \
                         format(new_trans.id, new_trans.amount, deposit_result[1]))

            return new_trans

        # db creaton succeeds



if __name__ =="__main__" :

    Database.initialise()
    deposit_to_account(20172, 25)
    #print(result)
    #deposit_to_account()