import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    audio = r.listen(source)
    print('Time is over, Thanks')

try:
    res = r.recognize_google(audio, language = 'bn-IN')
    print(res)
    saveFile = open('exampleFile','w')
    saveFile.write(res)
    saveFile.close()
except:
    pass
