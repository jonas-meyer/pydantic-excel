from typing import Any

from pydantic_excel.model import BaseExcelModel


class ExcelColumnConfig:
    """Optional Excel metadata with sensible defaults"""

    def __init__(self, header: str | None = None, format: str | None = None, _order: int = 0):
        self.header = header
        self.format = format
        self._order = _order


class BaseRowModel(BaseExcelModel):
    """Row model with automatic Excel column mapping"""

    @classmethod
    def __init_subclass__(cls, **kwargs: Any):
        super().__init_subclass__()
