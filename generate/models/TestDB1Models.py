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
