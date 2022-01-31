from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utility import Utility as ut
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from sqlalchemy import exc


class Database:
    """ A class to represent the databse"""
    __db_url ="mysql+pymysql://chu:tree@localhost:3306/bank"
    __session = None
    __engine = None
    const_success = 1
    const_fail = -1
    #session =None

    def __init__(self):
        #"mysql+pymysql://chu:tree@localhost:3306/bank"

        engine = create_engine(Database.__db_url, echo=False)
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.engine = engine

    def get_session2():
        return self.session

    def print_session(self):
        print("%%%%%%% session:{} %%%%%%%%".format(self.session))

    @staticmethod
    def initialise(**kwargs):
        db_url = "mysql+pymysql://chu:tree@localhost:3306/bank"
        #db_url = "mysql+pymysql://{user}:{password}@{host}:{port}/{db}"
        engine = create_engine(db_url, echo=False)
        Session = sessionmaker(bind=engine)
        Database.__session = Session()
        #Database.__engine = engine

        #Database.__connection_pool = pool.SimpleConnectionPool(1, 10, **kwargs)

    @staticmethod
    def get_session():
        return Database.__session

    @staticmethod
    def update_rec_in_db(DBClass, id, dict_mapped):
        """update table record in database

          Args:
           DBClass (class -- table):
           id (str): id of the record to be  updated
           dict_mapped: dict  which contains the  column/value pairs to be updated

          Returns:
                 const_success, if success
                 const_fail, if failure
        """
        session = Database.get_session()

        try:
            session.query(DBClass).filter(DBClass.id ==id).update(dict_mapped)
            session.commit()
            return Database.const_success
        except Exception as e:
            ut.log_exeption(e)
            return Database.const_fail

   # s.query(Media).filter(Media.id == self.id).update(mapped_values)


    @staticmethod
    def new_rec_in_db(object):
            """create a new record in database

              Args:
                self : The first parameter.
                p_database (Database object):

              Returns:
                      object, if success
                      None, if failure
            """

            session = Database.get_session()

            try:
                    #write this object  to database
                    session.add(object)
                    session.commit()

                    # if succeed return (1, object.id)
                    return object

            except Exception as e:
                    #if fail
                    ut.log_exeption(e)
                    return None



if __name__ == '__main__':
    pass


