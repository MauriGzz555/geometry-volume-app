from geometry.cylinder import volume_cylinder
import math
import pytest

def test_volume_cylinder_valid_inputs():
    """
    Test volume computation for valid cylinder dimensions.
    """
    radius, height = 1.0, 2.0
    expected = math.pi * radius**2 * height  #Same formula as cylinder.py is used due to the high amount of decimals.
    assert volume_cylinder(radius,height) == expected

def test_volume_cylinder_negative_dimension():
    """
    Document current behavior when a negative dimension is used.
    """
    radius, height = -1.0, 2.0
    expected = math.pi * radius**2 * height
    assert volume_cylinder(radius,height) == expected

def test_volume_cylinder_float_tolerance():
    """
    Test volume computation using approximate comparison
    """
    radius, height = 1.1, 2.2
    expected = math.pi * radius**2 * height
    assert volume_cylinder(radius,height) == expected

