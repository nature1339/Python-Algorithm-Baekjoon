Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = set()
>>> 
>>> 
a
>>> 
>>> print(a)
set()
>>> a.add(3)
>>> a
{3}
>>> 
>>> b = {3, 4}
>>> b
{3, 4}
>>> 
>>> 
>>> a.add(5)
>>> 
>>> a
{3, 5}
>>> 
>>> a.add(3)
>>> 
>>> a
{3, 5}
>>> 