#regular expression

import re
from re import search

#num=0
#su = 0
file = open('regex_sum_1288036.txt','r')
x=list()
for line in file:
  #line = line.rstrip()
  #if re.search('From:',line):
  #print(line)
  s= re.findall('([0-9]+)',line)
  x = x + s

sum = 0
for z in x:
      sum = sum + int(z)#su=int(s[num])+su
      #num = num + num

      #su = int(su) + int(num)

print(sum)
#print(su)


#print(su)
