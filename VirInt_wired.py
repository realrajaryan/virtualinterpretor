import speech_recognition as sr
import serial
import time
ser1 = serial.Serial('COM5', 9600)
r = sr.Recognizer()
r.energy_threshold = 4000
keywords = ['hello', 'goodbye', 'welcome', 'thanks']
with sr.Microphone() as source:
    print("Please wait, calibrating microphone..")
    r.adjust_for_ambient_noise(source)
    print("Listening...")
    for i in range(1, 10):
        audio = r.listen(source, timeout=2.5)
        try:
            string = r.recognize_google(audio)
            list_speech = string.split()
            print (len(list_speech))
            for i in range(len(list_speech)):
                print (list_speech)
                if list_speech[i] in keywords:
                    print("Keywords found '" + list_speech[i] + "'")
                    print ('i=',i)
                    index = keywords.index(list_speech[i])
                    print (index, list_speech[i], keywords[index])
                    if (keywords[index] == 'hello'):
                        ser1.write('1'.encode())
                    if (keywords[index] == 'thanks'):
                        ser1.write('2'.encode())
                    if (keywords[index] == 'goodbye'):
                        ser1.write('3'.encode())
                    if (keywords[index] == 'welcome'):
                        ser1.write('4'.encode())
        except sr.UnknownValueError:
            print("Could not understand audio, try again")
        except sr.RequestError as e:
            print("Google error: (0)".format(e))

