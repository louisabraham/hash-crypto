"""
Binary trees are represented by arrays.
The children of node #i are nodes #((i << 1) + 1) and #((i << 1) + 2)
The parent of #i is #((i - 1) >> 1)
"""

# change this line into
# import lamport as OTS
# to use lamport OTS instead
import winternitz as OTS
from utils import shake128
from tqdm_alt import tqdm


class MerkleTree():

    def __init__(self, HEIGHT=10, progressbar=True):
        self.n_keys = 1 << HEIGHT
        r = range(self.n_keys)
        if progressbar:
            r = tqdm(r)
        keys = [OTS.key_generation() for _ in r]
        tree = [None] * (self.n_keys - 1) + \
            [shake128(b''.join(k[1])) for k in keys]

        for i in reversed(range(self.n_keys - 1)):
            tree[i] = shake128(tree[(i << 1) + 1] + tree[(i << 1) + 2])

        self.keys = keys
        self.tree = tree
        self.last_key_used = -1

    @property
    def public_key(self):
        return self.tree[0]

    def signature(self, msg):
        key_index = self.last_key_used + 1
        assert key_index in range(self.n_keys), 'All keys have been used'

        secret, public = self.keys[key_index]
        self.last_key_used = key_index

        auth = []
        for i, b in self.iter_ancestors(key_index + self.n_keys - 1):
            auth.append(self.tree[(i << 1) + 2 - b])

        auth = tuple(auth)

        return (key_index, OTS.signature(msg, secret), public, auth)

    @staticmethod
    def iter_ancestors(i):
        while i:
            i, b = divmod(i - 1, 2)
            yield i, b

    @staticmethod
    def verify(msg, sign, merkle_public):

        key_index, otssign, otspublic, auth = sign

        if not OTS.verify(msg, otssign, otspublic):
            return False

        h = shake128(b''.join(otspublic))

        n_keys = 1 << len(auth)

        # loop invariant: h is the value of node #i
        for a, (i, b) in zip(auth, MerkleTree.iter_ancestors(key_index + n_keys - 1)):
            h = shake128((a + h) if b else (h + a))

        return h == merkle_public
