Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
2 + 3
5
x = 10
y = 12
x + y
22
x + 3
13
x + y
22
x = 9
x + y
21
>>> x
9
>>> y
12
>>> _ + 2
14
>>> name = 'youtube'
>>> name + 'hi"
SyntaxError: unterminated string literal (detected at line 1)
>>> name + 'hi'
'youtubehi'
>>> name[0]
'y'
>>> name[-1]
'e'
>>> name[8]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    name[8]
IndexError: string index out of range
>>> name[6]
'e'
>>> name[0:2]
'yo'
>>> name[:2]
'yo'
>>> name[-2]
'b'
>>> name[-7]
'y'
>>> name[1:4]
'out'
>>> name[1:]
'outube'
>>> name[:4]
'yout'
>>> name[3:10]
'tube'
>>> 'my' + name[3:]
'mytube'
>>> myname = 'Deeksha k'
>>> len(myname)
9
