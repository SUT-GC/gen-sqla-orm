#! -*- coding:utf8 -*-

import os
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

from gensqlalorm.config import (
    get_gen_config,
)

from gensqlalorm.utils import (
    gen_file_abspath,
    format_for_hump,
    format_for_shard
)

from gen_table_model import (
    show_all_tables,
    desc_table
)

from gen_mapper import (
    FIELD_MAPPER,
    find_sqlalchemy_type,
    find_default_value
)


def gen():
    gen_config = get_gen_config()

    gen_project_names = gen_config.gen_list
    ignore_shard = gen_config.ignore_shard
    root_path = gen_config.root_path

    print '[info] read gen config success, gen_project_names:%s, ignore_shard:%s, root_path:%s ...' % (gen_project_names, ignore_shard, root_path)

    out_dir_path = gen_file_abspath("generate", root_path)
    out_init_file_path = gen_file_abspath("generate/__init__.py", root_path)
    out_model_dir_path = gen_file_abspath("generate/models/", root_path)

    if not os.path.exists(out_dir_path):
        os.makedirs(out_dir_path)

    print '[info] init generate dir success ...'

    if not os.path.exists(out_model_dir_path):
        os.makedirs(out_model_dir_path)

    print '[info] init gen models dir success ...'

    out_init_file = open(out_init_file_path, "w+")
    out_init_file.write("#! -*- coding:utf8 -*- \n")

    print '[info] write __init__.py success ...'

    sqlalchemy_fields = set(FIELD_MAPPER.values())
    empty_line = "\n"

    for project_name in gen_project_names:
        print '========================== 【%s】 ========================' % project_name

        project_file_name = format_for_hump(project_name) + "Models.py"
        project_model_py = open("%s%s" % (out_model_dir_path, project_file_name), "w+")
        print '[info] create 【%s】 model file named 【%s】 success ...' % (project_name, project_file_name)

        project_model_py.write("# -*- coding:utf8 -*-\n")
        project_model_py.write(empty_line)
        project_model_py.write("from sqlalchemy import (\n")
        project_model_py.write("    %s,\n" % "Column")

        for sqlalchemy_field in sqlalchemy_fields:
            project_model_py.write("    " + sqlalchemy_field + ",\n")

        project_model_py.write(")\n")

        project_model_py.write(empty_line)
        project_model_py.write("from sqlalchemy.ext.declarative import declarative_base\n")
        project_model_py.write(empty_line)
        project_model_py.write("from datetime import datetime\n")
        project_model_py.write(empty_line)
        project_model_py.write(empty_line)
        project_model_py.write("Base = declarative_base()\n")

        print '[info] write %s header success ...' % project_file_name
        tables = show_all_tables(project_name)
        duplicate_table = set()
        for table in tables:
            table_name = format_for_shard(table) if ignore_shard else table
            if table_name in duplicate_table:
                continue
            else:
                duplicate_table.add(table_name)

            table_desc = desc_table(project_name, table)
            class_name = format_for_hump(table_name)
            project_model_py.write(empty_line)
            project_model_py.write(empty_line)
            project_model_py.write("class %s(Base):\n" % class_name)
            project_model_py.write("    __tablename__ = \"%s\"\n" % table_name)
            project_model_py.write(empty_line)
            for column in table_desc:
                line = ""
                line += "    "
                line += column.get('name')
                line += " = "
                line += "Column"
                line += "("
                line += find_sqlalchemy_type(column.get('type'))
                line += ", "
                line += "name="
                line += "\""
                line += column.get("name")
                line += "\""
                if column.get("default_value") is not None and find_default_value(find_sqlalchemy_type(column.get('type')), column.get("default_value")):
                    line += ", default=%s" % find_default_value(find_sqlalchemy_type(column.get('type')), column.get("default_value"))
                if column.get("key_type") == "pri":
                    line += ", primary_key=True"
                if column.get("can_null") == "no":
                    line += ", nullable=False"
                else:
                    line += ", nullable=True"
                if column.get("extra") == "auto_increment":
                    line += ", autoincrement=True"
                line += ")\n"
                project_model_py.write(line)

            print '[info] write table 【%s】 model success ...' % table_name
