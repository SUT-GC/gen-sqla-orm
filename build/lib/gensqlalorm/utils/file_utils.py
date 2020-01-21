#! -*- coding:utf8 -*-

import os
import sys
import json

reload(sys)
sys.setdefaultencoding("utf-8")

program_path = os.path.abspath(__file__ + "/../..")


def gen_file_abspath(file_path, root_path=None):
    if root_path is None:
        return program_path + "/" + file_path
    else:
        return root_path + "/" + file_path
