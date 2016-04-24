#!/usr/bin/env python
import sys
import time
from functools import reduce

_dbg = '-d' in sys.argv[1:]

def out(s):
    sys.stdout.write(s)
    sys.stdout.flush()

if _dbg:
    def dbg(s):
        if isinstance(s, str):
            out(s)
        else:
            out(str(s) + '\n')
else:
    def dbg(s):
        pass

def readline():
    return sys.stdin.readline().strip()

def readfloat():
    return float(readline())

def readfloats():
    return [float(x) for x in readline().split()]

def readint():
    return int(readline())

def readints():
    return [int(x) for x in readline().split()]

def solve_case():
    pass

def main():
    fmt = 'Case #{0:d}: {1}\n'
    cases = readint()
    if _dbg:
        for c in range(1, cases + 1):
            t0 = time.time()
            out(fmt.format(c, solve_case()))
            dbg('{:.6f}\n'.format(time.time() - t0))
    else:
        for c in range(1, cases + 1):
            out(fmt.format(c, solve_case()))

if __name__ == '__main__':
    main()

