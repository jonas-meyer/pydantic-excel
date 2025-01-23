import typing
from .version import VERSION

if typing.TYPE_CHECKING:
    from .model import BaseExcelModel

__version__ = VERSION
__all__ = ("BaseExcelModel", "__version__", "VERSION")
