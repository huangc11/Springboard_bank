
from database import Database
from employee import Employee
import pytest




#create_account(p_customer_id, p_account_type='checking', p_balance=0, p_intrs_rate=0.01):

def test_create_employee():

    emp_name = 'marry'

    emp =Employee(emp_name)
    emp_cr=emp.insert_into_db()


    assert  emp_cr.name ==emp_name
    assert  emp_cr.password !=None

