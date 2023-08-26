import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time
# import pyaudio


def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        recognizer.adjust_for_ambient_noise(source)   #noise remove variable
        audio = recognizer.listen(source)
        try:
            print("Recognizing. ......")
            data = recognizer.recognize_google(audio)
            print(data)
            return data     #condition
        except sr.UnknownValueError:
            print("not understand")
# sptext()
  

# # dk = input("enter the string --------->")

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)   # 1--->female ,   0---->Male Voice
    rate = engine.getProperty('rate')
    engine.setProperty('rate',120)
    engine.say(x)
    engine.runAndWait()
# speechtx()

'''Tell me about yourself
My name is Deepak Prajapat, I am from Jaipur, Rajasthan. I have completed my secondary from Sarasvati Bal Deep Sen. Sec.  School, Jaipur (Rajasthan) with 70% in 10th standard and higher secondary from GOVT. Higher School, Jaipur (Rajasthan) with 77.80% in 12th standard.
Currently, I am pursuing B.Tech from Arya College of Engineering and Research Centre in the Computer Science discipline. My aggregate till 4th semester is 89% and working as a freelance worker.
I have my specialization in Python Programming Language and want to get recognized as a Data Scientist as I have completed my Data Course from GUVI and Great Learning. Adding to this, I can code in C and C++, and I can do Web designing as well and have a good knowledge of database concepts using SQL tools and good knowledge in data structure and algorithm. In addition to all above, I have good knowledge of Microsoft Office suite (word, PowerPoint, Excel, outlook), Adobe Acrobat. I am practicing real life problems and smart ways to code and practice new libraries in Python.
Apart from my technical skills, I am good in making strategies for markets and new plans, lead the team, manage task and time management. 
I am good at speaking, painting and playing Cricket and I had won many medals in my school Life. I love to code in my free time and have a link with websites like geeksforgeeks.'''
# print("succesful speech")

# if __name__== '__main__':
#     if sptext().lower() == "Deepak":
#         print("test")
#     else:
#         print("thanks")  




if __name__== '__main__':
    if "deepak" in sptext().lower():
        while True:
            data1 = sptext().lower()
            if "your name" in data1:
                name = "my name is deepak"
                speechtx(name)

            elif "how old are you" in data1:
                age = "i am 20 year old"
                speechtx(age)

            elif "now time" in data1:
                time = datetime.datetime.now().strftime("%I%M%p")
                speechtx(time)

            elif 'youtube' in data1:
                webbrowser.open("https://www.youtube.com/")

            elif 'web' in data1:
                webbrowser.open("https://chat.openai.com/")
            

            elif "joke" in data1:
                joke_1 = pyjokes.get_joke(language="en",category= 'neutral')
                print(joke_1)
                speechtx(joke_1)

            elif 'play song' in data1:
                add = "C:\Video's"
                listsong = os.listdir(add)
                print(listsong)
                os.startfile(os.path.join(add,listsong[0]))

            elif 'exit ' in data1:
                speechtx("thanks")
                break
            time.sleep(10)

    else:
        print("thanks")  