from urllib.request import urlopen
from bs4 import BeautifulSoup

import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter Url: ')
count = int(input("Enter count: "))
position = int(input("Enter position:"))
for i in range(count):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")


    tags = soup('a')
    s = []
    t = []
    for tag in tags:
        x = tag.get('href', None)
        s.append(x)
        y = tag.text
        t.append(y)

    print(s[position-1])
    print(t[position-1])
    url = s[position-1]
/Name=HVR_ASM_CONNECT /Value="ASMDBA/!{L/V.IKfhY/xNJKXB//v5ACZ9/LeBsARZ}!"

/SslRemoteCertificate="/opt/hvr/hvr_home/lib/cert/Oracleaebts02HVRCertificate.pub_cert"

/opt/oracle/app/product/19.0.0
tst2-ebs-scan.tst.nintendo.com

/opt/hvr/hvr_home/lib/cert/Oracleaebts02HVRCertificate.pub_cert

RAC  tst2-ebs-scan.tst.nintendo.com  1521
CDBDM02T
c##xxhvr

tst2-ebs-scan.tst.nintendo.com:1521/aebts02

xxhv


 error ORA-01804

/DatatypeMatch=<<sdo_geometry>> /CaptureExpression="SDO_UTIL.TO_WKTGEOMETRY({{hvr_col_name}}) " /CaptureExpressionType=SQL_WHERE_ROW
/DatatypeMatch=<<sdo_geometry>> /CaptureExpression="ST_ASWKT({{hvr_col_name}}) " /IntegrateExpression=TRY_TO_GEOGRAPHY({{hvr_col_name}})



C:\Users\chanpa02\AppData\Local\Programs\Python\Python36\Scripts\;C:\Users\chanpa02\AppData\Local\Programs\Python\Python36\Lib\site-packages;C:\Users\chanpa02\AppData\Local\Programs\Python\Python36\;%USERPROFILE%\AppData\Local\Microsoft\WindowsApps;C:\Program Files (x86)\Common Files\Oracle\Java\javapath;%SystemRoot%\system32;%SystemRoot%;%SystemRoot%\System32\Wbem;%SYSTEMROOT%\System32\WindowsPowerShell\v1.0\;C:\Program Files\PuTTY\;C:\Program Files\TortoiseSVN\bin;C:\Program Files (x86)\Windows Kits\8.1\Windows Performance Toolkit\;C:\oracle\product\11.2.0\client_1\bin;C:\oracle\product\11.2.0\client_1\instantclient;C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin;C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC
