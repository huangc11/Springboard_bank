import datetime as dt
from sqlalchemy import Column,  INTEGER, VARCHAR, FLOAT, DATE, or_
from sqlalchemy.ext.declarative import declarative_base

from utility import Utility as ut
from database import Database
from bankaccount import BankAccount

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

def withdraw_from_account():

    ut.print_one('Withdrawal Transaction')
    c_account_no = input("Please enter account_no: ")
    c_amount = int(input("Please enter amount to withdraw: "))
    c_account_type ="withdraw"

    seek_result = BankAccount.seek_db_by_account_no(c_account_no)


    #if record with specified account_no not found, abort
    if seek_result[0] == -1:
        ut.print_error("Account with this account_no was not found. Transaction failed.")

    # if record with specified account_no found, proceed
    elif seek_result[0] == 1:
        o_account = seek_result[1]
        withdraw_result = o_account.withdraw(c_amount)
        transaction =AccountTransaction(account_no=c_account_no, type='withdraw', amount=withdraw_result[0])
        db_result = Database.new_rec_in_db(transaction)

        # db creaton succeeds
        if  db_result[0] == 1:
            ut.print_success("Transaction succeeded")
            ut.print_success("Transaction id: {}; amount withdrawn: {} account balance: {} ".\
                             format(db_result[1], withdraw_result[0], withdraw_result[1]))

        # db creaton fails
        else:
            ut.print_error("Transaction failed, possibly due to database errors. ")

    # if search failed abort
    else:
            ut.print_error("Transaction failed.")

def deposit_to_account():
        ut.print_one('Deposit Transaction')
        c_account_no = input("Please enter account_no: ")
        c_amount = int(input("Please enter amount to deposit: "))
        c_account_type = "deposit"

        seek_result = BankAccount.seek_db_by_account_no(c_account_no)

        # if record with specified account_no not found, abort
        if seek_result[0] == -1:
            ut.print_error("Account with this account_no was not found. Transaction failed.")

        # if record with specified account_no found, proceed
        elif seek_result[0] == 1:
            o_account = seek_result[1]
            deposit_result =o_account.deposit(c_amount)
            ut.print_one(deposit_result)

            transaction = AccountTransaction(account_no=c_account_no, type='deposit', amount=c_amount)
            db_result = Database.new_rec_in_db(transaction)

            # db creaton succeeds
            if db_result[0] == 1:
                ut.print_success("Transaction succeeded")
                ut.print_success("Transaction id: {}; amount deposited: {}; account balance: {} ".\
                                 format(db_result[1], transaction.amount, deposit_result[1]))

            # db creaton fails
            else:
                ut.print_error("Transaction failed, possibly due to database errors. ")

        # if search failed abort
        else:
            ut.print_error("Transaction failed.")


if __name__ =="__main__" :

    Database.initialise()

    withdraw_from_account()
    #deposit_to_account()