#!/usr/bin/env python

import sys

def plus(a, b):
    return a + b

if __name__=="__main__":

    if plus(1,2)!=4:
        sys.exit("error")

    if plus(1.1, 2.2) < 3.29999 or plus(1.1, 2.2)>3.30001:
        sys.exit(2)

    if plus("abc", "def")!="abcdef":
        sys.exit(3)

    sys.exit(0)
