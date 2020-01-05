#! -*-coding:utf8 -*-

import os

program_path = os.path.abspath("..")


def gen_file_abspath(file_path):
    return program_path + "/" + file_path
