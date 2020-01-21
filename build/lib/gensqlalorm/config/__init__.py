#! -*- coding:utf8 -*-

import yaml

import os
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

from gensqlalorm.utils import (
    gen_file_abspath
)

db_config_file_path = gen_file_abspath("config/db_config.yml")
gen_config_file_path = gen_file_abspath("config/gen_config.yml")


class GenConfig(object):
    def __init__(self, gen_project_list, ignore_shard, root_path):
        self.gen_list = gen_project_list
        self.ignore_shard = ignore_shard
        self.root_path = root_path

    def __str__(self):
        return "gen_list:%s, ignore_shard:%s, root_path:%s" % (self.gen_list, self.ignore_shard, self.root_path)


class DBConfig(object):
    def __init__(self, host, user, pawd, port, name):
        self.host_name = host
        self.user_name = user
        self.pass_word = pawd
        self.port = port
        self.name = name

    def __str__(self):
        return "host:%s, port:%s, user:%s, pass:%s, name:%s" % (self.host_name, self.port, self.user_name, self.pass_word, self.name)


def get_gen_config():
    r_file = open(gen_config_file_path, "r")
    resource = yaml.load(r_file, Loader=yaml.FullLoader)

    return GenConfig(resource.get("genProjectNames"),
                     resource.get("ignoreShard"),
                     resource.get("rootPath"))


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
    r_file = open(db_config_file_path, "r")
    resource = yaml.load(r_file, Loader=yaml.FullLoader)
    result = {}
    for db_name, db_config in resource.items():
        config = DBConfig(
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
