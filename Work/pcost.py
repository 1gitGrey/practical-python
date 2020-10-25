#!/usr/bin/python3
# pcost.py


total_cost = 0 
with open('Data/portfolio.csv', 'rt') as filename:
    header_data = next(filename).split(',')
    content = filename.read() 
    print(header_data)
    for line in content:
    	#print(content) 
    	print(line)                                                                                                                                                                                                           
    	#num_of_shares = float(line[1])
    	#purchase_price = float(line[2])
    	#total_cost += num_of_shares * purchase_price
