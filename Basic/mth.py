strs = 'i am learning python'
count = len(strs)
print(count)
print(strs.capitalize())
print(strs.upper())

strs2 = "i am learning python. so i am here. i like to learn the different languages."
print(strs.find('o'))
print(strs2.find('learning'), strs.find('y'), 'in the same line')

print(strs2)
print(strs2.replace('here', 'there'))
print(strs2)


present = 'learning' in strs2
print(present)

is_present = 'exists' in strs2
print(is_present)

print('this is title', strs2.title())
