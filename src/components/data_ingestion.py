from dataclasses import dataclass
from src.exception import PnpragException
import sys
import json
import PyPDF2 as p
import pandas as pd

@dataclass
class DataIngestionConfig():
    baseUrl = ""
    acceptedType : { "json" , "pdf" ,"txt" ,"csv" }

class DataIngestion():
    def __init__(self ,fileName, filePath='input/'):
        self.config = DataIngestionConfig()
        self.fileName :str = fileName
        self.filePath :str = filePath

    def read(self):
        try :
            if self.fileName.split('.')[-1] not in self.config.acceptedType:
                raise PnpragException("File type Not Supported" ,sys)
            match self.fileName.split('.')[-1] :
                case 'json':
                    return self._read_json()
                case 'pdf':
                    return self._read_pdf()
                case 'txt':
                    return self._read_txt()
                case 'csv':
                    return self._read_csv()   
        except Exception as e : raise PnpragException(e ,sys)
    
    def _read_json(self):
        try :
            with open(f'{self.filePath}{self.fileName}' , "r") as f:
                return json.load(f)
        except : raise PnpragException("Error reading JSON file" ,sys)

    def _read_txt(self):
        try :
            with open(f'{self.filePath}{self.fileName}' , "r") as f:
                return f.read()
        except : raise PnpragException("Error reading TXT file" ,sys)
            
    def _read_pdf(self):
        try :
            with open(f'{self.filePath}{self.fileName}' , "r") as f:
                return p.PdfReader(f)
        except : raise PnpragException("Error reading PDF file" ,sys)
    
    def _read_csv(self):
        try :
            with open(f'{self.filePath}{self.fileName}' , "r") as f:
                return pd.read_csv(f)
        except : raise PnpragException("Error reading CSV file" ,sys)


