#! -*- coding:utf8 -*-

import os
import sys
import json

sys.path.append(os.path.abspath(".."))
reload(sys)
sys.setdefaultencoding("utf-8")

import os

program_path = os.path.abspath("..")


def gen_file_abspath(file_path, root_path=None):
    if root_path is None:
        return program_path + "/" + file_path
    else:
        return root_path + "/" + file_path
