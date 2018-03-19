# cryptographic secure
from os import urandom
from keccak import SHAKE128, SHAKE128_ITER


def getrandom(l):
    return bytes(urandom(l))


def bits(msg):
    for by in msg:
        for bi in format(by, '08b'):
            yield bi == '1'


def chunks4(msg):
    for by in msg:
        yield from divmod(by, 16)


def shake128(m):
    return SHAKE128(m, 32)


def shake128_iter(it, m):
    return SHAKE128_ITER(it, m, 32)
