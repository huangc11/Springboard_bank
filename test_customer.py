
from database import Database
from customer import Customer
from customer import create_customer
import pytest


Database.initialise()

def test_f_customer_not_exist():

    assert Customer.f_customer_not_exist('fei1','kirkland') == True
    assert Customer.f_customer_not_exist('fei','kirkland') == False

def test_seek_db_by_id():
    assert Customer.f_seek_db_by_id(169)==None
    assert Customer.f_seek_db_by_id(144) != None

def test_create_customer():
    assert create_customer('fei', 'kirkland')!=None
    #assert create_customer('fei4', 'kirkland')==True

   # assert seek_db_by_id(144)!=None



