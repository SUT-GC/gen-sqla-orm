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
    desc_table,
    show_create_table
)

from gensqlalorm.config import (
    DBConfig,
    set_db_config
)

if __name__ == "__main__":

    write_file = open("/Users/gc/Documents/table_desc.csv", "w+")

    configs = {
        # "PayCommodity": DBConfig(
        #     host="xxxx",
        #     port=3306,
        #     user="soul",
        #     pawd="xxxx",
        #     name="pay-commodity"),
    }

    for project, config in configs.items():
        set_db_config({project: config})
        all_tables = show_all_tables(project)
        table_list = []
        for table in all_tables:
            table_format_name = format_for_shard(table)
            if table_format_name in table_list:
                continue

            table_list.append(table_format_name)
            table_desc = show_create_table(project, table)

            for column_info in table_desc:
                write_file.write("%s,%s,%s,%s\n" % (table_format_name, column_info.get("column"), column_info.get("type"), column_info.get("comment")))

            print project, format_for_shard(table), "done"
