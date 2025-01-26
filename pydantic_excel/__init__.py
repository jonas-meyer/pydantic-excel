import typing
from .version import VERSION

if typing.TYPE_CHECKING:
    from .model import BaseExcelModel
    from .row_model import BaseRowModel

__version__ = VERSION
__all__ = ("BaseExcelModel", "BaseRowModel", "__version__", "VERSION")
