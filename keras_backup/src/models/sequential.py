"""Compatibility shim for `keras.src.models.sequential`.

This module provides aliases to `tensorflow.keras.models.Sequential` and
`tensorflow.keras.models.Model` so that pickled objects referencing the
original `keras.src.models.sequential` module can be unpickled.
"""

from tensorflow.keras.models import Sequential as Sequential
from tensorflow.keras.models import Model as Model

# Expose symbols expected by unpickling
__all__ = ["Sequential", "Model"]
