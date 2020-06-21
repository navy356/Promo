#!/usr/bin/python3
from progress.bar import Bar
from random import choice
import time
from random import randint
sel = 0
print("Tracing attacker...")
obj = Bar('Processing', max=100)
for i in range(100):
    # Do some work
    # obj.index() = choice(list(range(100)))
    # print(obj.index())
    obj.next(-sel)
    sel = randint(0,100)
    obj.next(sel)
    time.sleep(0.1)
obj.next(100-obj.index)
obj.finish()
print("Success!")
