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


class ProductGradientPrice(Base):
    __tablename__ = "product_gradient_price"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    item_identity = Column(String, name="item_identity", default='', nullable=False)
    rule = Column(String, name="rule", default='', nullable=False)
    type = Column(Integer, name="type", default=0, nullable=False)
    data_state = Column(Integer, name="data_state", default=0, nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), nullable=False)


class ProductPrice(Base):
    __tablename__ = "product_price"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    item_identity = Column(String, name="item_identity", nullable=False)
    price = Column(Float, name="price", nullable=False)
    type = Column(Integer, name="type", nullable=False)
    state = Column(Integer, name="state", default=0, nullable=True)
    snapshot_id = Column(BigInteger, name="snapshot_id", nullable=False)
    exp_group = Column(String, name="exp_group", nullable=True)
    label_type = Column(Integer, name="label_type", default=-1, nullable=True)
    label = Column(String, name="label", nullable=True)
    currency_type = Column(Integer, name="currency_type", default=1, nullable=True)
    start_time = Column(DateTime, name="start_time", nullable=True)
    end_time = Column(DateTime, name="end_time", nullable=True)
    effective_month = Column(String, name="effective_month", nullable=True)
    effective_day = Column(String, name="effective_day", nullable=True)
    effective_month_day = Column(String, name="effective_month_day", nullable=True)
    create_time = Column(DateTime, name="create_time", nullable=True)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), nullable=True)


class ProductPriceSnapshot(Base):
    __tablename__ = "product_price_snapshot"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    price_id = Column(BigInteger, name="price_id", nullable=True)
    item_identity = Column(String, name="item_identity", nullable=False)
    price = Column(Float, name="price", nullable=False)
    type = Column(Integer, name="type", nullable=False)
    state = Column(Integer, name="state", default=0, nullable=True)
    exp_group = Column(String, name="exp_group", nullable=True)
    label_type = Column(Integer, name="label_type", default=-1, nullable=True)
    label = Column(String, name="label", nullable=True)
    currency_type = Column(Integer, name="currency_type", default=1, nullable=True)
    start_time = Column(DateTime, name="start_time", nullable=True)
    end_time = Column(DateTime, name="end_time", nullable=True)
    effective_month = Column(String, name="effective_month", nullable=True)
    effective_day = Column(String, name="effective_day", nullable=True)
    effective_month_day = Column(String, name="effective_month_day", nullable=True)
    create_time = Column(DateTime, name="create_time", nullable=True)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), nullable=True)
