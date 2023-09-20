from PyPDF2 import PdfReader

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
