# import os
# from gtts import gTTS
# from pygame import mixer
#
# my_file = open('hello.txt', 'r')
# my_text = my_file.read()
# my_file.close
#
# mixer.init()
# tts = gTTS(text=my_text, lang = 'en')
# tts.save("audio_1.mp3")
# mixer.music.load("audio_1.mp3")
# mixer.music.play()
# while mixer.music.get_busy():
#     time.sleep(1)
# mixer.music.upload()

import pyaudio
import speech_recognition as sr

recognize = sr.Recognizer()

with sr.Microphone() as sourse:
    print ('Скажи что-нибудь...')
    audio = recjgnize.listen(sourse)
speech = recognize.recognize_google(audio, language='ru_Ru')
print ('Вы сказали: ', speech)
