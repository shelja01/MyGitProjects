#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.




name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

count = dict()

for line in handle:
    line = line.strip()
    if line.startswith('From '):
    	line = line.split()
        words= line[1]
        count[words] = count.get(words,0) + 1
    else:
        continue
     		#print(words[1])
     		#count=count+1

#print(count.items())


bigcount = None
bigword = None
for words,count in count.items():
    if bigcount is None or count > bigcount:
        bigword = words
        bigcount = count

print(bigword, bigcount)
