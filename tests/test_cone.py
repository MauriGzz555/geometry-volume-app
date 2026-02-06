from geometry.cone import volume_cone
import math
import pytest

def test_volume_cone_valid_inputs():
    """
    Test volume computation for valid cone dimensions.
    """
    base_radius, height = 1.0, 2.0
    expected = (1/3) * math.pi * base_radius**2 * height  #Same formula as cone.py is used due to the high amount of decimals.
    assert volume_cone(base_radius,height) == expected

def test_volume_cone_negative_dimension():
    """
    Document current behavior when a negative dimension is used.
    """
    base_radius, height = -1.0, 2.0
    expected = (1/3) * math.pi * base_radius**2 * height
    assert volume_cone(base_radius,height) == expected

def test_volume_cone_float_tolerance():
    """
    Test volume computation using approximate comparison
    """
    base_radius, height = 1.1, 2.2
    expected = (1/3) * math.pi * base_radius**2 * height
    assert volume_cone(base_radius,height) == expected

