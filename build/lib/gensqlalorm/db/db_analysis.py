#! -*- coding:utf8 -*-

import os
import sys
import json

reload(sys)
sys.setdefaultencoding("utf-8")

from gensqlalorm.config import get_db_config
from db_connect import DBConnectionPool
from db_executor import DBExecutor

db_connection_pool = None
db_executor = None


def init():
    global db_connection_pool
    global db_executor

    if db_connection_pool is None:
        db_connection_pool = DBConnectionPool(get_db_config())
    if db_executor is None:
        db_executor = DBExecutor(db_connection_pool)


def desc_table(project_name, table_name):
    init()
    """
    [
        {
            "name": 'id',
            "type: 'bigint(20)',
            "can_null: 'yes',
            "key_type": 'pri',
            "default_value": null,
            "extra": "auto_increment"
        }
    ]
    """
    sql_r = db_executor.exec_sql(project_name, "desc %s;" % table_name)

    result = []
    for sql_r_one in sql_r:
        result.append({
            "name": sql_r_one[0].lower() if sql_r_one[0] is not None else None,
            "type": sql_r_one[1].lower() if sql_r_one[1] is not None else None,
            "can_null": sql_r_one[2].lower() if sql_r_one[2] is not None else None,
            "key_type": sql_r_one[3].lower() if sql_r_one[3] is not None else None,
            "default_value": sql_r_one[4].lower() if sql_r_one[4] is not None else None,
            "extra": sql_r_one[5].lower() if sql_r_one[5] is not None else None,
        })

    return result


def show_tables(project_name):
    init()
    """
    ['table_name_1', 'table_name_2']
    """
    sql_r = db_executor.exec_sql(project_name, "show tables;")
    if not sql_r:
        return []

    result = []
    for sql_r_one in sql_r:
        result.append(sql_r_one[0])

    return result


if __name__ == "__main__":
    print json.dumps(show_tables("TestDB_2"))
    print json.dumps(desc_table("TestDB_2", "gc_test_shard_table_2"))
