
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
    password = Column(VARCHAR(20))

    def __init__(self, name):
        self.name=name

        tmpseq = Seq.next()
        self.login = 'a'+str(tmpseq).rjust(4,'0')
        self.password = str(tmpseq)

    def __repr__(self):
        return("Employee(id={},name='{}',login='{}', password='{}')".format(self.id, self.name, self.login,self.password))
        #return ("Employee({id}, '{name}', '{login}'".format(self.id, self.name, self.login))

    def insert_into_db(self):


            new_emp= Database.new_rec_in_db(self)

            # db creaton succeeds
            if new_emp!=None:
                ut.log_info("The employee has been created.")
                ut.log_info(self)
                return new_emp

            ut.log_info("The employee creation faild.")

            return None


if __name__ =="__main__" :

    Database.initialise()

    emp =Employee('tom')
    emp.insert_into_db()
    print(emp)
