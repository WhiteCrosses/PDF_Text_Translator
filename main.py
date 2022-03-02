import PyPDF2
import re
from googletrans import Translator



translator = Translator()


global file
global re_en


def filename():
    file = input("Nazwa pliku: ")
    return file

def metadata():
    global file
    global pdfReader

    print(f"This PDF has {pdfReader.numPages} pages.\n\n")

def text():
    global en_
    global file

    PageObject = pdfReader.getPage(2)
    TextObject = str(PageObject.extractText())


    en_en = re.sub('[\r\n?|\n][\r\n?|\n]', 'JP2GMD', TextObject,) #enter + enter
    en_my = re.sub('-'+"(\r\n?|\n)", '', en_en) #myślnik + enter
    en_ = re.sub("(\r\n?|\n)", ' ', en_my) #enter
    re_en = re.sub('JP2GMD', ' \n', en_)
    re_en = str(re_en)

    open('test.txt', 'w').close()
    file1=open('test.txt',"a")
    file1.writelines(en_)
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


filename()

pdfFileObject = open('Fake News.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObject)

metadata()
text()
translate()

#if __name__ == '__main__':
    #test()