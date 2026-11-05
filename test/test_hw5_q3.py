import math

import pytest

import hw5


# PlaneFigure (abstract class / interface)

def test_plane_figure_cannot_be_instantiated():
    with pytest.raises(TypeError):
        hw5.PlaneFigure()


def test_plane_figure_subclass_missing_method_cannot_be_instantiated():
    class OnlyPerimeter(hw5.PlaneFigure):
        def compute_perimeter(self):
            return 0

    with pytest.raises(TypeError):
        OnlyPerimeter()


def test_plane_figure_abstract_methods_return_not_implemented_error():
    class CallsParent(hw5.PlaneFigure):
        def compute_perimeter(self):
            return super().compute_perimeter()

        def compute_surface(self):
            return super().compute_surface()

    figure = CallsParent()

    assert figure.compute_perimeter() is NotImplementedError
    assert figure.compute_surface() is NotImplementedError


def test_figures_are_plane_figures():
    figures = [hw5.Triangle(3, 4, 5, 4), hw5.Rectangle(2, 3), hw5.Circle(1)]

    for figure in figures:
        assert isinstance(figure, hw5.PlaneFigure)


# Triangle

def test_triangle_init():
    triangle = hw5.Triangle(3, 4, 5, 4)

    assert triangle.base == 3
    assert triangle.c1 == 4
    assert triangle.c2 == 5
    assert triangle.h == 4


@pytest.mark.parametrize(
    "base, c1, c2, h, expected",
    [
        (3, 4, 5, 4, 12),
        (2, 2, 2, math.sqrt(3), 6),
        (1.5, 2.5, 3.5, 1, 7.5),
        (0, 0, 0, 0, 0),
    ],
)
def test_triangle_compute_perimeter(base, c1, c2, h, expected):
    triangle = hw5.Triangle(base, c1, c2, h)

    output = triangle.compute_perimeter()

    assert output == pytest.approx(expected)


@pytest.mark.parametrize(
    "base, c1, c2, h, expected",
    [
        (3, 4, 5, 4, 6),
        (2, 2, 2, math.sqrt(3), math.sqrt(3)),
        (5, 4, 4, 3, 7.5),
        (0, 0, 0, 0, 0),
    ],
)
def test_triangle_compute_surface(base, c1, c2, h, expected):
    triangle = hw5.Triangle(base, c1, c2, h)

    output = triangle.compute_surface()

    assert output == pytest.approx(expected)


# Rectangle

def test_rectangle_init():
    rectangle = hw5.Rectangle(2, 3)

    assert rectangle.a == 2
    assert rectangle.b == 3


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 10),
        (4, 4, 16),
        (0.5, 1.5, 4),
        (0, 0, 0),
    ],
)
def test_rectangle_compute_perimeter(a, b, expected):
    rectangle = hw5.Rectangle(a, b)

    output = rectangle.compute_perimeter()

    assert output == pytest.approx(expected)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),
        (4, 4, 16),
        (0.5, 1.5, 0.75),
        (0, 7, 0),
    ],
)
def test_rectangle_compute_surface(a, b, expected):
    rectangle = hw5.Rectangle(a, b)

    output = rectangle.compute_surface()

    assert output == pytest.approx(expected)


# Circle

def test_circle_init():
    circle = hw5.Circle(2)

    assert circle.radius == 2


@pytest.mark.parametrize(
    "radius, expected",
    [
        (1, 2 * math.pi),
        (2.5, 5 * math.pi),
        (0, 0),
    ],
)
def test_circle_compute_perimeter(radius, expected):
    circle = hw5.Circle(radius)

    output = circle.compute_perimeter()

    assert output == pytest.approx(expected)


@pytest.mark.parametrize(
    "radius, expected",
    [
        (1, math.pi),
        (2.5, 6.25 * math.pi),
        (0, 0),
    ],
)
def test_circle_compute_surface(radius, expected):
    circle = hw5.Circle(radius)

    output = circle.compute_surface()

    assert output == pytest.approx(expected)
