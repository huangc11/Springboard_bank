
from database import Database
from customer import Customer
from bankaccount import create_account
import bankaccount as bkacc
import pytest


Database.initialise()

#create_account(p_customer_id, p_account_type='checking', p_balance=0, p_intrs_rate=0.01):
def test_create_account():
    pass

    '''

    result = bkacc.create_account(2, 0)
    assert  result == False

    result = bkacc.create_account(3456, 'checking',300)
    assert result ==True
    
    '''

def test_get_prefix():
    assert bkacc.BankAccount.get_prefix('c') ==20000
    assert bkacc.BankAccount.get_prefix('s') ==30000

def test_seek_db_by_account_no():
    assert  bkacc.BankAccount.seek_db_by_account_no(3456)!=None
    assert  bkacc.BankAccount.seek_db_by_account_no(1)==None

def test_seek_db_by_account_id():
    result =bkacc.BankAccount.seek_db_by_account_id(1950)
    print(result)
    assert  result==None

def test_savingacc():
    s_acc = bkacc.SavingsAccount(300,0.01)
    assert  s_acc.balance ==300
    assert  s_acc.account_type =='savings'
    assert  s_acc.intrst_rate ==0.01

def test_chking():
    s_acc = bkacc.CheckingAccount(200)
    assert  s_acc.balance ==200
    assert  s_acc.account_type =='checking'


#pytest test_bankaccount.py

