import fitz  # PyMuPDF

class ExtractTextFromPDF:

    def __init__(self,pdfPath):
        self.pdfDocument = fitz.open(pdfPath)
        self.text = self.extractText()

    def extractText(self):
        text = ""
        for page_num in range(len(self.pdfDocument)):
            page = self.pdfDocument.load_page(page_num)
            text += page.get_text()
        return text

    def getText(self):
        return self.text

    def __del__(self):
        if hasattr(self, 'pdfDocument'):
            self.pdfDocument.close()
    
