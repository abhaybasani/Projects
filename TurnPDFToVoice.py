# -----------------------------Turn any PDF to Voice---------------------------------
class PDF_V:
    def PDFtoVoice(self):
        from win32com.client import Dispatch
        def speak(str):
            speak=Dispatch(("SAPI.SpVoice"))
            speak.Speak(str)
        #Importing Libraries
        #Importing Google Text to Speech library
        from gtts import gTTS
        #Importing PDF reader PyPDF2
        import PyPDF2

        #Open file Path
        user=input("Enter your exact location of your PDF file:> ")
        pdf_File = open(user, 'rb')

        #Create PDF Reader Object
        pdf_Reader = PyPDF2.PdfFileReader(pdf_File)
        count = pdf_Reader.numPages # counts number of pages in pdf
        textList = []

        #Extracting text data from each page of the pdf file
        for i in range(count):
           try:
            page = pdf_Reader.getPage(i)
            textList.append(page.extractText())
           except:
               pass

        #Converting multiline text to single line text
        textString = " ".join(textList)

        print(textString)
        speak(textString)