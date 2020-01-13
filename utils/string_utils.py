#! -*- coding:utf8 -*-

import os
import sys
import json

sys.path.append(os.path.abspath(".."))
reload(sys)
sys.setdefaultencoding("utf-8")


def is_number(string):
    try:
        float(string)
        return True
    except Exception as e:
        return False


def format_for_hump(string, separator="_"):
    if not string:
        return string

    if separator not in string:
        return string[:1].upper() + string[1:]

    string_blocks = string.split(separator)
    if not string_blocks:
        return string

    result = ""
    for string_block in string_blocks:
        result += string_block[:1].upper() + string_block[1:]

    return result


def format_for_shard(string, separator="_"):
    if not string:
        return string

    if separator not in string:
        return string

    string_blocks = string.split(separator)
    if not string_blocks:
        return string

    if is_number(string_blocks[-1:][0]):
        i = string.rfind(separator)
        if i < 0:
            return string
        return string[:i]
    else:
        return string


if __name__ == "__main__":
    # print format_for_hump("hello_gc")
    print format_for_shard("hello_gc_1")
