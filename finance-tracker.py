#!/usr/bin/env python3
# -*- coding: utf8 -*-
#-------------------------------------------------------------------------------
# created on: 09-30-2018
# filename: finance-tracker.py
# author: brendan
# last modified: 10-01-2018 10:47
#-------------------------------------------------------------------------------
"""
An interactive widget for tracking my finances. Update this feature list as the
project progesses
"""
import tkinter as tk

master = tk.Tk()

def makeentry(parent, caption, row, width=None, **options):
    tk.Label(parent, text=caption).grid(row=row)
    entry = tk.Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.grid(row=row, column=1)
    return entry


def expense_widget():
    def logexpense():
        expense = line1.get()
        line1.delete(0,tk.END)
        reason = line2.get()
        line2.delete(0,tk.END)
        method = line3.get()
        line3.delete(0,tk.END)
        print(expense, reason, method)

    expense = tk.Tk()
    line1 = makeentry(expense, 'Expense:', 0)
    line2 = makeentry(expense, 'Reason:', 1)
    line3 = makeentry(expense, 'Method:', 2)
    log = tk.Button(expense, text='log', width=10, command=logexpense)
    log.grid(row=3, columnspan=2)
    close = tk.Button(expense, text='close', width=10, command=expense.destroy)
    close.grid(row=4, columnspan=2)

def income_widget():
    def logincome():
        income = line1.get()
        line1.delete(0, tk.END)
        reason = line2.get()
        line2.delete(0,tk.END)
        method = line3.get()
        line3.delete(0,tk.END)
        print(income, reason, method)

    income = tk.Tk()
    line1 = makeentry(income, 'Income:', 0)
    line2 = makeentry(income, 'Reason:', 1)
    line3 = makeentry(income, 'Method:', 2)
    log = tk.Button(income, text='log', width=10, command=logincome)
    log.grid(row=3, columnspan=2)
    close = tk.Button(income, text='close', width=10, command=income.destroy)
    close.grid(row=4, columnspan=2)
    


tk.Button(master, text='income', width=10, command=income_widget).pack()
tk.Button(master, text='expense', width=10, command=expense_widget).pack()
tk.Button(master, text='close', width=10, command=master.destroy).pack()

tk.mainloop()
