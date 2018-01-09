
import sqlalchemy
import pytest

from ..saltsdb import SALTSdb


def test_creation():
    with pytest.raises(TypeError):
        sdb = SALTSdb()


def test_connection():
    with pytest.raises(Exception): #sqlalchemy.exc.ProgrammingError):
        sdb = SALTSdb('sdb', 'sdb', 'sdb', 'sdb', '1111')
        sdb.sdb.connect()
