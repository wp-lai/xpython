"""
Rolling Hash Data Structure

>>> rh1 = RollingHash('abcde')
>>> rh2 = RollingHash('bcdef')
>>> rh3 = RollingHash('cdefz')
>>> rh1.append('f').skip()
RollingHash("bcdef")
>>> rh1.hash == rh2.hash
True
>>> rh1.skip().append('z');
RollingHash("cdefz")
>>> rh1.hash == rh3.hash
True
"""
from collections import deque


def modular_inverse(a, p):
    """find the modular inverse s.t. aa^-1 mod p = 1"""
    for b in range(1, p):
        if (a * b) % p == 1:
            return b


class RollingHash(object):

    def __init__(self, seq, base=7, buckets=16, prehash=ord):
        self.__hash = 0
        self.__size = 0
        self.__base = base
        self.__buckets = buckets
        self.__pow_base_size = 1
        self.__inv_mod = modular_inverse(self.__base, self.__buckets)
        self.__prehash = prehash
        self.__seq = deque()

        for e in seq:
            self.append(e)

    @property
    def hash(self):
        return self.__hash

    def __len__(self):
        return self.__size

    def __repr__(self):
        return "RollingHash(\"{}\")".format(''.join(self.__seq))

    def append(self, e):
        m = self.__buckets
        base = self.__base
        self.__hash = (self.__hash * base + self.__prehash(e)) % m
        self.__size += 1
        self.__pow_base_size = (self.__pow_base_size * base) % m
        self.__seq.append(e)
        return self

    def skip(self):
        m = self.__buckets
        e = self.__seq.popleft()
        self.__size -= 1
        self.__pow_base_size = (self.__pow_base_size * self.__inv_mod) % m
        self.__hash = \
            (self.__hash - self.__prehash(e) * self.__pow_base_size +
             self.__base * m) % m
        return self
