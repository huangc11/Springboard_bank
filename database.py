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
        session = Database.get_session_()

        ut.print_one((dict_mapped))

        session.query(DBClass).filter(DBClass.account_id ==id).update(dict_mapped)
        session.commit()

   # s.query(Media).filter(Media.id == self.id).update(mapped_values)


    @staticmethod
    def new_rec_in_db(object):
            """create a new record in database

              Args:
                self : The first parameter.
                p_database (Database object):

              Returns:
                a tuple as follows:
                      (1, id), if success
                      (-1, '.Operation failed -- record with this primary key value exists')
                      (-2, 'operation failed')
            """

            session = Database.get_session()
            ut.print_one(object)

            try:
                    #write this object  to database
                    session.add(object)
                    session.commit()

                    # if succeed return (1, object.id)
                    return (1, object.id)

            except exc.IntegrityError:
                   session.rollback()
                   return (-1, '1.Operation failed -- record with this primary key value exists ')

            except Exception as e:
                    #Other fail
                    session.rollback()
                    ut.print_one('2.Operation failed . ')
                    ut.print_one(e)
                    return (-2, 'operation failed')



if __name__ == '__main__':
    pass


