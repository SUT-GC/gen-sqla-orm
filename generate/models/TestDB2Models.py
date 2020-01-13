# -*- coding:utf8 -*-

from sqlalchemy import (
    Column,
    SmallInteger,
    BigInteger,
    String,
    Text,
    Float,
    DateTime,
    Integer,
)

from sqlalchemy.ext.declarative import declarative_base

from datetime import datetime


Base = declarative_base()


class GcTestShardTable(Base):
    __tablename__ = "gc_test_shard_table"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(BigInteger, name="user_id", default=0, nullable=False)
    user_name = Column(String, name="user_name", default='', nullable=False)
    user_age = Column(Integer, name="user_age", default=0, nullable=False)
    data_status = Column(Integer, name="data_status", default=0, nullable=False)
    created_at = Column(DateTime, name="created_at", default=datetime.now(), nullable=True)
    updated_at = Column(DateTime, name="updated_at", default=datetime.now(), nullable=True)
