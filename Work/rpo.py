#FFFFFFimport csv 
portfolio = {}
def read_prices(filename):
    f = open("Data/prices.csv", "r")
	rows = csv.reader(f)
	for row in rows:
		print(row)
		portfolio[row[0]] = float(row[1])

	return portfolio

