import random
import os
import time
import sys
from progress.spinner import Spinner


def generate_ip():
    return str(1)+str(random.choice([9, 8, 9, 9])) + str(random.choice([1, 2, 3]))+'.'+str(random.randint(0, 100))+'.'+str(random.randint(0, 100))+'.'+str(random.randint(0, 100))


for i in range(10):
    ip = str(generate_ip())
    first = 'PING '+ip+' ('+ip+') 56(84) bytes of data.'
    n = random.randint(200, 400)
    every_line = '64 bytes from '+ip + \
        ' ('+ip+'): icmp_seq=1 ttl=55 time='+str(n)+' ms'
    # spin = spinner('Connecting...')
    print(first)
    spinner = Spinner('connecting ... ')
    for i in range(10):
        time.sleep(0.1)
        spinner.next()
    # print('\n')
    time.sleep(n//200)
    print(f'\n{every_line}\n')
    time.sleep(n//300)
