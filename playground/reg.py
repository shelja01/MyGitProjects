#regular expression

import re
from re import search

file = open('mbox-short.txt','r')
for line in file:
  line = line.rstrip()
  if re.search('From:',line):
     print(line)
