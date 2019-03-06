import re

pattern = r"user/(?:(?P<user_name>[A-Za-z]+)|(?P<id>\d+))$"
# pattern = r"user/(\w+|\d+)$"
print(f'pattern = {pattern}')


tests = [
  'http://127.0.0.1:8000/demos/user/ivan',
  'http://127.0.0.1:8000/demos/user/1'
]

for test in tests:
  print(f'\ntest = {test}')  
  m = re.search(pattern, test)  
  if m:
    print(len(m.groups()))   