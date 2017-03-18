import time

import sys


def timer_stuff():
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
     for i in range(20):
          print("\r" + str(i), end="")
          time.sleep(0.25)


# timer_stuff()

print('{}'.format("asdf").rjust(6))