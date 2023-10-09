course = 'python'
print(course)
print(course[5])
print(course[4])
print(course[3])
print(course[2])
print(course[1])
print(course[0])
print('---')
print(course[-0])
print(course[-1])
print(course[-2])
print(course[-3])
print(course[-4])
print(course[-5])
print('---')
# print(course[6]) IndexError: string index out of range


print(course[0:3])
print(course[0:])
print(course[:6])
print(course[:])  # Used to copy or clone
print(course)


another = course[:]
print('This is another : ', another)



print(course[1:-1])
