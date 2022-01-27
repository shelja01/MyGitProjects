import urllib.request , urllib.parse
import sqlite3


#connecting to the sqllite file in which we want to store the Data

conn=sqlite3.connect('emaildb.sqlite')
cur=conn.cursor()

#Deleting an previous assignents to the db
cur.execute('''
drop table if exists counts;
''')


#creating a TABLE
cur.execute('''
create table counts(org text,count INTEGER) ;
''')

#from where are you reading the data to place in the database?
file = input("Enter File name")
if len(file) < 1: file = 'mbox.txt'
fh=open(file)
for lines in fh:
        if not lines.startswith('From:'): continue
    #    print('Lines     ',lines)
    #    print('Llllllllllllllllllll')
        orgs=lines.split('@')
        org=orgs[1]
        cur.execute('SELECT count FROM counts WHERE org = ? ', (org,))
        row = cur.fetchone()
        if row is None:
        #for o in org:
            cur.execute('''
            insert into counts(org,count) values (?,1)''',(org,))
        else:
            cur.execute('''
            update counts set  count = count+1 where org = ?''',(org,))

conn.commit()


sqlstr = 'select org,count from counts order by count DESC;'

for ro in cur.execute(sqlstr):
    print(str(ro[0]),str(ro[1]))

conn.close()
        #print(email)
