#! -*- coding:utf8 -*-

import yaml

import os
import sys

sys.path.append(os.path.abspath(__file__))
reload(sys)
sys.setdefaultencoding("utf-8")

file_path = "db_config.yml"


class Config(object):
    def __init__(self, host, user, port, pawd, name):
        self.host_name = host
        self.user_name = user
        self.pass_word = pawd
        self.port = port
        self.name = name


def get_db_config():
    """
    {
        "TestDB_1":{
            "host": xxxx,
            "user": xxxx,
            "pass": xxxx,
            "port": xxxx
        }
    }
    """
    r_file = open(file_path, "r")
    resource = yaml.load(r_file)
    result = {}
    for db_name, db_config in resource.items():
        config = Config(
            db_config.get("hostName"),
            db_config.get("userName"),
            db_config.get("passWord"),
            db_config.get("dbPort"),
            db_config.get("dbName")
        )
        result[db_name] = config

    return result


if __name__ == "__main__":
    print get_db_config()
