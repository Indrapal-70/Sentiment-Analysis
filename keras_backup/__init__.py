"""Local shim package to satisfy pickle imports referencing `keras.src`.

This package maps select keras modules to `tensorflow.keras` equivalents so
older pickled objects that reference `keras.src...` can be unpickled.
"""

__all__ = ["src"]
