import re

## Coloque aqui usa expressão regular
regexp = r'[0]([x]|[X])([0-9]+|[A-F])*'


for string in input().split(' '):
  print( re.fullmatch(regexp, string) != None)
