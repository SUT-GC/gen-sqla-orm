#! -*- coding:utf8 -*-
import sys
import os

sys.path.append(os.path.abspath(".."))
reload(sys)
sys.setdefaultencoding("utf-8")

from utils import (
    is_number
)


def check_url(input_url):
    """
    check url like localhost:3306/db_name?username=root&password=123
    """
    if not input_url:
        return False

    # check localhost
    g1 = input_url.split(":")
    if len(g1) != 2:
        return False
    if not g1[0]:
        return False
    if not g1[1]:
        return False

    # check 3306
    g2 = g1[1].split("/")
    if len(g2) != 2:
        return False
    if not g2[0]:
        return False
    if not g2[1]:
        return False
    if not is_number(g2[0]):
        return False

    # check db_name
    g3 = g2[1].split("?")
    if len(g3) != 2:
        return False
    if not g3[0]:
        return False
    if not g3[1]:
        return False

    # check username=root&password=123
    g4 = g3[1].split("&")
    if len(g4) != 2:
        return False
    if not g4[0]:
        return False
    if not g4[1]:
        return False

    g5 = g4[0].split("=")
    g6 = g4[1].split("=")
    if len(g5) != 2:
        return False
    if len(g6) != 2:
        return False
    if g5[0] != "username":
        return False
    if not g5[1]:
        return False
    if g6[0] != "password":
        return False
    if not g6[1]:
        return False

    return True


def check_path(input_path):
    if not input_path:
        return False

    if not os.path.exists(input_path):
        print '[%s] not exists' % input_path
        return False

    if not os.access(input_path, os.W_OK):
        print '[%s] not access' % input_path
        return False

    return True


def check_file(input_path):
    if not input_path:
        return False

    if not os.path.exists(input_path):
        print '[%s] not exists' % input_path
        return False

    if not os.access(input_path, os.R_OK):
        print '[%s] not access' % input_path
        return False

    return True


def gen_console():
    print ''
    print ''
    print '''----------------------------------- welcome -----------------------------------'''
    print '''
    step 1 select mode:
        c: config mode, read db config from config file. you can read README.md to get the file layout 
        u: url mode, read db config from url. like localhost:3306/db_name?username=root&password=123
    step 2 input the path where to output:
        the path use to output orm class file, like '/gc/orm/'
    '''
    while True:
        select_mode = raw_input("place input the mode what do you want to use ( c / u ) : ")
        if not select_mode or (select_mode.lower() != 'c' and select_mode.lower() != 'u'):
            print 'input mode error, place input c / u...'
            continue

        if select_mode.lower() == 'u':
            input_url = raw_input("place input db config url : ")
            if not check_url(input_url):
                print "input url error, place input url like localhost:3306/db_name?username=root&password=123"
                continue
            input_out_path = raw_input("place input out orm class path : ")
            if not check_path(input_out_path):
                print "input path error, place input path like /gc/orm/"
                continue
            print 'set url success...'
            break
        elif select_mode.lower() == 'c':
            input_config_path = raw_input("place input db config path : ")
            if not check_file(input_config_path):
                print "input config file path error, place input path like /gc/orm/config.yml"
                continue
            input_out_path = raw_input("place input out orm class path : ")
            if not check_path(input_out_path):
                print "input path error, place input path like /gc/orm/"
                continue
            print 'set config success...'
            break
        else:
            continue

    while True:
        gen_now = raw_input("if you want gen orm class now ? ( y / n ) :")
        if not gen_now or (gen_now.lower() != 'y' and gen_now.lower() != 'n'):
            print 'input mode error, place input c / u...'
            continue
        if gen_now.lower() == "y":
            print 'start to gen...'
            break
        else:
            print 'stop the program...'
            break

    print '''----------------------------------- finish -----------------------------------'''


if __name__ == "__main__":
    gen_console()
