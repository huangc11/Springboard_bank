from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Database:
    """ A class to represent the databse"""

    __session = None
    __engine = None

    def __init__(self, db_url):
        self.engine = create_engine(db_url, echo=False)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def get_session(self):
        return self.session


    @staticmethod
    def initialise(**kwargs):
        db_url = "mysql+pymysql://chu:tree@localhost:3306/bank"
        #db_url = "mysql+pymysql://{user}:{password}@{host}:{port}/{db}"
        engine = create_engine(db_url, echo=False)
        Session = sessionmaker(bind=engine)
        Database.__session = Session()
        Database.__engine = engine

        #Database.__connection_pool = pool.SimpleConnectionPool(1, 10, **kwargs)

    @staticmethod
    def get_session():
        return Database.__session

