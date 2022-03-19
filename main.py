import PyPDF2
import re
from googletrans import Translator



translator = Translator()


global file
global re_en
file = 0

#def filename():
    #file = input("Nazwa pliku: ")
    #return file

def metadata():
    global file
    global pdfReader

    print(f"This PDF has {pdfReader.numPages} pages.\n\n")

def text():
    global en_
    global file

    PageObject = pdfReader.getPage(2)
    TextObject = str(PageObject.extractText())


    #edit = re.sub('[\r\n?|\n][\r\n?|\n]', 'JP2GMD', TextObject,) #enter + enter
    edit = re.sub('-'+"(\r\n?|\n)", '', TextObject) #myślnik + enter
    edit = re.sub("(\r\n?|\n)", ' ', edit) #enter
    edit = re.sub('JP2GMD', ' \n', edit)
    edit = str(edit)

    open('test.txt', 'w').close()
    file1=open('test.txt',"a")
    file1.writelines(edit)
    pdfFileObject.close()

def translate():
    global re_en
    global file

    f = open('test.txt', 'r')
    text = f.read()
    result = translator.translate(text = text, src='en', dest='pl')
    print(result)
    open('test.txt', 'w').close()
    file1 = open('test.txt', "a")
    file1.writelines(str(result))
    pdfFileObject.close()

pdfFileObject = open(input("Nazwa pliku: "), 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObject)

metadata()
text()
translate()

#if __name__ == '__main__':
    #test()