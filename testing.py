from gtts import gTTS
from pypdf import PdfReader
import os
print("enter the pdf file name in the format  ---> FileName.pdf")
string=input()
read=PdfReader(string)
page=read.pages[0]
text=page.extract_text()
print("converting the pdf to an audiobook")
obj=gTTS(text=text,lang='en',slow=False)
obj.save("test.mp3")
os.system("start test.mp3")
