import os
import sys
import pdb

class Aclass():
    def __init__(self,num):
        self.num=num
    def reverse(self):
        a = int(self.num / 100)
        b = int(self.num % 100 / 10)
        c = int(self.num % 10)
        return c * 100 + b * 10 + a


if __name__ == '__main__':
    print(Aclass(586).reverse())
