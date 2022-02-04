
from utility import glb_logger



import datetime as dt

from database import Database
from bankaccount import BankAccount
from acctransaction import AccountTransaction

from utility import Utility as ut


def log_app_info(msg):
    #ut.logger_app.info(msg)
    glb_logger.info(msg)


def withdraw_from_account(p_account_no, p_amount):

    o_account = BankAccount.get_by_account_no(p_account_no)

    #if account not found
    if o_account == None:
        ut.logger_app.info("Withdrawal transaction failed -- account not found.")

    # Withdraw from the account: get the actual amount withdrawn and new balance
    amount_withdraw = o_account.withdraw(p_amount)
    #Create the transasction record

    transaction =AccountTransaction(account_no=p_account_no, type='withdraw', amount=amount_withdraw[0])
    new_trans = Database.new_rec_in_db(transaction)

    #if new transsation  in database failed
    if new_trans == None:
        log_app_info('Withdraw transaction failed -- can not create transaction record')
        return None

    #new transsation in database succeed
    log_app_info('Withdraw transaction succeeded')
    log_app_info("Transaction id: {}; amount withdrawn: {} account balance: {} ".\
                             format(new_trans.account_no, amount_withdraw[0], amount_withdraw[1]))

    return new_trans