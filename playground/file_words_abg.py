# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname,"r")
except:
    print("File can not be opened")
    quit()
k=0
lastvalue = 0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    w = line.rstrip()
    words = w.split()
    #print(line)
   #print(lastvalue)
    lastvalue = lastvalue + float(words[-1])
    k=k+1

    #print(lastvalue)
    #print(k)
   #print(avg)
#print(lastvalue)
avg = lastvalue/k
print("Average spam confidence:",avg)

Coming back: Sunday
Tuesday:  11:45 , or 2:15
Wednesday: 2:30

next Week Monday: pretty open
