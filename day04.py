# ============================================================
# DAY 04 - STRING METHODS
# ============================================================


# ===============================
# 1. strip(), lstrip(), rstrip()
# ===============================

a = '   python is simple   '

print(a.strip())
# Output: python is simple

print(a.lstrip())
# Output: python is simple   

print(a.rstrip())
# Output:    python is simple


# ==============
# 2. replace()
# ==============

a = 'python is simple, python is easy, python is allrounder'

b = a.replace('python', 'java')

print(a)
# Output: python is simple, python is easy, python is allrounder

print(b)
# Output: java is simple, java is easy, java is allrounder


# =========================================================
# 3. upper(), lower(), swapcase(), title(), capitalize()
# =========================================================

a = 'PYTHON is siMPle'

print(a.lower())
# Output: python is simple

print(a.upper())
# Output: PYTHON IS SIMPLE

print(a.swapcase())
# Output: python IS SImpLE

print(a.title())
# Output: Python Is Simple

print(a.capitalize())
# Output: Python is simple


# =====================================
# 4. count(), startswith(), endswith()
# =====================================

a = 'abacad'

b = a.startswith('a')
c = a.startswith('ad')
d = a.endswith('d')
e = a.endswith('de')
f = a.count('a')
g = a.count('ad')

print(b)
# Output: True

print(c)
# Output: False

print(d)
# Output: True

print(e)
# Output: False

print(f)
# Output: 3

print(g)
# Output: 0


# =======================================
# 5. find(), rfind(), index(), rindex()
# =======================================

s = 'abacada'

print(s.find('a'))
# Output: 0

print(s.find('a', 3))
# Output: 4

print(s.find('a', 4, 8))
# Output: 4

print(s.rfind('a'))
# Output: 6

print(s.rfind('a', 3))
# Output: 6

print(s.rfind('a', 4, 8))
# Output: 6

print(s.index('a'))
# Output: 0

print(s.index('a', 3))
# Output: 4

print(s.index('a', 4, 8))
# Output: 4

print(s.index('a'))
# Output: 0

print(s.index('a', 3))
# Output: 4

print(s.index('a', 4, 8))
# Output: 4

# 'z' does not exist.
# index() gives ValueError if the substring is not found.
# print(s.index('z'))
# Output: ValueError

print(s.find('z'))
# Output: -1


# ===============
# 6. is METHODS
# ===============

# -------- isspace() --------

a = ' '

b = ' a'

print(a.isspace())
# Output: True

print(b.isspace())
# Output: False


# -------- isalpha() --------

a = 'aBcD'

print(a.isalpha())
# Output: True

b = 'aBcD1'

print(b.isalpha())
# Output: False

c = 'aBc@D'

print(c.isalpha())
# Output: False


# -------- isdigit() --------

a = '13'

print(a.isdigit())
# Output: True

b = '12a'

print(b.isdigit())
# Output: False


# -------- isalnum() --------

a = 'AbC123'

print(a.isalnum())
# Output: True

b = 'Ab#C2'

print(b.isalnum())
# Output: False


# -------- isupper() --------

a = '23$U'

print(a.isupper())
# Output: True

b = '23%Ua'

print(b.isupper())
# Output: False


# -------- islower() --------

a = '23$u'

print(a.islower())
# Output: True

b = '23%uA'

print(b.islower())
# Output: False


# ============
# 7. split()
# ============

a = 'badac'

print(a.split('a'))
# Output: ['b', 'd', 'c']


b = '   '       # 3 spaces

print(b.split(' '))
# Output: ['', '', '', '']


c = 'abaca'

print(c.split('a'))
# Output: ['', 'b', 'c', '']


d = 'iam a good person'

print(d.split())
# Output: ['iam', 'a', 'good', 'person']


# =============
# 8. join()
# =============

a = '@'

# NOTE:
# join() requires strings.
# Integer elements cannot be joined directly.

l = ['1', '2', '3']
t = ('1', '2', '3')
s = {'1', '2', '3'}
d = {'3': '1', '2': '3'}

print(a.join(l))
# Output: 1@2@3

print(a.join(t))
# Output: 1@2@3

print(a.join(s))
# Output: Order may vary because set is unordered

print(a.join(d))
# Output: 3@2@3
# Dictionary join() uses its keys.


