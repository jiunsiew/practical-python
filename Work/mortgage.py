# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

extraPaymentStartMonth = 61  
extraPaymentEndMonth = 108
extraPayment = 1000

iMonth = 1
while principal > 0:
    
    if iMonth >= extraPaymentStartMonth and iMonth < extraPaymentEndMonth:
        tmpExtraPayment = extraPayment
    else:
        tmpExtraPayment = 0
    principal = principal * (1+rate/12) - (payment + tmpExtraPayment)
    total_paid = total_paid + payment + tmpExtraPayment
    print(iMonth, total_paid, principal)
    iMonth = iMonth + 1

print('Total paid:', total_paid)
print('Number of Months:', iMonth-1)