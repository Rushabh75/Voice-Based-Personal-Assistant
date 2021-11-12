import PyPDF2
import re
from PyPDF2 import PdfFileReader as R
from fpdf import FPDF



class PDFsum():
    def __init__(self,search,file,cwd):
        target = cwd+"/"+file+".pdf"
        object = PyPDF2.PdfFileReader(target)

        NumPages = object.getNumPages()
        String = search
        x = ""
        lst = []

        for i in range(0, NumPages):
            PageObj = object.getPage(i)
            Text = PageObj.extractText()
            ResSearch = re.search(String, Text)
            if (ResSearch != None):
                f = open(target, "rb")
                pdf = R(f)
                page_no = i
                lst.append(page_no)
                P_O = pdf.pages[page_no]
                y = P_O.extractText()
                x = x + " " + y
                f.close()
        import os
        from PyPDF2 import PdfFileReader, PdfFileWriter

        pdf_file_path = target


        pdf = PdfFileReader(pdf_file_path)

        pages = lst  # page 1, 3, 5
        pdfWriter = PdfFileWriter()

        for page_num in pages:
            pdfWriter.addPage(pdf.getPage(page_num))

        with open('{}_{}.pdf'.format(file, String), 'wb') as f:
            pdfWriter.write(f)
            f.close()
        path = '{}_{}.pdf'.format(file, String)
        os.system(path)
        print(path + "opened")
