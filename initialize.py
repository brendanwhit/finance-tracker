#!/usr/bin/env python3
# -*- coding: utf8 -*-
#-------------------------------------------------------------------------------
# created on: 09-30-2018
# filename: test.py
# author: brendan
# last modified: 10-23-2018 16:07
#-------------------------------------------------------------------------------
"""
File made to test the ssh connection, we need to test 1 more time. So here
are some small edits.
"""
import MySQLdb as mdb

# use the password that is saved outside of the directory
pword_file = '../password.txt'
with open(pword_file, 'r') as f:
    root_password = f.readline()

db = mdb.connect('localhost', 'root', root_password)

cur = db.cursor()

# create the database Finances
cur.execute('CREATE DATABASE Finances')

# then create the finance_tracker user, which will control this database
cur.execute('CREATE USER "finance_tracker"@"localhost" IDENTIFIED BY \
            "finances"')

# give the finance tracker all privileges
cur.execute('GRANT ALL PRIVILEGES ON Finances.* TO \
            "finance_tracker"@"localhost"')

