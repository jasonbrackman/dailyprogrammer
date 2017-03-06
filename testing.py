import time

import sys

x = ['-',
     '\\',
     '|',
     '/']

y = ['-********',
     '*-*******',
     '**-******',
     '***-*****',
     '****-****',
     '*****-***',
     '******-**',
     '*******-*',
     '********-']
for s in range(30):
    for item in x:
        print('\r[{0}]'.format(item), end='')

        time.sleep(0.25)
        #sys.stdout.flush()
        #sys.stdout.write('\r' * len(item))

for i in range(20):
     print("\r" + str(i), end="")
     time.sleep(0.25)
