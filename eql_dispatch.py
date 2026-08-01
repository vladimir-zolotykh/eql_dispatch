#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK


def eql_dispatch(func):
    return func


@eql_dispatch
def name_number(num):
    print(f"{num!r}: anything else")


@name_number.register(0)
def _(num):
    print(f"{num!r}: zero")


@name_number.register(1, 3, 5)
def name_number(num):
    print(f"{num!r}: zero")


@name_number.register(2, 4, 6)
def _(num):
    print(f"{num!r}: enen")


if __name__ == "__main__":
    name_number(0)
    name_number(3)
    name_number(6)
    name_number(100)
