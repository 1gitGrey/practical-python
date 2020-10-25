# report.py
#
# Exercise 2.4

# __file__ = 'Data/portfolio.csv'



# reads portfolio files 
# define fn read_portfolio(filename)
# list of tuples is output

portfolio = []


def read_portfolio(filename): 

	for row in rows:
		holding = (row[0], int(row[1]), float(row[2]))
		portfolio.append(holding)

		
		
 


import csv

def portfolio_cost(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            nshares = int(row[1])
            price = float(row[2])
            total_cost += nshares * price
    return total_cost