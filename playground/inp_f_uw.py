# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname,"r")
except:
    print("File can not be opened")
    quit()

w=0
for words in fh:
    uw = words.upper()
    print(uw.rstrip())
