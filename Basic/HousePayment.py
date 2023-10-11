# price of a house is 10,00,000 rupees. if buyer have good credit they need to put down 10% otherwise they need to
# put down 20%. print the down payment.

Payment = 0
name = input('What is  your name? Choose between a & b? ')
if name == 'a':
    Payment = (1000000 * 10) / 100
else:
    Payment = (1000000 * 20) / 100

print('you have to put down', Payment)
