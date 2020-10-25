# report.py
#
# Exercise 2.4

# __file__ = 'Data/portfolio.csv'
import csv 
import os
import re
import sys
# reads portfolio files 
# define fn read_portfolio(filename)
# list of tuples is output
#portfolio = []
portfolio = {}

def read_portfolio(filename):

	with open(filename, 'rt') as file:
		rows = csv.reader(file)
		headers = next(rows)
		for row in rows:
			#holding = (row[0], int(row[1]), float(row[2]))
			#portfolio.append(holding)
			portfolio["name"] = row[0]
			portfolio["shares"] = int(row[1])
			portfolio["price"] = float(row[2])
			nshares = int(row[1])
			price = float(row[2])
			cost = nshares * price 

	return portfolio

