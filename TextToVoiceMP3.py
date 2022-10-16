class TextToVoice:
    def T_V(self):
        while(1):
            try:
                from gtts import gTTS
                import os
                # forFile=open("text.txt","r")
                # forFileText=forFile.read().replace("\n"," ")
                myText = input("[+]enter your text: ")
                language = 'en-in'
                output = gTTS(text=myText, lang=language, slow=False)
                output.save("output.mp3")
                os.system("start output.mp3")
            except:
                print("sorry for your interption can you say it again")