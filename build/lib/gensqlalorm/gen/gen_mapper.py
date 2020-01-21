#! -*- coding:utf8 -*-

import os
import sys
import json

reload(sys)
sys.setdefaultencoding("utf-8")

FIELD_MAPPER = {
    "bigint": "BigInteger",
    "int": "Integer",
    "tinyint": "Integer",
    "smallint": "SmallInteger",
    "mediumint": "Integer",
    "integer": "Integer",
    "float": "Float",
    "double": "Float",
    "decimal": "Float",
    "date": "DateTime",
    "datetime": "DateTime",
    "timestamp": "DateTime",
    "char": "String",
    "varchar": "String",
    "tinyblob": "String",
    "tinytext": "String",
    "blob": "String",
    "text": "Text",
    "mediumblob": "String",
    "mediumtext": "String",
    "longblob": "String",
    "longtext": "String",
    "bit": "String"
}

DEFAULT_VALUE_MAPPER_FORMAT = {
    "String": "\"\'%s\'\"",
    "Text": "\"\'%s\'\"",
    "Float": "\"%s\"",
    "Integer": "\"%s\"",
    "BigInteger": "\"%s\"",
    "SmallInteger": "\"%s\"",
    "DateTime": "datetime.now()"
}


def find_sqlalchemy_type(db_type):
    for k, v in FIELD_MAPPER.items():
        if db_type.startswith(k):
            return v

    raise Exception("not support type " + db_type)


def find_default_value(sqlal_type, value):
    if sqlal_type == "DateTime" and "current_timestamp" == value:
        return DEFAULT_VALUE_MAPPER_FORMAT.get(sqlal_type)
    if sqlal_type == "DateTime":
        return ""

    return eval("%s %% (%s)" % (DEFAULT_VALUE_MAPPER_FORMAT.get(sqlal_type), "value"), {"value": value})


if __name__ == "__main__":
    print find_default_value("String", "0")
