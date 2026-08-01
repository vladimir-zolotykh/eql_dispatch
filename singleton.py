#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in (saved := type(cls)._instances):
            saved[cls] = super().__call__(*args, **kwargs)
        return saved[cls]


class Logger(metaclass=Singleton):
    def __init__(self):
        print(f"Initializing {type(self)!r}")


if __name__ == "__main__":
    g1 = Logger()
    g2 = Logger()
    assert g1 is g2
