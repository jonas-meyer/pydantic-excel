from pydantic import BaseModel


class BaseExcelColumns(BaseModel):
    pass


class BaseExcelModel(BaseModel):
    def to_excel(self):
        pass
