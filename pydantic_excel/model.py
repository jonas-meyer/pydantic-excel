from pathlib import Path
from fastexcel import ExcelReader
from pydantic import BaseModel
from typing import Any, TypeVar, overload


class BaseExcelColumns(BaseModel):
    pass


ModelT = TypeVar("ModelT", bound="BaseExcelModel")


class BaseExcelModel(BaseModel):
    """Base pydantic-excel model."""

    def model_validate_excel(cls: type[ModelT], source: Path | str, context: dict[str, Any] | None = None) -> ModelT:
        pass

    def model_dump_excel(self) -> None:
        pass


class BaseWorkBookModel(BaseExcelModel):
    pass


class BaseWorkSheetModel(BaseExcelModel):
    pass
