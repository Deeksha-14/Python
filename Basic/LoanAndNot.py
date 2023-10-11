name = input("what is your name? ")
has_high_income = int(input('Do you have high income? ans 0 or 1 '))
not_criminal_record = int(input('do you have criminal record? ans 0 or 1 '))
if bool(has_high_income) and not bool(not_criminal_record):
    print(f'{name} is Eligible to take loan')
else:
    print(f'{name} is not eligible to take loan')
