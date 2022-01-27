#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.


name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)


count = dict()
for lines in handle:
    #line = lines.rstrip()
    if  lines.startswith('From '):
    #for words in line:
        #word = line.split()
        #print(word)
        #hour = (word[5].split(':')[0])
        # ((word[5].split(':')[0]))
        hour = lines.split()[5].split(':')
        count[hour[0]] = count.get(hour[0],0) + 1
        #h=hour
        #for h in hour: count = count+1
        #if hour in hour : count = count+1
        #print(hour)#,count)

l= list()

for k,v in count.items():
    l.append((k,v))
l.sort()

for h,c in l:
    print(h,c)
