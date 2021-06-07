f = open('3000.txt')
output = open('3000url.txt','a')
lst = []
url = ''
all_word=[]

for line in f : 
    line = line[:-5]
    lst = line.split('>')
    url = lst[0][9:-1]
    url = 'https://www.oxfordlearnersdictionaries.com'+url
    #print(url)
    del lst[0]
    lst.append(url)
    all_word.append(lst)
    output.write(url)
    output.write('\n')



