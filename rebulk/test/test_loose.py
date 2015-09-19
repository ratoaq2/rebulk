#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=no-self-use, pointless-statement, missing-docstring

from ..loose import call


def test_loose_function():

    def func(v1, v2, v3=3, v4=4):
        return v1 + v2 + v3 + v4

    assert call(func, 1, 2) == func(1, 2)
    assert call(func, 1, 2, 3, 5) == func(1, 2, 3, 5)
    assert call(func, 1, 2, v3=4, v4=5) == func(1, 2, v3=4, v4=5)
    assert call(func, 1, 2, 3, 4, 5) == func(1, 2, 3, 4)
    assert call(func, 1, 2, 3, 4, more=5) == func(1, 2, 3, 4)

def test_loose_class():
    class Dummy(object):
        def __init__(self, v1, v2, v3=3, v4=4):
            self.v1 = v1
            self.v2 = v2
            self.v3 = v3
            self.v4 = v4

        def call(self):
            return self.v1 + self.v2 + self.v3 + self.v4

    assert call(Dummy, 1, 2).call() == Dummy(1, 2).call()
    assert call(Dummy, 1, 2, 3, 5).call() == Dummy(1, 2, 3, 5).call()
    assert call(Dummy, 1, 2, v3=4, v4=5).call() == Dummy(1, 2, v3=4, v4=5).call()
    assert call(Dummy, 1, 2, 3, 4, 5).call() == Dummy(1, 2, 3, 4).call()
    assert call(Dummy, 1, 2, 3, 4, more=5).call() == Dummy(1, 2, 3, 4).call()
