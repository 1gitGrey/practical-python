# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
num_of_payments = 0 
sum_of_payments = 0



while principal > 0: 
    if num_of_payments < 12:
        payment = 3684.11
    else:
        payment = 2684.11
    principal = principal * (1+rate/12) - payment
    total_paid = payment + total_paid
    num_of_payments += 1
    print(num_of_payments, 'Total paid:' + str(total_paid))