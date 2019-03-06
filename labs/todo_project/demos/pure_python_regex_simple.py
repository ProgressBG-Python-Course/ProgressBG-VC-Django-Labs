import re

"""
capture goups are always created, when there is a match
"""
#pattern = r"(?P<a>a)|(?P<b>b)|(?P<c>c)"
pattern = r"a|(b)|(c)"

tests = [
  'ab',
  'ac',
  'xy '
]

for test in tests:
  print(f'\ntest = {test}')  
  m = re.search(pattern, test)  
  print(m.groups())
  
       