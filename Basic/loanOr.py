name = input("what is your name? ")
has_high_income = int(input('Do you have high income? ans 0 or 1 '))
has_good_credit = int(input('do you have good credit? ans 0 or 1 '))
if bool(has_high_income) or bool(has_good_credit):
    print(f'{name} is Eligible to take loan')
else:
    print(f'{name} is not eligible to take loan')
