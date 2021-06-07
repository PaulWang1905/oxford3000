import os
import random
from time import sleep


f = open('3000url.txt')
def download(self):
    cmd = 'wget ' + self
    os.system(cmd)
    print(cmd)
    print("Dowloading")
    num= round(random.uniform(30,60),2)
    sleep(num)
    print('waiting' + num)
    return


for url in f:
    download(url)


