#!/usr/bin/env python3
# -*- coding: utf8 -*-
#-------------------------------------------------------------------------------
# created on: 10-02-2018
# filename: database-setup.py
# author: brendan
# last modified: 11-01-2018 18:58
#-------------------------------------------------------------------------------
"""
Short script to create the databases
"""
import MySQLdb as mdb

finances_db = mdb.connect('localhost', 'finance_tracker', 'financesRFun',
                          'Finances')

cur = finances_db.cursor()

# create the income table
cur.execute('''CREATE TABLE income (
    id INT NOT NULL AUTO_INCREMENT,
    cur_time DATETIME default CURRENT_TIMESTAMP,
    value DECIMAL(20,2),
    source VARCHAR(255),
    method VARCHAR(155),
    PRIMARY KEY(id)
)''')

# create the expense table
cur.execute('''CREATE TABLE expense (
    id INT NOT NULL AUTO_INCREMENT,
    cur_time DATETIME default CURRENT_TIMESTAMP,
    value DECIMAL(20,2),
    reason VARCHAR(200),
    method VARCHAR(200),
    PRIMARY KEY(id)
)''')

finances_db.commit()
finances_db.close()

