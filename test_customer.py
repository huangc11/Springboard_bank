
from database import Database
from customer import Customer
import pytest


Database.initialise()

def test_exist_by_name_addr():

    assert Customer.not_exist_by_name_addr('fei','kirkland') ==False
    assert Customer.not_exist_by_name_addr('Maria','bothell1') ==True


def t1est_get_by_id():
    assert Customer.get_by_id(169)==None
    assert Customer.get_by_id(144) != None

def test_insert_customer():
    customer = Customer('Jack','Kenmore').insert_to_db()
    assert customer.name =='Jack'
    assert customer.address=='Kenmore'


   # assert seek_db_by_id(144)!=None



