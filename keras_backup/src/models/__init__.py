"""shim package: keras.src.models

This module exposes the objects that pickled models may import from
`keras.src.models.*`. It re-exports tensorflow.keras implementations.
"""

from .sequential import Sequential, Model

__all__ = ["Sequential", "Model"]
