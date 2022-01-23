
from sqlalchemy import Column,  INTEGER, VARCHAR, FLOAT, DATETIME, or_
from sqlalchemy.ext.declarative import declarative_base

from utility import Utility as ut
from database import Database


Base = declarative_base()

class Employee(Base):
    ''' A class to represent a bank account transaction'''

    __tablename__ = 'employee'

    id = Column(INTEGER, primary_key=True)
    name  = Column(VARCHAR(60))
    level = Column(VARCHAR(20))
    project = Column(VARCHAR(100))

    def __init__(self, name , level='employee', project=None):
        self.name=name
        self.level = level
        self.project= project

    @staticmethod
    def new_employee_at_db( name, level='employee', project=None):

            employee = Employee(name, level,project)

            db_result= Database.new_rec_in_db(employee)

            # db creaton succeeds
            if db_result[0]==1:
                ut.print_success("The employee has been created.")
                ut.print_success("The id is: {} ".format(db_result[1]))

            # db creaton fails
            else:
                ut.print_error("Employee creation has failed.")


class Manager(Employee):
    def __init__(self, name, level='mananger', project='unknown'):
       Employee.__init__(self, name, level)
       self.project = project

    @staticmethod
    def new_manager_at_db( name, level='manager', project='Mis'):
        Employee.new_employee_at_db(name, level, project)




if __name__ =="__main__" :

    Database.initialise()
    #Employee.create_employee_db('Jerry')
    Manager.new_manager_at_db('Tom')
    #ut.print_success('succ!')

