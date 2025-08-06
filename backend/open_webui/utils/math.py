"""Mathematical utility functions."""

from typing import Union

Number = Union[int, float]

def cube(value: Number) -> Number:
    """Return the cube of ``value``.

    Parameters
    ----------
    value: Union[int, float]
        Numeric value to cube.

    Returns
    -------
    Union[int, float]
        The result of ``value`` raised to the third power.
    """
    return value ** 3
