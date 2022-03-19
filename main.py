import PyPDF2
import re
from googletrans import Translator



translator = Translator()


global file
global re_en
global whatpage

def filename():
    file = input("File name: ")
    return file

def numpages():
    global whatpage
    running = True
    while running:
        whatpage = input("Page: ")
        if int(whatpage) > pdfReader.numPages or int(whatpage) < 0 :
            print("Wrong page number!")
        else:
            running = False
    return whatpage

def metadata():
    global file
    global pdfReader

    print(f"This PDF has {pdfReader.numPages} pages.")

def text():
    global en_
    global file
    global whatpage

    PageObject = pdfReader.getPage(int(whatpage))
    TextObject = str(PageObject.extractText())


    #en_en = re.sub('[\r\n?|\n][\r\n?|\n]', 'JP2GMD', TextObject,) #enter + enter
    format = re.sub('-'+"(\r\n?|\n)", '', TextObject) #myślnik + enter
    format = re.sub("(\r\n?|\n)", ' ', format) #enter
    #re_en = re.sub('JP2GMD', '\n', en_)
    #re_en = re.sub('  ', '\n', re_en)
    #format = format.replace(' \t', ' \n')
    #format = re.sub([ \t], '\n', format)

    open('test.txt', 'w').close()
    file1=open('test.txt',"a")
    file1.writelines(format)
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
numpages()
text()
translate()

#if __name__ == '__main__':
    #test()