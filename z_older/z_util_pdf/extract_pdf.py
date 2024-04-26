import PyPDF2

from util.elastic_data import ElasticData


def readPDF(path):

    # pdf file object
    # you can find find the pdf file with complete code in below
    pdfFileObj = open(path, 'rb')
    # pdf reader object
    pdfReader = PyPDF2.PdfReader(pdfFileObj)

    # loop through pages in pdf
    text=""
    counter=0;
    print(len(pdfReader.pages))

    for pageObj in pdfReader.pages:
        
        # extracting text from page.
        # this will print the text you can also save that into String
        text += pageObj.extract_text() 

        print("Completed page "+str(counter))
        counter+=1
    
    # sanitize text
    text = text.replace("\n","")
    print(text)

    return text



def prepareElasticModel(text, name):
    eModel = ElasticData()

    eModel.name = name
    eModel.text = text
    return eModel
