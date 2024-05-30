Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
nums = [25, 12, 14, 95, 36]
nums
[25, 12, 14, 95, 36]
nums[0]
25
nums[4]
36
nums[2:]
[14, 95, 36]
nums[-1]
36
nums[-5]
25
names = ['apple', 'banana', 'grapes']
names
['apple', 'banana', 'grapes']
values = [9.5, 'apple', 25]
values
[9.5, 'apple', 25]
 mil = [nums, names]
 
SyntaxError: unexpected indent
mil = [nums, names]
mil
[[25, 12, 14, 95, 36], ['apple', 'banana', 'grapes']]
nums.append(45)
nums
[25, 12, 14, 95, 36, 45]
nums.insert(2, 77)
nums
[25, 12, 77, 14, 95, 36, 45]
nums.remove(12)
nums
[25, 77, 14, 95, 36, 45]
nums.count
<built-in method count of list object at 0x000001AD19942200>
nums.count()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    nums.count()
TypeError: list.count() takes exactly one argument (0 given)
nums.count(1)
0
>>> nums.count(14)
1
>>> names.count('banana')
1
>>> nums.pop(5)
45
>>> nums
[25, 77, 14, 95, 36]
>>> nums.pop()
36
>>> nums
[25, 77, 14, 95]
>>> del nums[2:]
>>> nums
[25, 77]
>>> nums.extend([29, 10, 14, 36])
>>> nums
[25, 77, 29, 10, 14, 36]
>>> nums.min()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    nums.min()
AttributeError: 'list' object has no attribute 'min'
>>> min
<built-in function min>
>>> min(nums)
10
>>> max(nums)
77
>>> sum(nums)
191
>>> nums.sort()
>>> nums
[10, 14, 25, 29, 36, 77]
>>> print(r'Deeksha \n Kushwah')
Deeksha \n Kushwah
>>> print('Deeksha \n Kushwah')
Deeksha 
 Kushwah
>>> name = "Deeksha"
>>> print(name[-3])
s
>>> name[-3]
's'
