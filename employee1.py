
from sqlalchemy import Column,  INTEGER, VARCHAR, FLOAT, DATETIME, or_
from sqlalchemy.ext.declarative import declarative_base

from utility import Utility as ut
from sequence import Sequence as Seq
from database import Database


Base = declarative_base()

class Employee(Base):
    ''' A class to represent a bank account transaction'''

    __tablename__ = 'employee'

    id = Column(INTEGER, primary_key=True)
    name  = Column(VARCHAR(60))
    login = Column(VARCHAR(20))
    password = Column(INTEGER)


    __pwd_key =43989

    def __init__(self, name):
        self.name=name

        tmpseq = Seq.next()
        self.login = 'a'+str(tmpseq).rjust(4,'0')
        self.password = tmpseq


    def __repr__(self):
        return("Employee(id={},name='{}',login='{}', password='{}'')".format(self.id, self.name, self.login, self.password))
        #return ("Employee({id}, '{name}', '{login}'".format(self.id, self.name, self.login))


    def insert_into_db(self):
        """insert a new account record into database"""
        new_emp= Database.new_rec_in_db(self)
        # db creaton succeeds
        if new_emp!=None:
            ut.log_info("The employee has been created.")
        else:
            ut.log_info("The employee creation faild.")

        return new_emp

    def set_password(self, password):
        self.password = password

    def update_in_db(self, ):
        Database.update_rec_in_db(Employee, self.id, {'password':self.password})


    @staticmethod
    def get_by_id(p_id):
        """Get the employee  record from database by id. Returns employee object (if found) or None (not found)
        """
        session = Database.get_session()
        rec = session.query(Employee).filter(Employee.id == p_id).scalar()
        return rec



if __name__ =="__main__" :

    Database.initialise()

    '''
    emp =Employee('jerry')
    emp.insert_into_db()
    print(emp.password)
    '''

    emp = Employee.get_by_id(10)
    print(emp)
    emp.set_password('845')
    emp.update_in_db
    print(emp)
    emp = Employee.get_by_id(10)
    print(emp.password)



