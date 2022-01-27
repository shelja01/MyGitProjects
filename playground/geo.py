import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys

file = open('where.data.txt')
#data = jsonloads(file)
conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()
cur.executescript('''
DROP TABLE IF EXISTS LOCATIONS;
CREATE TABLE IF NOT EXISTS LOCATIONS( ADDRESS TEXT , GEO TEXT);
'''
)
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
count=0
for line in file:
    if count > 50 :
        print('Retrieved  locations, restart to retrieve more')
        break
    address = line.strip()
    cur.execute('select ADDRESS from LOCATIONS WHERE ADDRESS =  ?',(memoryview(address.encode()),))
    try:
        data = cur.fetchone()[0]
        print("Exists")
    except:
        pass
    params = dict()
    params["address"] = address
    geo_link = 'http://py4e-data.dr-chuck.net/geojson?'
    link = geo_link + urllib.parse.urlencode(params)
    uh = urllib.request.urlopen(link,context =ctx)
    url_data = uh.read().decode()
    count = count + 1

    try:
        js = jsonloads(url_data)
    except:
        print("Issue")
    continue

    cur.execute('''
    INSERT INTO LOCATIONS (ADDRESS, GEODATA)
    VALUES (?,?)
    ''', memoryview(address.ENCODE(),memoryview(url_data.encode())))
    print("Inserted ",address,url_data)
    conn.COMMIT()
