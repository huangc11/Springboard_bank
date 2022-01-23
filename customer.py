from sqlalchemy import Column,  INTEGER, VARCHAR, or_
from sqlalchemy.ext.declarative import declarative_base
#import database as db
from  database import Database
from utility import Utility as ut

from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
Base = declarative_base()

class Customer(Base):

    """
    A class to represent a customer.

    Attributes
    ----------
    id:         customer id.  Generated by system at creation.
    name (str):          name of the customer
    address (str):       name of the customer
    customer_no (str):  customer_no of the customer.

    Methods
    -------
    __init__(self, name, address='', cust_no=None):
        constructor

    __repr__()

    seek_db_by_name_addr(p_name, p_addr=None)
        (staticmethod) seek customer record in database by name and address.

    list_customer(self)
        (staticmethod) print records in customer table

    """

    __tablename__ = 'customer'

    id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR(60), nullable=False)
    address = Column(VARCHAR(100))


    def __init__(self, name, address=''):
        self.name, self.address = name, address


    @classmethod
    def list_customer(self):
         session = Database.get_session()
         for customer in session.query(Customer):
            print(customer)

    def __repr__(self):
      return ("Customer({id}, '{name}', '{address}')".format(id=self.id, name=self.name, address=self.address))

    @staticmethod
    def seek_db_by_name_addr(p_name, p_addr=None):
        """search  customer in database by name and address

          Args:
            p_name (str): customer name
            p_addr (str): customer address

        Returns:
            a tuple which could have following values:
                 (1, id)   -- single result found
                 (2, 'mulitple results  found')  -- multiple results found
                 (-1, 'no one found') -- no one found
                 (-2, 'action fails due to low level issue') --failure
        """

        try:
            session = Database.get_session()
            rec = session.query(Customer). \
                filter(Customer.name == p_name). \
                filter(or_(Customer.address == p_addr,
                           p_addr == None)). \
                one()

            return (1, rec.id)
        except MultipleResultsFound:
            return (2, '2. multiple results found')
        except NoResultFound:
            return (-1, '1.not found')
        except Exception as e:
            ut.print_error(e)
            return (-2, 'Seeking customer in DB failed')


def create_customer():

    name = input("Please enter the new customer's name: ")
    addr = input("Please enter the new customer's address: ")
   # option = input("Please confirm save or not: s for save, otherwise cancel: ")
   # option = input("Please confirm: S -- save M -- modify "

    seek_result = Customer.seek_db_by_name_addr(name, addr)

    # if not found, create in database
    if  seek_result[0] == -1:

            customer = Customer(name, addr)
            db_result= Database.new_rec_in_db(customer)

            # db creaton succeeds
            if db_result[0]==1:
                print("%%%%%%%% customer has been created %%%%%%%% ")
                print("         The customer id is: {} ".format(db_result[1]))

            # db creaton fails
            else:
                ut.print_error("####### Creation failed due to errors ########")


    #if one ore more result found, aborted
    elif ( seek_result[0]>0):
          ut.print_error( 'Customer(s) with same name and address exist(s). Creation failed.')

    #  seeking fails, creaton aborts
    else:
           print("####### Creation failed due to errors ########")





if __name__ == '__main__':
    Database.initialise()
   # create_customer()
    Customer.list_customer()

