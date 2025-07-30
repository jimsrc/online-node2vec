"""Top-level package for online_node2vec.

Exposes submodules for public use and stores the library version.
"""

from importlib import metadata as _metadata

# Public sub-packages
# from online_node2vec import data as _data  # noqa: F401
from online_node2vec import evaluation as _evaluation  # noqa: F401
from online_node2vec import offline as _offline  # noqa: F401
from online_node2vec import online as _online  # noqa: F401

# Library version (taken from package metadata when installed)
try:
    __version__: str = _metadata.version(__name__)
except _metadata.PackageNotFoundError:  # pragma: no cover – during local dev
    # Fallback when the package hasn't been installed yet (editable mode)
    __version__ = "0.0.0+dev"

__all__: list[str] = [
    "__version__",
    # "_data",
    "_evaluation",
    "_offline",
    "_online",
]
