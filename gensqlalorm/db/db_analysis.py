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


def show_create_table(project_name, table_name):
    """
    [{
        "column": 'xxxx',
        "type: 'bigint(20)',
        "comment: 'xxxxx'
    }]
    """
    init()
    sql_r = db_executor.exec_sql(project_name, "show create table %s;" % table_name)
    table_create_sql = sql_r[0][1]
    result = []
    table_create_sql_lines = table_create_sql.split("\n")
    for table_create_sql_line in table_create_sql_lines:
        table_create_sql_line = table_create_sql_line.strip()
        if table_create_sql_line.startswith("`") and table_create_sql_line.endswith(","):
            one = {}
            one["column"] = table_create_sql_line.split("` ")[0].split("`")[1]
            one["type"] = table_create_sql_line.split("` ")[1].split(" ")[0]
            one["comment"] = table_create_sql_line.split("COMMENT ")[1].replace(",", "").replace("'", "") if "COMMENT" in table_create_sql_line else ""
            result.append(one)

    return result


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
    print json.dumps(desc_table("PayPrivilege", "gc_test_shard_table_2"))
