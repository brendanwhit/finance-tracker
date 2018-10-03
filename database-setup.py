#!/usr/bin/env python3
# -*- coding: utf8 -*-
#-------------------------------------------------------------------------------
# created on: 10-02-2018
# filename: database-setup.py
# author: brendan
# last modified: 10-02-2018 20:36
#-------------------------------------------------------------------------------
"""
Short script to create the databases
"""
import sqlite3

conn = sqlite3.connect('finances.db')

c = conn.cursor()

# create the income table
c.execute('''CREATE TABLE income (
    id INT PRIMARY KEY,
    cur_timestamp TIMESTAMP(8),
    value NUMERIC(20),
    source VARCHAR(200),
    method VARCHAR(100))''')

# create the expense table
c.execute('''CREATE TABLE expense (
    id INT PRIMARY KEY,
    cur_timestamp TIMESTAMP(8),
    value NUMERIC(20),
    reason VARCHAR(200),
    method VARCHAR(200))''')

conn.commit()
conn.close()

