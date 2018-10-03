#!/usr/bin/env python3
# -*- coding: utf8 -*-
#-------------------------------------------------------------------------------
# created on: 10-02-2018
# filename: database-manager.py
# author: brendan
# last modified: 10-02-2018 21:18
#-------------------------------------------------------------------------------
"""
Python code to manage the database where information is stored from the widget
"""
import sqlite3

database = 'finances.db'

def update_db(line1, line2, line3, wtype=['Income', 'Expense']):
    try:
        conn = sqlite3.connect(database)
    except Error as e:
        print(e)
    c = conn.cursor()
    if wtype == 'Income':
        c.execute('INSERT INTO income (value, source, method) VALUES (?,?,?)',
                  (line1, line2, line3))
    else:
        c.execute('INSERT INTO expense (value, reason, method) VALUES (?,?,?)',
                  (line1, line2, line3))





