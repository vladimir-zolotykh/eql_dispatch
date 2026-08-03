import pytest
from bunch import BunchMeta, Person, Point


@pytest.fixture
def bob():
    return Person()


@pytest.fixture
def max():
    return Person(name="Max", age=42, salary=25000.0)


def test_person_simple(bob, max):
    assert str(bob) == "Person()"
    assert str(max) == "Person(name='Max', age=42, salary=25000.0)"
    with pytest.raises(AttributeError, match="No slots left for 'job'"):
        Person(name="Bob", age=43, job="Engineer")
    with pytest.raises(
        AttributeError, match="'Person' object has no attribute 'mission'"
    ):
        bob.mission = "Save the world"


def test_point():
    p = Point()
    assert repr(p) == "Point()"  # Point redefines __str__

    p = Point(x=3, y=4, color="yellow")
    assert repr(p) == "Point(x=3, y=4, color='yellow')"
    assert str(p) == "Point(3, 4, yellow)"


def test_no_repr_overwrite():
    with pytest.raises(TypeError, match="Cannot overwrite __repr__"):

        class Line(metaclass=BunchMeta):
            x = 0.0
            y = 0.0

            def __repr__(self):
                pass


def test_init_positional_args():
    max = Person("Max", 42, 25000.0)
    assert repr(max) == "Person(name='Max', age=42, salary=25000.0)"

    max = Person("Max", 39)
    assert repr(max) == "Person(name='Max', age=39)"

    assert max.salary == 12000.0

    with pytest.raises(AttributeError, match="No slots left for 'Senior Java Dev'"):
        Person("Max", 39, 11000.0, "Senior Java Dev")
