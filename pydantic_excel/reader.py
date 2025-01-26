from fastexcel import ExcelReader


class ExcelAdapter:
    """Decouples fastexcel operation from model logic"""

    def __init__(self, reader: ExcelReader):
        self.reader = reader
