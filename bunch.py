#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK


class BunchMeta(type):
    def __new__(mcls, name, bases, ns0):
        defaults = {}

        def init(self, *args, **kwargs):
            for key in defaults:
                val = kwargs.pop(key) if key in kwargs else defaults[key]
                setattr(self, key, val)
            if kwargs:
                # raise ValueError(f"{list(kwargs)}: were not used")
                raise AttributeError(f"No slots left for {list(kwargs)}")

        def repr(self, *args, **kwargs):
            args = ", ".join(
                f"{key}={getattr(self, key)!r}"
                for key in defaults
                if getattr(self, key) != defaults[key]
            )
            return f"{type(self).__name__}({args})"

        reserved = {"__init__": init, "__repr__": repr}
        ns = dict(ns0)
        for key, val in ns0.items():
            if key[:2] == "__" and key[-2:] == "__":
                if key in reserved:
                    raise RuntimeError(f"Cannot overwrite {key}")
            else:
                defaults[key] = val
                del ns[key]
        ns["__slots__"] = list(defaults)
        ns["__init__"] = init
        ns["__repr__"] = repr
        return super().__new__(mcls, name, bases, ns)


class Test:
    """
    >>> bob = Person()
    >>> bob
    Person()
    >>> max = Person(name='Max', age=42, salary=25000.0)
    >>> max
    Person(name='Max', age=42, salary=25000.0)
    >>> bob = Person(name='Bob', age=43, job='Engineer')
    Traceback (most recent call last):
    ...
    AttributeError: No slots left for ['job']
    >>> bob.mission = 'Save the world'
    Traceback (most recent call last):
    ...
    AttributeError: 'Person' object has no attribute 'mission'
    """


class Person(metaclass=BunchMeta):
    name = "Bob"
    age = 37
    salary = 12000.0


if __name__ == "__main__":
    bob = Person()
    print(bob)
    bob = Person(age=38)
    print(bob)
