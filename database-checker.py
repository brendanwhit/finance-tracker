#!/usr/bin/env python3
# -*- coding: utf8 -*-
#-------------------------------------------------------------------------------
# created on: 10-02-2018
# filename: database-checker.py
# author: brendan
# last modified: 10-02-2018 21:22
#-------------------------------------------------------------------------------
"""
A short script to check the database and print all of its contents
"""
import sqlite3

db = 'finances.db'
conn = sqlite3.connect(db)
c = conn.cursor()
c.execute('SELECT * FROM income')


