import pytest
from shapes.triangle import Triangle

pytestmark = pytest.mark.triangle


def test_triangle_area(triangle):
    assert triangle.area() == 25


def test_triangle_perimeter(triangle):
    # triangle fixture: base=10, height=5; perimeter with sides 10, 10, 10
    assert triangle.perimeter(10, 10) == 30


def test_triangle_is_equilateral(triangle):
    assert triangle.is_equilateral(10, 10)


def test_triangle_is_not_equilateral(triangle):
    assert not triangle.is_equilateral(10, 5)


def test_triangle_is_isosceles(triangle):
    assert triangle.is_isosceles(10, 5)
    assert triangle.is_isosceles(5, 10)


def test_triangle_is_not_isosceles(triangle):
    t = Triangle(7, 3)
    assert not t.is_isosceles(5, 6)


def test_error_negative_base():
    with pytest.raises(ValueError):
        Triangle(base=-3, height=5)


def test_error_negative_height():
    with pytest.raises(ValueError):
        Triangle(base=3, height=0)
