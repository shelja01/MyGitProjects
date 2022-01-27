
#file = input("Enter a File name:")

#try:
  #fh = open(file, "r")
#except:
  #print("Can not open File, enter a new file")
  #quit()

count = dict()
fh = input("Enter a line of text:")
lines = fh.split()
for word in lines:
    count[word] = count.get(word,0) + 1

print('Count',count)
