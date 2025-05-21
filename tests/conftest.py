import pytest

@pytest.fixture
def circle():
    from shapes.circle import Circle
    return Circle(radius=10)


@pytest.fixture
def my_rectangle():
    from shapes.rectangle import Rectangle
    return Rectangle(width=10, height=4)


@pytest.fixture
def square():
    from shapes.rectangle import Rectangle
    return Rectangle(width=10, height=10)


@pytest.fixture
def triangle():
    from shapes.triangle import Triangle
    return Triangle(base=10, height=5)