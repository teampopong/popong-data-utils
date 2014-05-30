# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from popong_models import Base


__all__ = ['connect_db']


def connect_db(uri_or_session):
    if isinstance(uri_or_session, scoped_session):
        session = uri_or_session
    else:
        sqlalchemy_uri = uri_or_session
        engine = create_engine(sqlalchemy_uri)
        session = scoped_session(sessionmaker(autocommit=False,
                                              autoflush=False,
                                              bind=engine))
    _connect_db_by_scoped_session(session)


def _connect_db_by_scoped_session(session):
    Base.query = session.query_property()


class DbNotInitiatedError(Exception):
    def __init__(self):
        super(DbNotInitiatedError, self).__init__(
                'Please execute popong_data_utils.connect_db(uri) first')

