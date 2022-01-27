import json
import sqlite3

conn = sqlite3.connect('roosterdb.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;

create table User (
    id INTEGER not null PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT );

create table Course (
    id INTEGER not null PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT );


create table Member (
    user_id INTEGER,
    course_id INTEGER ,
    role INTEGER ,
    PRIMARY KEY (user_id , course_id));
'''
)

#File setup
file=input("Enter File: ")
if len(file) <1 : file='rooster_data.json'

fh = open(file).read()
file_data = json.loads(fh)

for data in file_data:
    name = data[0]
    title = data[1]
    role = data[2]

    #print(name, title,role)

    #insert user and get user_id
    cur.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name,) )
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]


    #insert course and get course_id
    cur.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES (?)''',(title,))
    cur.execute('SELECT id FROM Course WHERE TITLE = ?',(title,))
    course_id = cur.fetchone()[0]

    #insert MEMBER
    cur.execute('''INSERT OR IGNORE INTO MEMBER (USER_ID,course_id,ROLE)
        VALUES (?,?,?)''',(user_id,user_id,role,))
    #cur.execute('''select id from Course where TITLE = ?''',(TITLE))
    #course_id=cur.fetchone()[0]


conn.commit()

# # sqlstr = '''SELECT User.name,Course.title, Member.role FROM
#     User JOIN Member JOIN Course
#     ON User.id = Member.user_id AND Member.course_id = Course.id
#     ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;'''

sqlstr = '''SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X FROM
    User JOIN Member JOIN Course
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X LIMIT 1;'''

for ro in cur.execute(sqlstr):
    print(str(ro[0])) #,str(ro[1]))

#conn.close()
