#! -*- coding:utf8 -*-

import pymysql

from gensqlalorm.config import get_db_config

import os
import sys

sys.path.append(os.path.abspath(__file__))
reload(sys)
sys.setdefaultencoding("utf-8")


class DBConnection(object):
    def __init__(self, config):
        self.__db_config = config
        self.__db_connect = self.__connect()
        print '[info] init db connect success ...'

    def __connect(self):
        return pymysql.connect(
            self.__db_config.host_name,
            self.__db_config.user_name,
            self.__db_config.pass_word,
            self.__db_config.name,
            self.__db_config.port
        )

    def get_cursor(self):
        return self.__db_connect.cursor()


class DBConnectionPool(object):
    def __init__(self, configs):
        self.__db_config_list = configs
        self.__db_connect_pool = self.__connect()

    def __connect(self):
        connect_pool = {}
        for db_name, db_config in self.__db_config_list.items():
            connect_pool[db_name] = DBConnection(db_config)

        return connect_pool

    def get_connection(self, project_name):
        return self.__db_connect_pool[project_name]


if __name__ == "__main__":
    db_config_list = get_db_config()
    db_connection_pool = DBConnectionPool(db_config_list)

    # print db_connection_pool
    # print gen_file_abspath("hello")
