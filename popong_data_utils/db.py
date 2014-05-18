# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from popong_models import Base


__all__ = ['connect_db']


def connect_db(sqlalchemy_uri):
    engine = create_engine(sqlalchemy_uri)
    session = scoped_session(sessionmaker(autocommit=False,
                                          autoflush=False,
                                          bind=engine))
    Base.query = session.query_property()


class DbNotInitiatedError(Exception):
    def __init__(self):
        super(DbNotInitiatedError, self).__init__(
                'Please execute popong_data_utils.connect_db(uri) first')

