# Licensed under a 3-clause BSD style license - see LICENSE.rst

import sqlalchemy
import pandas as pd

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

    def select(self, selection, table, logic=None):
        """Select a record from a table

        Parameters
        ----------
        selection: string
            columns to return
        table: string
            table or group of tables to select from
        logic: string
            logic for selecting from table

        Returns
        -------
        record: ~pandas.DataFrame
            Dataframe of results
        """

        cmd_sql = 'SELECT {} FROM {}'.format(selection, table)
        if logic is not None:
            cmd_sql += ' WHERE {}'.format(logic)
        return pd.read_sql(cmd_sql, self.sdb)

    def insert(self, insertion, table):
        """Insert a record into a table

        Parameters
        ----------
        insertion: string
            values and columns to insert
        table: string
            table or group of tables to select from

        """

        # build the command
        exec_command = "INSERT INTO {} SET {}".format(table, insertion)
        exec_command = sqlalchemy.sql.text(exec_command)

        self.sdb.execute(exec_command)

    def replace(self, replace, table):
        """Insert a record into a table

        Parameters
        ----------
        replace: string
            values and columns to replace
        table: string
            table or group of tables to select from

        """

        # build the command
        exec_command = "REPLACE INTO {} VALUES ({})".format(table, replace)
        exec_command = sqlalchemy.sql.text(exec_command)

        self.sdb.execute(exec_command)

    def update(self, insertion, table, logic=None):
        """Update a record in a table

        Parameters
        ----------
        insertion: string
            values and columns to insert
        table: string
            table or group of tables to select from
        logic: string
            logic for selecting from table

        """

        # build the command
        exec_command = "UPDATE {} SET {}".format(table, insertion)
        if logic is not None:
            exec_command += ' WHERE {}'.format(logic)
        exec_command = sqlalchemy.sql.text(exec_command)

        self.sdb.execute(exec_command)
