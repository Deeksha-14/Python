name = input('Enter name here : ')

if len(name) < 3:
    print('name must be atleast 3 character long')
elif len(name) > 50:
    print('name can be maximum of 50 chars ')
else:
    print('name looks good')
    
