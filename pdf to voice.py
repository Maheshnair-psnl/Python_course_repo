import requests
import pdftotext
from gtts import gTTS

#Download the PDF file using HTTP request
pdf_url = "maheshpdf.pdf" 			#file saved in local directory
response = requests.get(pdf_url)

#Save the PDF file locally
pdf_filename = "sample.pdf"
with open(pdf_filename, "wb") as f:
    f.write(response.content)

#Convert PDF to text
with open(pdf_filename, "rb") as f:
    pdf = pdftotext.PDF(f)

raw = "\n".join(pdf)

tts = gTTS(text=raw, lang="en")

# Step 5: Save the audio file
audio_filename = "audiobook.mp3"
tts.save(audio_filename)

print("Audiobook conversion complete. Saved as", audio_filename)
