choice = int(input('if you want to enter weight in lbs enter 1 or else if you want to enter in kg enter 2 '))
answer = 0
weight = 0
if choice == 1:
    weight = int(input('Enter weight lbs : '))
    answer = weight * 0.45359237
    print('the weight in kg : ', answer)
else:
    weight = int(input('Enter weight in kg : '))
    answer = weight * 2.20462
    print('the weight in lbs : ', answer)
