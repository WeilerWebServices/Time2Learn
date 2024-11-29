from gtts import gTTS
import os

def speak_text(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    tts.save("output.mp3")
    os.system("mpv output.mp3")

if __name__ == "__main__":
    speak_text("Hello, welcome to Time2Learn!")
