# price of a house is 10,00,000 rupees. if buyer have good credit they need to put down 10% otherwise they need to
# put down 20%. print the down payment.

name = input('Enter name? ')
payment = 0

credit_score = input('if you have good credit then choose 1 else 2 ')

if credit_score == '1':
    payment = (1000000 * 10) / 100
else:
    payment = (1000000 * 20) / 100

if credit_score == '1':
    credit_score_value = 'good credit'
else:
    credit_score_value = 'bad credit'

print(name, ' have ', credit_score_value, ' hence they will have to put down sum of ', payment, ' dollars')
