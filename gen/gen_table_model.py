#! -*- coding:utf8 -*-

import os
import sys
import json

sys.path.append(os.path.abspath(".."))
reload(sys)
sys.setdefaultencoding("utf-8")

from utils import (
    format_for_hump
)
from db import (
    desc_table,
    show_tables
)


def show_all_tables(project_name):
    return show_tables(project_name)


def gen_table_model(project_name, table_name):
    table_desc = desc_table(project_name, table_name)
    table_model_name = format_for_hump(table_name)
