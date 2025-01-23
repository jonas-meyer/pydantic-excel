"""The `version` module holds the version information for Pydantic-Excel"""

from __future__ import annotations as _annotations

__all__ = "VERSION", "version_info"

VERSION = "0.0.1"


def version_short() -> str:
    """Return the `major.minor` part of Pydantic-Excel version.

    It returns '2.1' if Pydantic-Excel version is '2.1.1'
    """
    return ".".join(VERSION.split(".")[:2])


def version_info() -> str:
    """Return complete version information for Pydantic-Excel and its dependencies"""
    import platform
    import sys
    from pathlib import Path
    import pydantic as pd

    info = {
        "pydantic-excel version": VERSION,
        "pydantic version": pd.__version__,
        "install path": Path(__file__).resolve().parent,
        "python version": sys.version,
        "platform": platform.platform(),
    }

    return "\n".join("{:>30} {}".format(k + ":", str(v).replace("\n", " ")) for k, v in info.items())
