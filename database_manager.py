#!/usr/bin/env python3
# -*- coding: utf8 -*-
#-------------------------------------------------------------------------------
# created on: 10-02-2018
# filename: database-manager.py
# author: brendan
# last modified: 11-01-2018 12:23
#-------------------------------------------------------------------------------
"""
Python code to manage the database where information is stored from the widget
"""
import MySQLdb as mdb

def update_db(line1, line2, line3, wtype=['Income', 'Expense']):
    db = mdb.connect('localhost', 'finance_tracker', 'financesRFun', 'Finances')
    c = db.cursor()
    print(line1)
    try:
        line1 = float(line1)
    except ValueError:
        # catch and remove a dollar sign if it is there
        line1 = line1.replace('$', '')
        line1 = float(line1)
    print(line1)
    if wtype == 'Income':
        c.execute("""INSERT INTO income ( value, source, method ) VALUES
                  ( {:.2f}, "{}", "{}" )""".format(line1, line2, line3))
    else:
        c.execute("""INSERT INTO expense ( value, reason, method ) VALUES
                  ( {:.2f}, "{}", "{}" )""".format(line1, line2, line3))
    db.commit()
    db.close()





