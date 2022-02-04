import datetime as dt
from utility import Utility as ut
from  database import Database
from customer import Customer
from bankaccount import BankAccount, SavingsAccount, CheckingAccount
from utility import glb_logger
import CustomerAccount as m_ca



def create_customer_account(p_customer_id, p_account_type, p_balance=0, p_intrs_rate=0.01):
    """create account

      Args:
        p_customer_id(int): customer id
        p_balance(float): balance of the account
        p_account_type(str):   account type, ['checking', 'savings']

      Returns:
              Account id, if success
              None, if failure
    """

    #check if customer existing
    o_customer = Customer.f_seek_db_by_id(p_customer_id)
    if o_customer ==None:
            ut.log_info('account creation failed -- customer with id={} not found.'.format(p_customer_id))
            return None

   #check if account type is valid
    if p_account_type not in ('s','c'):
            ut.log_info('account creation failed, account type "{} unknown"'.format('p_account_type'))
            return None

   # create an account object
    if p_account_type =='s':
        o_account = SavingsAccount(p_balance,  0.01)
    elif  p_account_type =='c':
        o_account = CheckingAccount(p_balance)

    # create a new record in database
    new_account=o_account.insert_to_db()

    if new_account==None:
        ut.log_info('Account creation failed -- isnert account into database failed')
        return None

    # assign the acocunt to the customer, i.e. create a customer-account associatioon
    o_cust_acc= m_ca.CustomerAccount(o_customer.id,  new_account.id)
    new_cust_acc = Database.new_rec_in_db(o_cust_acc)

    if new_cust_acc == None: #if fail
        #ut.log_info('Account creation failed -- customer-account assignment failed')
        return None

    ut.log_info('Account (id ={}) successfully created and assgined to customer (id={}).'
                .format(o_account.id, o_customer.id))
    ut.log_info('\t {}'.format(o_account))
    ut.log_info('\t {}'.format(o_customer))
    return o_account




#print(Customer.f_seek_db_by_id(100))

#Database.initialise()
#create_customer_account(101, 'c' ,200)
create_customer_account(101, 's' ,300)

