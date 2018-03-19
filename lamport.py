from utils import *

SIGNATURE_LENGTH = 256


def key_generation():
    """
    returns: (secret_key, public_key)
    """
    s = tuple(getrandom(32) for _ in range(512))
    p = tuple(map(shake128, s))
    return s, p


def signature(msg, secret):
    assert len(msg) == 32, 'message must be 256-bit long'
    return tuple(secret[2 * i + b]
                 for i, b in zip(range(256), bits(msg)))


def verify(msg, sign, public):
    # calling signature with the public key must
    # generate the hashes of the signature
    return all(hs == p
               for hs, p in zip(map(shake128, sign),
                                signature(msg, public)))
