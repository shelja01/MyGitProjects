# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

num_content=0
url =  input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
#print('h')
# Retrieve all of the anchor tags
tags = soup('span')    #find_all('td')
#if len(tags) > 1: print('hey')
for tag in tags:
    # Look at the parts of a tag
    #print('TAG:', tag, len(tag))   #s= re.findall('([0-9]+)',line)
    #if len(tag) == 1:
        #comment = re.findall('([0-9]+)',tag)
        #print(comment)
    #print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[0])
    num_content = int(tag.contents[0]) + num_content

   # print('Attrs:', tag.attrs)
print(num_content)
