#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from functools import wraps


def eql_dispatch(func):
    registry = {}

    def register(*values):
        def inner(_func):  # def _(num):
            for val in values:
                registry[val] = _func

        return inner

    @wraps(func)
    def wrapper(*args, **kwwargs):
        val = args[0]
        try:
            return registry[val](*args, **kwwargs)
        except KeyError:
            return func(*args, **kwwargs)

    wrapper.register = register
    return wrapper


@eql_dispatch
def name_number(num):
    print(f"{num!r}: anything else")


@name_number.register(0)
def _(num):
    print(f"{num!r}: zero")


@name_number.register(1, 3, 5)
def _(num):
    print(f"{num!r}: 1-3-5")


@name_number.register(2, 4, 6)
def _(num):
    print(f"{num!r}: 2-4-6")


if __name__ == "__main__":
    name_number(0)
    name_number(3)
    name_number(6)
    name_number(100)
