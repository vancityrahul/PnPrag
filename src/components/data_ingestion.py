import sys
import PyPDF2 as pdf2
import json
import pandas as pd
from src.logging import logging
from src.exception import PnpragException

class DataIngestion:
    def __init__(self, file):
        self.file = file

    def _pdf_file(self):
        try:
            with open(self.file, "rb") as f:
                pdf = pdf2.PdfReader(f)
                return pdf
        except:
            raise PnpragException("Error reading file: ", sys)

    def _json_file(self):
        try:
            with open(self.file, "r") as f:
                data = json.load(f)
                return data
        except:
            raise PnpragException("Error decoding JSON file: ", sys)

    def _txt_file(self):
        try:
            with open(self.file, "r") as f:
                return f.read()
        except:
            raise PnpragException("Error reading file: ", sys)

    def _csv_file(self):
        try:
            df = pd.read_csv(self.file)
            return df
        except:
            raise PnpragException("Error reading file: ", sys)