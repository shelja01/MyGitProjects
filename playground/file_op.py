fh = open("romeo.txt", "r")
sh = open("mbox-short.txt", "r")
lh = open("words.txt", "r")

count = 0
for line in fh:
  #  print(line.strip())
    count = count + 1


k=0
for words in sh:
    if (words.startswith('svn log')) == True:
      k = k + 1

l=0
for words in lh:
  # print(words.split())
   l = l + len(words.split())
   # l = l + 1

print(count,"Lines")
print(k,"Lines starting with svn log")
print(str(l),"# of words in file 3")
