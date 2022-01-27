#python create a discinary with , values as # of times the key appears in a list

d = dict()
names = ['James','Work','Anthony','James','Work']

for name in names:
    d[name] = d.get(name,0) +1
    #if name not in d:
    #    d[name] = 1
    #else:
    #    d[name] = d[name] +1
print(d)
