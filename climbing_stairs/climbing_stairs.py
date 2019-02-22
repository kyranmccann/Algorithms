#!/usr/bin/python

import sys


def climbing_stairs(n, cache=None):
    if not cache:
        cache = [0] * n
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        ways = 0
        for step in range(3, 0, -1):
            stairs_left = n - step
            if stairs_left < 0:
                continue
            if cache[stairs_left] == 0:
                cache[stairs_left] = climbing_stairs(stairs_left, cache)
            ways += cache[stairs_left]
        return ways


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')
