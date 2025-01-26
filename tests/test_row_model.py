from pydantic_excel.row_model import BaseRowModel


class SimpleRow(BaseRowModel):
    product_id: int  # Auto: header="Product Id", format="NUMBER"
    price: float  # Auto: header="Price", format="CURRENCY"
    description: str


def test_row_model():
    assert True
