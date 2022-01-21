from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utility import Utility as ut


class Database:
    """ A class to represent the databse"""
    __db_url ="mysql+pymysql://chu:tree@localhost:3306/bank"
    __session = None
    __engine = None
    #session =None

    def __init__(self):
        #"mysql+pymysql://chu:tree@localhost:3306/bank"

        engine = create_engine(Database.__db_url, echo=False)
        #engine = create_engine(db_url, echo=False)
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.engine = engine
        ut.print_one(self.session)
        #Database.session= self.session



    def get_session(self):
        print("@@@@@@ session:{} @@@@@@@".format(self.session))
        return self.session

    def print_session(self):
        print("%%%%%%% session:{} %%%%%%%%".format(self.session))

    @staticmethod
    def initialise(**kwargs):
        db_url = "mysql+pymysql://chu:tree@localhost:3306/bank"
        #db_url = "mysql+pymysql://{user}:{password}@{host}:{port}/{db}"
        engine = create_engine(db_url, echo=False)
        Session = sessionmaker(bind=engine)
        #Database.__session = Session()
        #Database.__engine = engine

        #Database.__connection_pool = pool.SimpleConnectionPool(1, 10, **kwargs)

if __name__ == '__main__':

    bank_db = Database()

    session1 = bank_db.get_session()
    ut.print_one('session1')
    ut.print_one(session1)
