Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s = 'Learn to Program'
>>> s(0)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    s(0)
TypeError: 'str' object is not callable
>>> s[0]
'L'
>>> s[1]
'e'
>>> s[2]
'a'
>>> s[-1]
'm'
>>> s[-2]
'a'
>>> s[-3]
'r'
>>> s[0:5]
'Learn'
>>> s[9:16]
'Program'
>>> s[9:len(s)]
'Program'
>>> s[9:]
'Program'
>>> s[:8]
'Learn to'
>>> s[1:8]
'earn to'
>>> s[1:-8]
'earn to'
>>> s[-15:-8]
'earn to'
>>> s = 'Call Me Maybe'
>>> s[12]
'e'
>>> s[13]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    s[13]
IndexError: string index out of range
>>> s[-0]
'C'
>>> s[-1]
'e'
>>> s[1:]
'all Me Maybe'
>>> s[:2]
'Ca'
>>> s[:4]
'Call'
>>> s[:5] +'ed' + s[5:]
'Call edMe Maybe'
>>> s = 'Learn to Program'
>>> s[:5] +'ed' + s[5:]
'Learned to Program'
>>> 'Learned to Program'
'Learned to Program'
>>> s = s[:5] +'ed' + s[5:]
>>> s =
SyntaxError: invalid syntax
>>> s
'Learned to Program'
>>>  s = 'Call Me Maybe'
 
SyntaxError: unexpected indent
>>> s = 'Call Me Maybe'
>>> s[-5:]=’Perhaps’
SyntaxError: invalid character in identifier
>>> s[-5:]='Perhaps'
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    s[-5:]='Perhaps'
TypeError: 'str' object does not support item assignment
>>> s = s[:-5] + ’Perhaps’
SyntaxError: invalid character in identifier
>>> s = s[:-5] + 'Perhaps'
>>> s
'Call Me Perhaps'
>>> s[-5:]= 'Perhaps'
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    s[-5:]= 'Perhaps'
TypeError: 'str' object does not support item assignment
>>> s = s[0:-5] +'Perhaps'
>>> s
'Call Me PePerhaps'
>>> s = 'Call Me Maybe'
>>> s = s[0:-5] +'Perhaps'
>>> s
'Call Me Perhaps'
>>> s = s-s[-5:]+'Perhaps'
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    s = s-s[-5:]+'Perhaps'
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> s = 'Call Me Maybe'
>>> s = s - s[-5:] + 'Perhaps'
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    s = s - s[-5:] + 'Perhaps'
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> import math
>>> math.sqrt(4.0)
2.0
>>> white_rabbitt = "I´m late! I´m late! For a very important date!"
>>> white_rabbitt.lower()
'i´m late! i´m late! for a very important date!'
>>> white_rabbitt
'I´m late! I´m late! For a very important date!'
>>> dir(white_rabbitt)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(str.lower)
Help on method_descriptor:

lower(self, /)
    Return a copy of the string converted to lowercase.

>>> help(str.count)
Help on method_descriptor:

count(...)
    S.count(sub[, start[, end]]) -> int
    
    Return the number of non-overlapping occurrences of substring sub in
    string S[start:end].  Optional arguments start and end are
    interpreted as in slice notation.

>>> white_rabbitt.count('ate')
3
>>> 'computer'.capitalize()
'Computer'
>>> white_rabbitt.find('late')
4
>>> white_rabbitt.find('late', 7)
14
>>> >>> white_rabbitt.find('late', 7)
14
>>> white_rabbitt.find('moogah')
SyntaxError: invalid syntax
>>> white_rabbitt.find('Late')
-1
>>> white_rabbitt.find('moogah')
-1
>>> white_rabbitt.rfind('late')
14
>>> s = "  I'm feeling spaced out. "
>>> s.lstrip()
"I'm feeling spaced out. "
>>> s.rstrip()
"  I'm feeling spaced out."
>>> s.strip()
"I'm feeling spaced out."
>>> queen_of_hearts= 'Off with their heads!'
>>> queen_of_hearts.find('hearts,7)
		     
SyntaxError: EOL while scanning string literal
>>> queen_of_hearts.find('hearts',7)
-1
>>> queen_of_hearts.find('hearts')
-1
>>> white_queen = "Jam tomorrow and jam yesterday - but never jam today."
>>> queen_of_hearts.find('heads')
15
>>> s = 'Hi there !'
>>> for char in s:
	prin(char)

	
Traceback (most recent call last):
  File "<pyshell#76>", line 2, in <module>
    prin(char)
NameError: name 'prin' is not defined
>>> for char in s:
	print(char)

	
H
i
 
t
h
e
r
e
 
!
>>> for char in s:
	print(char)
	print(char)

	
H
H
i
i
 
 
t
t
h
h
e
e
r
r
e
e
 
 
!
!
>>> for vowel in 'aeiou':
    print("I'd like to buy a", vowel)

    
I'd like to buy a a
I'd like to buy a e
I'd like to buy a i
I'd like to buy a o
I'd like to buy a u
>>> 
=== RESTART: C:/Users/edgar/Desktop/Universities/Toronto/loops_over_str.py ===
>>> count_vowels ('Happy Anniversary!')
5
>>> count_vowels('xyz')
0
>>> 
=== RESTART: C:/Users/edgar/Desktop/Universities/Toronto/loops_over_str.py ===
>>> collect_vowels ('Happy Anniversary!')
'aAiea'
>>> collect_vowels ('xyz')
''
>>> 
[DEBUG ON]
>>> 
[DEBUG OFF]
>>> def collect_vowels(s):
    '''(str) -> str

    Return the vowels from s. Do not treat the
    letter y as vowel
    
    >>>collect_vowels ('Happy Anniversary!')
    'aAiea'
    >>>collect_vowels ('xyz')
    '''

    vowels = ''
    for char in s:
        if char in 'aeiouAEIOU':
            vowels = vowels + char

    return vowels        
    
    
def count_vowels(s):
    ''' (str) -> int
    Return the number of vowels in s. Do not treat the
    letter y as vowel

    >>> count_vowels ('Happy Anniversary!')
    5
    >>> count_vowels('xyz')
    0
    '''


    num_vowels = 0

    for char in s:
        if char in 'aeiouAEIOU':
            num_vowels  = num_vowels + 1

    return num_vowels
[DEBUG ON]
>>> 
[DEBUG OFF]
>>> 
[DEBUG ON]
>>> 
=== RESTART: C:/Users/edgar/Desktop/Universities/Toronto/loops_over_str.py ===
[DEBUG OFF]
>>> 
>>> 
========= RESTART: C:/Users/edgar/Desktop/Universities/Toronto/a2.py =========
>>> 
========= RESTART: C:/Users/edgar/Desktop/Universities/Toronto/a2.py =========
>>> 
========= RESTART: C:/Users/edgar/Desktop/Universities/Toronto/a2.py =========
>>> 
========= RESTART: C:/Users/edgar/Desktop/Universities/Toronto/a2.py =========
>>> 
========= RESTART: C:/Users/edgar/Desktop/Universities/Toronto/a2.py =========
>>> 
========= RESTART: C:/Users/edgar/Desktop/Universities/Toronto/a2.py =========
>>> 
========= RESTART: C:/Users/edgar/Desktop/Universities/Toronto/a2.py =========
>>> 
========= RESTART: C:/Users/edgar/Desktop/Universities/Toronto/a2.py =========
>>> 
========= RESTART: C:/Users/edgar/Desktop/Universities/Toronto/a2.py =========
>>> 
========= RESTART: C:/Users/edgar/Desktop/Universities/Toronto/a2.py =========
>>> 
========= RESTART: C:/Users/edgar/Desktop/Universities/Toronto/a2.py =========
>>> 'bit' in 'habit'
True
>>> len('deed')==4
True
>>> 'sit' in 'tis'
False
>>> len('deed')==2
False
>>> len('')
0
>>> dance_style = 'Gangnam'
>>> dance_style[4]
'n'
>>> dance_style[-3]
'n'
>>> dance_style[-4]
'g'
>>> dance_style[3]
'g'
>>> title = 'Queen'
>>> title[2]
'e'
>>> title[1]
'u'
>>> s = 'pineapple'
>>> s[4:9]
'apple'
>>> s[5:]
'pple'
>>> s[-5:]
'apple'
>>> s[-5:-1]
'appl'
>>> prefix = 'mad'
>>> prefix[:1]+prefix[1:3]+prefix[-2]+prefix[0]
'madam'
>>> 'apple'.upper().isupper()
True
>>> 'abc123'.isalnum()
True
>>> 'apple'.upper().islower()
False
>>> '12.34'.isalnum()
False
>>> s.lower()ors.upper()ors.isdigit()
SyntaxError: invalid syntax
>>> s.lower() or s.upper() or s.isdigit()
'pineapple'
>>> digits = '0123456789'
result = 100

for digit in digits:
    result = result - int(digit)

print(result)
SyntaxError: multiple statements found while compiling a single statement
>>> message = 'Happy 29th!'
new_message = ''

for char in message:
    new_message = new_message + str((int(char) + 1) % 10)

print(new_message)
SyntaxError: multiple statements found while compiling a single statement
>>> 
======= RESTART: C:/Users/edgar/Desktop/Universities/Toronto/exam4.py =======
>>> common_chars
<function common_chars at 0x015ED738>
>>> 
======= RESTART: C:/Users/edgar/Desktop/Universities/Toronto/exam4.py =======
>>> resw
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    resw
NameError: name 'resw' is not defined
>>> res
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    res
NameError: name 'res' is not defined
>>> 
======= RESTART: C:/Users/edgar/Desktop/Universities/Toronto/exam4.py =======
>>> 
======= RESTART: C:/Users/edgar/Desktop/Universities/Toronto/exam4.py =======
>>> common_chars('abc', 'ad')
'a'
>>> common_chars('a', 'a')
'a'
>>> common_chars('abb', 'ab')
'ab'
>>> common_chars('abracadabra', 'ra')
'ra'
>>> 
======= RESTART: C:/Users/edgar/Desktop/Universities/Toronto/exam4.py =======
>>> common_chars('abc', 'ad')
'a'
>>> common_chars('a', 'a')
'a'
>>> common_chars('abb', 'ab')
'abb'
>>> common_chars('abracadabra', 'ra')
'araaara'
>>> num = 2
>>> while num < 100:
	num = num * 2
	print(num)

4
8
16
32
64
128
>>> num = 10
>>> while num < 100:
	num = num * 2
	print(num)

	
20
40
80
160
>>> num = 6
while num > 0:
    num = num - 2
    print(num)
    
SyntaxError: multiple statements found while compiling a single statement
>>> num = 6
>>> while num > 0:
    num = num - 2
    print(num)

    
4
2
0
>>> s = 'hello'
>>> for char in s:
	print(char)

	
h
e
l
l
o
>>> i = 0
>>> while not (s[i] in 'aeiouAEIOU'):
	print(s[i])
	i = i + 1

	
h
>>> s = 'there'
>>> i = 0
>>> while not (s[i] in 'aeiouAEIOU'):
	print(s[i])
	i = i + 1

	
t
h
>>> s = 'xyz'
>>> i = 0
>>> while not (s[i] in 'aeiouAEIOU'):
	print(s[i])
	i = i + 1

	
x
y
z
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    while not (s[i] in 'aeiouAEIOU'):
IndexError: string index out of range
>>> s[0]
'x'
>>> s[1]
'y'
>>> s[2]
'z'
>>> i = 0
>>> s = 'xyz'
>>> while i < len(s) and not (s[i] in 'aeiouAEIOU'):
	print(s[i])
	i = i + 1

	
x
y
z
>>> 
==== RESTART: C:/Users/edgar/Desktop/Universities/Toronto/while_loops.py ====
>>> up_to_vowel('hello')
'e'
>>> 
==== RESTART: C:/Users/edgar/Desktop/Universities/Toronto/while_loops.py ====
>>> up_to_vowel('hello')
'h'
>>> up_to_vowel('there')
'th'
>>> up_to_vowel('cs')
'cs'
>>> 
==== RESTART: C:/Users/edgar/Desktop/Universities/Toronto/while_loops.py ====
>>> get_answer('Are you tired? Answer yes or no.')
Are you tired? Answer yes or no.yes
'yes'
>>> grades = [80, 90, 70]
>>> grades[0]
80
>>> grades[1]
90
>>> grades[2]
70
>>> grades[1:2]
[90]
>>> grades[0:2]
[80, 90]
>>> 80 in grades
True
>>> 60 in grades
False
>>> len(grades)
3
>>> min(grades)
70
>>> max(grades)
90
>>> subjects = ['bio','cs','math','history']
>>> sum(grades)
240
>>> len(subjects)
4
>>> min(subjects)
'bio'
>>> max(subjects)
'math'
>>> sum(subjects)
Traceback (most recent call last):
  File "<pyshell#185>", line 1, in <module>
    sum(subjects)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> temperatures = [18, 20, 22.5, 24]
>>> temperatures[1]
20
>>> temperatures [18,20,22.5,24]
Traceback (most recent call last):
  File "<pyshell#188>", line 1, in <module>
    temperatures [18,20,22.5,24]
TypeError: list indices must be integers or slices, not tuple
>>> temperatures [18, 20, 22.5, 24]
Traceback (most recent call last):
  File "<pyshell#189>", line 1, in <module>
    temperatures [18, 20, 22.5, 24]
TypeError: list indices must be integers or slices, not tuple
>>> temperatures [18, 20, 22, 24]
Traceback (most recent call last):
  File "<pyshell#190>", line 1, in <module>
    temperatures [18, 20, 22, 24]
TypeError: list indices must be integers or slices, not tuple
>>> temperatures = [18, 20, 22.5, 24]
>>> temperatures[-1]
24
>>> temperatures[4]
Traceback (most recent call last):
  File "<pyshell#193>", line 1, in <module>
    temperatures[4]
IndexError: list index out of range
>>> temperatures[3:0]
[]
>>> temperatures[3:4]
[24]
>>> len([1,2,3,4])
4
>>>  len(["math"])
 
SyntaxError: unexpected indent
>>> min([10,8,4])
4
>>> sum([4])
4
>>> street_address = [10,'Main Street']
>>> for grade in grades:
	print(grade)

	
80
90
70
>>> for item in subjects:
	print(item)

	
bio
cs
math
history
>>> s = ""
names = ["Alice", "Bob", "Carol"]
for name in names:
    s = s + name
    
SyntaxError: multiple statements found while compiling a single statement
>>> s = ""
>>> names = ["Alice", "Bob", "Carol"]
>>> for name in names:
    s = s + name

    
>>> s
'AliceBobCarol'
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> colours = []
>>> prompt = 'Enter another one of your favourite colours (type return to end):'
>>> colour = input(prompt)
Enter another one of your favourite colours (type return to end): blue
>>> colour
' blue'
>>> colours
[]
>>> while colour != '':
	colours.append(colour)
	colour = input(prompt)

	
Enter another one of your favourite colours (type return to end):yellow
Enter another one of your favourite colours (type return to end):brown
Enter another one of your favourite colours (type return to end):
>>> colours
[' blue', 'yellow', 'brown']
>>> colours.extend(['hot pink','neon green'])
>>> colours
[' blue', 'yellow', 'brown', 'hot pink', 'neon green']
>>> colours.pop()
'neon green'
>>> colours
[' blue', 'yellow', 'brown', 'hot pink']
>>> colours.pop(2)
'brown'
>>> colours
[' blue', 'yellow', 'hot pink']
>>> colours.remove('black')
Traceback (most recent call last):
  File "<pyshell#231>", line 1, in <module>
    colours.remove('black')
ValueError: list.remove(x): x not in list
>>> if colours.count('yellow') > 0:
	colours.remove('yellow')

	
>>> colours
[' blue', 'hot pink']
>>> if colours.count('yellow') > 0:
	colours.remove('yellow')

	
>>> if 'yellow' in colours:
	colours.remove('yellow')

	
>>> grades = [70,60,75,60]
>>> list.pop()
     remove and return the item at the end of the list
     (optional index to remove from anywhere)
     
SyntaxError: multiple statements found while compiling a single statement
>>> grades.pop()
60
>>> grades.pop(60)
Traceback (most recent call last):
  File "<pyshell#245>", line 1, in <module>
    grades.pop(60)
IndexError: pop index out of range
>>> colours.extend('auburn','taupe', 'magenta')
Traceback (most recent call last):
  File "<pyshell#246>", line 1, in <module>
    colours.extend('auburn','taupe', 'magenta')
TypeError: extend() takes exactly one argument (3 given)
>>> colours.extend(['auburn','taupe', 'magenta'])
>>> colours
[' blue', 'hot pink', 'auburn', 'taupe', 'magenta']
>>> colours.sort()
>>> colours
[' blue', 'auburn', 'hot pink', 'magenta', 'taupe']
>>> colours.reverse()
>>> colours
['taupe', 'magenta', 'hot pink', 'auburn', ' blue']
>>> colours.insert(-2,'brown')
>>> colours
['taupe', 'magenta', 'hot pink', 'brown', 'auburn', ' blue']
>>> colours.index('neon green')
Traceback (most recent call last):
  File "<pyshell#255>", line 1, in <module>
    colours.index('neon green')
ValueError: 'neon green' is not in list
>>> if 'hot pink' in colours:
	where = colours.index('hot pink')
	colours.pop(where)

	
'hot pink'
>>> colours
['taupe', 'magenta', 'brown', 'auburn', ' blue']
>>> 
====== RESTART: C:/Users/edgar/Desktop/Universities/Toronto/exercise.py ======
Traceback (most recent call last):
  File "C:/Users/edgar/Desktop/Universities/Toronto/exercise.py", line 5, in <module>
    interrupted(greeting)
  File "C:/Users/edgar/Desktop/Universities/Toronto/exercise.py", line 2, in interrupted
    s[-1] = "-"
TypeError: 'str' object does not support item assignment
>>> 
====== RESTART: C:/Users/edgar/Desktop/Universities/Toronto/exercise.py ======
>>> for num in range(10):
	print(num)

	
0
1
2
3
4
5
6
7
8
9
>>> help(range)

>>> help(range)

>>> 
=============================== RESTART: Shell ===============================
>>> help(range)
Help on class range in module builtins:

class range(object)
 |  range(stop) -> range object
 |  range(start, stop[, step]) -> range object
 |  
 |  Return an object that produces a sequence of integers from start (inclusive)
 |  to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
 |  start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
 |  These are exactly the valid indices for a list of 4 elements.
 |  When step is given, it specifies the increment (or decrement).
 |  
 |  Methods defined here:
 |  
 |  __bool__(self, /)
 |      self != 0
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __reduce__(...)
 |      Helper for pickle.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(...)
 |      Return a reverse iterator.
 |  
 |  count(...)
 |      rangeobject.count(value) -> integer -- return number of occurrences of value
 |  
 |  index(...)
 |      rangeobject.index(value) -> integer -- return index of value.
 |      Raise ValueError if the value is not present.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  start
 |  
 |  step
 |  
 |  stop

>>> s = 'computer science'
>>> len(s)
16
>>> for i in range(len(s)):
	print(i)

	
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
>>> for i in range (1, len(s),2):
	print(i)

	
1
3
5
7
9
11
13
15
>>> len('mom') in [1, 2, 3]
True
>>> [1, 2, 3] in len ('mom')
Traceback (most recent call last):
  File "<pyshell#275>", line 1, in <module>
    [1, 2, 3] in len ('mom')
TypeError: argument of type 'int' is not iterable
>>> int('3') in [len('a'), len('ab'),len('abc')]
True
>>> 'a' in ['mom','dad']
False
>>> len([1, 2, 3]) == len(['a','b','c'])
True
>>> '3' in [1,2,3]
False
>>> 
===== RESTART: C:/Users/edgar/Desktop/Universities/Toronto/Exam_Week5.py =====
>>> mystery('abc123')
'abc'
>>> mystery('123abc')
''
>>> mystery('123')
''
>>> mystery('abc')
Traceback (most recent call last):
  File "<pyshell#283>", line 1, in <module>
    mystery('abc')
  File "C:/Users/edgar/Desktop/Universities/Toronto/Exam_Week5.py", line 5, in mystery
    while not s[i].isdigit():
IndexError: string index out of range
>>> 
===== RESTART: C:/Users/edgar/Desktop/Universities/Toronto/Exam_Week5.py =====
>>> 
===== RESTART: C:/Users/edgar/Desktop/Universities/Toronto/Exam_Week5.py =====
>>> compress_list
<function compress_list at 0x0328D738>
>>> 
===== RESTART: C:/Users/edgar/Desktop/Universities/Toronto/Exam_Week5.py =====
>>> while_version
<function while_version at 0x00E3D738>
>>> 
===== RESTART: C:/Users/edgar/Desktop/Universities/Toronto/Exam_Week5.py =====
>>> return total
SyntaxError: 'return' outside function
>>> letters = ['b', 'd', 'a']
>>> letters.sort()
>>> print(letters)
['a', 'b', 'd']
>>> letters = ['b', 'd', 'a']
>>> sort(letters)
Traceback (most recent call last):
  File "<pyshell#291>", line 1, in <module>
    sort(letters)
NameError: name 'sort' is not defined
>>> letters=letters.sort()
>>> print(letters)
None
>>> letters = ['b', 'd', 'a']
>>> letters=sort(letters)
Traceback (most recent call last):
  File "<pyshell#295>", line 1, in <module>
    letters=sort(letters)
NameError: name 'sort' is not defined
>>> a = [1, 2, 3]
>>> b = a
>>> b[-2]='A'
>>> print(a, b)
[1, 'A', 3] [1, 'A', 3]
>>> a = [1, 2, 3]
>>> b = a
>>> a=[1,'A',3]
>>> b=[1,'A',3]
>>> print(a, b)
[1, 'A', 3] [1, 'A', 3]
>>> a = [1, 2, 3]
>>> b = a
>>> b[1]='AB'
>>> a[1]=a[1][0]
>>> print(a, b)
[1, 'A', 3] [1, 'A', 3]
>>> a = [1, 2, 3]
>>> b = a
>>> a[1]='A'
>>> print(a, b)
[1, 'A', 3] [1, 'A', 3]
>>> a = [1, 2, 3]
>>> b = [1, 2, 3]
>>> a=[1,'A',3]
>>> b=[1,'A',3]
>>> print(a, b)
[1, 'A', 3] [1, 'A', 3]
>>> a = [1, 2, 3]
>>> b=[1,'A',3]
>>> b[-2]='A'
>>> print(a, b)
[1, 2, 3] [1, 'A', 3]
>>> a = [1, 2, 3]
>>> b = [1, 2, 3]
>>> b[-2]='A'
>>> print(a, b)
[1, 2, 3] [1, 'A', 3]
>>> a = [1, 2, 3]
>>> b = [1, 2, 3]
>>> b[1]='AB'
>>> a[1]=a[1][0]
Traceback (most recent call last):
  File "<pyshell#330>", line 1, in <module>
    a[1]=a[1][0]
TypeError: 'int' object is not subscriptable
>>> a = [1, 2, 3]
>>> b = [1, 2, 3]
>>> a[1]='A'
>>> print(a, b)
[1, 'A', 3] [1, 2, 3]
>>> s = 'abccdeffggh'
>>> for i in range(len(s) - 1):
	print(i)

	
0
1
2
3
4
5
6
7
8
9
>>> 
====== RESTART: C:/Users/edgar/Desktop/Universities/Toronto/For_Loop.py ======
>>> print(count_adjacent_repeats('accffh'))
2
>>> 
====== RESTART: C:/Users/edgar/Desktop/Universities/Toronto/For_Loop.py ======
>>> L = ['a','b','c', 'd']
