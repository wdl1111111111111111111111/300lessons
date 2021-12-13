import os
import sys
def reverse(num):
    a=int(num/100)
    b=int(num%100/10)
    c=int(num%10)
    return c*100+b*10+a

if __name__ == '__main__':
    print(reverse(396))