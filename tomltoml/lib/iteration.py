# -*- coding: utf-8 -*-
from itertools import chain
from itertools import cycle


def interleave(xs, ys):
    # This doesn't work for lists of different lengths. Use itertool recipes
    # roundrobin() instead.
    return chain.from_iterable(zip(xs, ys))
