import speech_recognition as sr
import webbrowser


print("welcome to my tools\n\n")

print("enter ur requirements .... We are listening ...",end='')
#ch=input()

r=sr.Recognizer()

with sr.Microphone() as source:
    print('start saying..')
    p=  r.listen(source)
    print('We got it .. Please Wait ..')


ch=r.recognize_google(p)

if ("date" in ch) and ("run" in ch) or ("execute" in ch):
          webbrowser.open("http://192.168.0.107/cgi-bin/iiec.py?x=date")
elif  "calender" in ch:
          webbrowser.open("http://192.168.0.107/cgi-bin/iiec.py?x=cal")
else:
    print("not understand")
