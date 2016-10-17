#!/usr/bin/python
# -*- coding: utf-8 -*-

from pprint import pprint
from mysql import connector
import mysql.connector.errors as conn_error


def createConn():
    try:
        global conn
        conn = connector.connect(host='sql6.freemysqlhosting.net', user='sql6138787',
                                 passwd='hrcuwyGIrR', db='sql6138787')
        global cursor
        cursor = conn.cursor()

    except (Exception, conn_error.Error), e:
        print e


def closeConn():
    try:
        cursor.close()
        conn.close()
    except (Exception, conn_error.Error), e:
        print e


def findGender(name):

    try:

        createConn()
        cursor.execute(
            'SELECT GENDER FROM collections WHERE collections.NAME="' + name + '"')
        gender = cursor.fetchone()

        if gender is not None:
            return "%s is %s" % (name, gender[0])
        else:
            print "%s name not found" % name
            case = raw_input(
                "want to add %s to database (Y/n): " % name).upper()
            if case == 'Y':
                result_add = addName(name)
                return result_add
            else:
                return "Thank You."

    except (Exception, conn_error.Error), e:
        print e
        closeConn()
    finally:
        closeConn()


def readName():
    name = raw_input('Enter a Name: ').upper()
    result = findGender(name)

    print result


def addName(name):
    try:
        createConn()
        gender = raw_input("what is %s's gender (male/female) : "%name).lower()
        sql="INSERT INTO collections VALUES('%s','%s')"%(name,gender)
        cursor.execute(sql)
        conn.commit()

        return "%s added"%name
    except (Exception, conn_error.Error) as e:
        print e
    finally:
        closeConn()



if __name__ == '__main__':
    readName()
