#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from stupidlang.skeleton import fib

__author__ = "minglong-cse2016"
__copyright__ = "minglong-cse2016"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
