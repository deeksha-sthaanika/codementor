from PyPDF2 import PdfReader
import pandas as pd

class Utility:
    @staticmethod
    def readPdf(filename):
        '''
        :read text from pdf and return rawtext
        '''
        pdfreader = PdfReader(filename)
        raw_text = ''
        for i, page in enumerate(pdfreader.pages):
            content = page.extract_text()
            if content:
                raw_text += content

        return raw_text

    @staticmethod
    def readTxt(filename):
        '''
        :read text from txt format and return raw text
        '''
        with open(filename, 'r') as file:
            raw_text = file.read()
            
        return raw_text
    
    @staticmethod
    def readExcel(filename):
        '''
        :read text from excel format and return raw text in paragraph
        '''
        df = pd.read_excel(filename)
        raw_text = '. '.join(list(df['standard']))
        return raw_text
    
    @staticmethod
    def readCsv(filename):
        '''
        :read text from txt format and return raw text in paragraph
        '''
        df = pd.read_csv(filename)
        raw_text = '. '.join(list(df['standard']))
        return raw_text
    
    @staticmethod
    def readPy(filename):
        '''
        :read text from PY format and return raw text
        '''
        with open(filename, 'r') as file:
            raw_text = file.read()
            
        return raw_text
    
    @staticmethod
    def readSQL(filename):
        '''
        :read text from sql format and return raw text
        '''
        with open(filename, 'r') as file:
            raw_text = file.read()
            
        return raw_text
