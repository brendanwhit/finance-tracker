#!/usr/bin/env python3
# -*- coding: utf8 -*-
#-------------------------------------------------------------------------------
# created on: 09-30-2018
# filename: finance-tracker.py
# author: brendan
# last modified: 10-02-2018 21:08
#-------------------------------------------------------------------------------
"""
An interactive widget for tracking my finances. Update this feature list as the
project progesses
"""
import tkinter as tk
from database_manager import update_db


def makeentry(parent, caption, row, width=None, **options):
    tk.Label(parent, text=caption).grid(row=row)
    entry = tk.Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.grid(row=row, column=1)
    return entry


class Widget():
    
    def __init__(self, wtype=['Expense', 'Income']):      
        self.widget = tk.Tk()
        self.wtype = wtype
        
    def loginfo(self):
        value = self.line1.get()
        self.line1.delete(0, tk.END)
        line2 = self.line2.get()
        self.line2.delete(0, tk.END)
        method = self.line3.get()
        self.line3.delete(0, tk.END)
        update_db(value, line2, method, self.wtype)

    def makeWidget(self):
        self.line1 = makeentry(self.widget, 'Value:', 0)
        if self.wtype == 'Expense':
            self.line2 = makeentry(self.widget, 'Reason:', 1)
        else:
            self.line2 = makeentry(self.widget, 'Source:', 1)
        self.line3 = makeentry(self.widget, 'Method:', 2)
        self.log = tk.Button(self.widget, text='log', width=10, 
                             command=self.loginfo)
        self.log.grid(row=3, columnspan=2)
        self.close = tk.Button(self.widget, text='close', width=10,
                               command=self.widget.destroy)
        self.close.grid(row=4, columnspan=2)


def expense_widget():
    Widget('Expense').makeWidget()


def income_widget():
    Widget('Income').makeWidget()   


master = tk.Tk()

tk.Button(master, text='income', width=10, command=income_widget).pack()
tk.Button(master, text='expense', width=10, command=expense_widget).pack()
tk.Button(master, text='close', width=10, command=master.destroy).pack()

tk.mainloop()
