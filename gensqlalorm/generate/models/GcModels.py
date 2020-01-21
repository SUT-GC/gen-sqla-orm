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


class ProjectMainTaskInfo(Base):
    __tablename__ = "project_main_task_info"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    project_name = Column(String, name="project_name", default='', nullable=False)
    main_task_id = Column(String, name="main_task_id", default='', nullable=False)
    main_task_name = Column(String, name="main_task_name", default='', nullable=False)
    main_task_status = Column(Integer, name="main_task_status", default=0, nullable=False)
    main_task_request_body = Column(Text, name="main_task_request_body", nullable=True)
    owner = Column(String, name="owner", default='', nullable=False)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), nullable=False)


class ProjectSubTaskInfo(Base):
    __tablename__ = "project_sub_task_info"

    id = Column(BigInteger, name="id", primary_key=True, nullable=False, autoincrement=True)
    main_task_id = Column(String, name="main_task_id", default='', nullable=False)
    sub_task_id = Column(String, name="sub_task_id", default='', nullable=False)
    sub_task_name = Column(String, name="sub_task_name", default='', nullable=False)
    sub_task_status = Column(Integer, name="sub_task_status", default=0, nullable=False)
    sub_task_process = Column(Integer, name="sub_task_process", default=0, nullable=False)
    sub_task_code = Column(String, name="sub_task_code", default='', nullable=False)
    sub_task_request_body = Column(Text, name="sub_task_request_body", nullable=True)
    create_time = Column(DateTime, name="create_time", default=datetime.now(), nullable=False)
    update_time = Column(DateTime, name="update_time", default=datetime.now(), nullable=False)
    weight = Column(Integer, name="weight", default=0, nullable=False)
