from geometry.sphere import volume_sphere
import math
import pytest

def test_volume_sphere_valid_inputs():
    """
    Test volume computation for valid sphere dimensions.
    """
    radius = 1.0
    expected = (4 / 3) * math.pi * radius ** 3  #Same formula as sphere.py is used due to the high amount of decimals.
    assert volume_sphere(radius) == expected

def test_volume_sphere_negative_dimension():
    """
    Document current behavior when a negative dimension is used.
    """
    radius = -1.0
    with pytest.raises(ValueError) as exc_info:
        volume_sphere(radius)

    assert str(exc_info.value) == "Radius must be non-negative"

def test_volume_sphere_float_tolerance():
    """
    Test volume computation using approximate comparison
    """
    radius = 1.1
    expected = (4 / 3) * math.pi * radius ** 3  
    assert volume_sphere(radius) == expected

