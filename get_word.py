handle = open('3000.html')
f = open('3000.txt','a')
dct= dict()
lst = []


for line in handle:
    line = line.rstrip()
    if line.startswith('<a') :
        lst.append(line)

for line in lst:
    f.write(str(line))
    f.write('\n')



