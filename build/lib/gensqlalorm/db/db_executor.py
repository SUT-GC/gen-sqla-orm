#! -*-coding:utf8 -*-
import os
import sys

sys.path.append(os.path.abspath(__file__))
reload(sys)
sys.setdefaultencoding("utf-8")


class DBExecutor(object):
    def __init__(self, connection_pool):
        self.__connection_pool = connection_pool
        self.__cursor_pool = {}

    def exec_sql(self, project_name, sql):
        self.__init_cursor(project_name)

        cursor = self.__cursor_pool.get(project_name)

        if cursor is None:
            raise Exception("%s's cursor not init..." % project_name)

        cursor.execute(sql)

        return cursor.fetchall()

    def __init_cursor(self, project_name):
        if self.__cursor_pool.get(project_name) is None:
            connection = self.__connection_pool.get_connection(project_name)
            self.__cursor_pool[project_name] = connection.get_cursor()
        else:
            pass
