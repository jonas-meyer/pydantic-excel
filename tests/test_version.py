from unittest.mock import patch

import pytest
from packaging.version import parse as parse_version

import pydantic_excel
from pydantic_excel.version import version_info, version_short


def test_version_info():
    version_info_fields = [
        "pydantic-excel version",
        "pydantic version",
        "install path",
        "python version",
        "platform",
    ]

    s = version_info()
    assert all(f"{field}:" in s for field in version_info_fields)
    assert s.count("\n") == 4


def test_standard_version():
    v = parse_version(pydantic_excel.VERSION)
    assert str(v) == pydantic_excel.VERSION


def test_version_attribute_is_present():
    assert hasattr(pydantic_excel, "__version__")


def test_version_attribute_is_a_string():
    assert isinstance(pydantic_excel.__version__, str)


@pytest.mark.parametrize("version,expected", (("2.1", "2.1"), ("2.1.0", "2.1")))
def test_version_short(version, expected):
    with patch("pydantic_excel.version.VERSION", version):
        assert version_short() == expected
