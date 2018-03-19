from functools import partial
from itertools import chain

from utils import *

SIGNATURE_LENGTH = 67


def key_generation():
    """
    returns: (secret_key, public_key)
    """
    s = tuple(getrandom(256) for _ in range(67))
    p = tuple(map(partial(shake128_iter, 16), s))
    return s, p


def checksum(msg):
    c = 960 - sum(chunks4(msg))
    c1, c2, c3 = c // 256, c // 16 % 16, c % 16
    return [c1, c2, c3]


def signature(msg, secret):
    assert len(msg) == 32, 'message must be 256-bit long'
    chunks = chain(chunks4(msg), checksum(msg))
    return tuple(shake128_iter(ch, s)
                 for ch, s in zip(chunks, secret))


def verify(msg, sign, public):
    chunks = chain(chunks4(msg), checksum(msg))
    return all(p == shake128_iter(16 - ch, si)
               for p, ch, si in zip(public, chunks, sign))
