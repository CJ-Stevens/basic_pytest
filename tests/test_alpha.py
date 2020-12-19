# doc https://docs.pytest.org/en/stable/index.html

from src.area import rectangle, triangle
from src.volume import *
import pytest


def test_one():
    assert rectangle(5, 2) == 10
    assert rectangle(5, 4.5) == 22.5
    assert triangle(5, 2) == 5


def test_volume():
    assert cubic(3) == 27
    assert cylinder(1, 10) == 31.41592653589793
    assert cylinder(1, 10) == pytest.approx(31.4159, .0001)


def test_list():
    assert [cubic(n) for n in range(1, 4)]==[1,8,27]


def test_exception():
    with pytest.raises(ValueError):
        rectangle(-5, 2)

    with pytest.raises(ValueError, match=r'w, h must be greater than zero.'):
        rectangle(-5, 2)

    # with pytest.raises(FileExistsError):
    #     rectangle(-5, 2)
