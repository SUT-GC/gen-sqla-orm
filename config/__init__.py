#! -*- coding:utf8 -*-

import yaml

from utils import gen_file_abspath

import os
import sys

sys.path.append(os.path.abspath(__file__))
reload(sys)
sys.setdefaultencoding("utf-8")

file_path = gen_file_abspath("/config/db_config.yml")


class Config(object):
    def __init__(self, host, user, pawd, port, name):
        self.host_name = host
        self.user_name = user
        self.pass_word = pawd
        self.port = port
        self.name = name

    def __str__(self):
        return "host:%s, port:%s, user:%s, pass:%s, name:%s" % (self.host_name, self.port, self.user_name, self.pass_word, self.name)


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
    resource = yaml.load(r_file, Loader=yaml.FullLoader)
    result = {}
    for db_name, db_config in resource.items():
        config = Config(
            str(db_config.get("hostName")),
            str(db_config.get("userName")),
            str(db_config.get("passWord")),
            int(db_config.get("dbPort")),
            str(db_config.get("dbName"))
        )
        result[db_name] = config

    return result


if __name__ == "__main__":
    print get_db_config()
