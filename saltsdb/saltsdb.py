# Licensed under a 3-clause BSD style license - see LICENSE.rst

import sqlalchemy

__all__ = ['SALTSdb']


class SALTSdb:
    """SALTSdb is an interface to the SALT mysql database and specifically
      simplifies the steps of returning objects from a call to the database

      Parameters
      ----------
      host: string
           host name of mysql database

      dbname: string
           name of mysql database

      user: string
           user for database

      passwd: string
           password of user for mysql database

      port: int
           Port for connecting to the database
    """

    def __init__(self, host, dbname, user, passwd, port):
        sdb = 'mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(user, passwd,
                                                             host, port,
                                                             dbname)
        self.sdb = sqlalchemy.create_engine(sdb)
