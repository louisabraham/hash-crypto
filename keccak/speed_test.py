#!/usr/bin/env python3

from time import time

from .keccak import SHAKE128, SHAKE128_ITER
from .CompactFIPS202 import SHAKE128 as SHAKE128_slow


def test_all(inp=b'a', it=50):
    r1 = inp
    d = time()
    for _ in range(it):
        r1 = SHAKE128_slow(r1, 32)
    t1 = time() - d
    print(t1)

    r2 = inp
    d = time()
    for _ in range(it):
        r2 = SHAKE128(r2, 32)
    print(time() - d)

    r3 = inp
    d = time()
    r3 = SHAKE128_ITER(it, r3, 32)
    t3 = time() - d
    print(t3)

    assert r1 == r2 == r3
    print('Speedup: x%i' % (t1 / t3))


if __name__ == '__main__':
    test_all(it=1000)
