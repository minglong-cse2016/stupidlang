#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from stupidlang.skeleton import fib

__author__ = "minglong-cse2016"
__copyright__ = "minglong-cse2016"
__license__ = "mit"

import pytest
from stupidlang.skeleton import main

__author__ = "Rahul Dave"
__copyright__ = "Rahul Dave"
__license__ = "mit"


def test_main():
    assert main(["tests/test2.sl"])=='7'

