from pyttsx3 import *
import speech_recognition as spr
import webbrowser as wb
from PyDictionary import PyDictionary
import wikipedia
import os
import time
import psutil
import platform
chrome_path="C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s"
x=0
cu_time = time.localtime(time.time())
converter = init()
converter.setProperty('rate', 150) 
converter.setProperty('volume', 2.0)
cur_time = time.localtime(time.time())
if cur_time[3] >= 0 and cur_time[3] < 12:
    converter.say("Good Morning Sir")
    converter.runAndWait()
elif cur_time[3] >= 12 and cur_time[3] < 18 or ((cu_time[4] > 0 and cu_time[4] < 59) and cur_time[3] == 18):
    converter.say("Good Afternoon Sir")
    converter.runAndWait()
elif cur_time[3] > 18 or ((cu_time[4] > 0 and cu_time[4] < 59) and cur_time[3] == 18):
    converter.say("Good Evening Sir")
    converter.runAndWait()
converter.say("I am Oliver")
converter.runAndWait()
R=spr.Recognizer()


def openfile():
    count = 0
    fil = []
    converter.say("Openning Path Finder")
    converter.runAndWait()
    converter.say("Type the absolute filename with extension")
    converter.runAndWait()
    os.system('cls')
    filnam = input(str('Enter the file name - '))
    for r, d, f in os.walk("C:\\"):
        for files in f:
            if files == filnam:
                count += 1
                print(os.path.join(r, files))
    if count == 1:
        txt1 = 'location'
    else:
        txt1 = 'locations'
    zp = "This file is Located in" + str(count) + str(txt1)
    converter.say(zp)
    converter.runAndWait()


def wikisearch():
    s2="yes"
    converter.say("Turning on Wikipedia") 
    converter.runAndWait()
    while(s2=="yes" or s2=="Yes"):
        with spr.Microphone() as source:
            converter.say("What do you want to search about?") 
            converter.runAndWait()
            aud = R.listen(source)
        try:
            s = R.recognize_google(aud)   
            a = wikipedia.summary(s) 
            converter.setProperty('rate', 150) 
            converter.setProperty('volume', 0.7)
            print(a)
            converter.say(a) 
            converter.runAndWait() 
        except Exception as e:
            converter.say("Sorry Sir, there is an error") 
            converter.runAndWait()
            exit()
        try:
            converter.say("Do you wish to continue?") 
            converter.runAndWait()
            with spr.Microphone() as source:
                aud2 = R.listen(source)
            s2 = R.recognize_google(aud2)
        except Exception as e2:
            converter.say("Sorry Sir, there is an error") 
            converter.runAndWait()
            exit()
    else:
        converter.say("Turning off Wikipedia") 
        converter.runAndWait()


def meaningword():
        dictionary=PyDictionary()
        s2="yes"
        converter.say("Turning on Dictionary") 
        converter.runAndWait()
        while(bool("yes" in s2)==True or bool("Yes" in s2)==True):
                with spr.Microphone() as source:
                    converter.say("Please tell me the word") 
                    converter.runAndWait()
                    aud = R.listen(source)
                try:
                    word = R.recognize_google(aud)
                    print(word)
                    converter.say(word)
                    converter.say(dictionary.meaning(word))
                except Exception as e:
                    converter.say("Sorry Sir, there is an error") 
                    converter.runAndWait()
                    exit()
                try:
                    converter.say("Do you wish to continue?") 
                    converter.runAndWait()
                    with spr.Microphone() as source:
                        aud2 = R.listen(source)
                        s2 = R.recognize_google(aud2)
                except Exception as e2:
                    converter.say("Sorry Sir, there is an error") 
                    converter.runAndWait()
                    exit()
        else:
            converter.say("Turning off Dictionary") 
            converter.runAndWait()

def songss():
    loc = "C:\\Users\\prakh\\Music\\Playlists"
    music = os.listdir(loc)
    os.startfile(os.path.join(loc, music[-1]))
while(x==0):
    try:
        with spr.Microphone() as source:
                            aud = R.listen(source)
                            text=R.recognize_google(aud)
                            if ("open Google" in text):
                                converter.say("Openning Google") 
                                converter.runAndWait()
                                wb.get(chrome_path).open("www.google.com")
                            elif ("open YouTube" in text):
                                converter.say("Openning YouTube") 
                                converter.runAndWait()
                                wb.get(chrome_path).open("www.youtube.com")
                            elif ("open WhatsApp" in text):
                                converter.say("Openning WhatsApp")
                                converter.runAndWait()
                                wb.get(chrome_path).open("web.whatsapp.com")
                            elif ("open Gmail" in text):
                                converter.say("Openning Gmail") 
                                converter.runAndWait()
                                wb.get(chrome_path).open("www.gmail.com")
                            elif ("open Facebook" in text):
                                converter.say("Openning Facebook") 
                                converter.runAndWait()
                                wb.get(chrome_path).open("www.facebook.com")
                            elif ("open Instagram" in text):
                                converter.say("Openning Instagram") 
                                converter.runAndWait()
                                wb.get(chrome_path).open("www.instagram.com")
                            elif ("your creator" in text):
                                converter.say("My creator is Prakhar, who is also having a Youtube Channel. Let me show you.")
                                converter.runAndWait()
                                wb.get(chrome_path).open("www.youtube.com/channel/UC6joIJYT--NwnSYC3o38A0A")
                            elif ("play music" in text):
                                songss()
                            elif ("MS Paint" in text):
                                os.system('mspaint')
                            elif ("shutdown" in text):
                                converter.say("Turning off your PC") 
                                converter.runAndWait()
                                os.system("shutdown /s /t 1") 
                            elif ("open dictionary" in text):
                                meaningword()
                            elif ("open wikipedia" in text):
                                wikisearch()
                            elif ("open notepad" in text):
                                os.system('notepad')
                            elif ("how are you" in text):
                                converter.say("I am fine Sir")
                                converter.runAndWait()
                            elif ("the time" in text):
                                cu_time = time.localtime(time.time())
                                converter.say(str(cu_time[3])+'hours'+str(cu_time[4])+'minutes')
                                converter.runAndWait()
                            elif ("list of games" in text):
                                converter.say('There are '+str(len(os.listdir('c:/games')))+'Games installed in your PC')
                                converter.runAndWait()
                                converter.say('Game Titles are '+str(os.listdir('c:/games')))
                                converter.runAndWait()
                            elif ("goodbye Oliver" in text):
                                converter.say("goodbye sir")
                                converter.runAndWait()
                                break
                            elif ("clear cache" in text):
                                '''loc2 = "C:\\Users"
                                foldr = os.listdir(loc)
                                for i in range(len(foldr)):
                                    try:
                                        os.chdir("C:\\Users\\" + foldr[i] + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cache")
                                    except:
                                        pass
                                os.system('DEL/F/Q/S *. *>NUL')
                                else:
                                    print('Google Chrome not Available')'''
                                os.system('Del /S /F /Q %temp%')
                                converter.say("All Cache files have been deleted")
                                converter.runAndWait()
                            elif ("the system" in text):
                                uname = platform.uname()
                                converter.say("System, "+ str(uname.system))
                                converter.runAndWait()
                                converter.say("Machine, " + str(uname.machine))
                                converter.runAndWait()
                                converter.say("Processor, " + str(uname.processor))
                                converter.runAndWait()
                                converter.say('Your Computer has '+str(psutil.cpu_count(logical=False))+" Physical cores "+'and '+str(psutil.cpu_count(logical=True))+" Total Cores")
                                converter.runAndWait()
                                cpufreq = psutil.cpu_freq()
                                a = f"Maximum Frequency: {cpufreq.max:.2f}Mhz"
                                b = f"Minimum Frequency: {cpufreq.min:.2f}Mhz"
                                c = f"Current Frequency: {cpufreq.current:.2f}Mhz"
                                converter.say(str(a+' '+b+' '+c))
                                converter.runAndWait()
                            elif ("open zoom" in text):
                                converter.say("Openning Zoom")
                                converter.runAndWait()
                                os.system('C:\\Users\\prakh\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe')
                            elif ("location of a file" in text):
                                openfile()
                            elif ("weather of " in text):
                                from bs4 import BeautifulSoup
                                import requests
                                area1 = text[11:]
                                r = requests.get('https://www.google.com/search?sxsrf=' +
                                                 'ALeKk001t27n2Ott-CxnbmlcfPOXXNuLPA%3A1593587990124&source=hp&ei=Fjn8XvDVBamc4-EPtdKG4Aw&q=temperature+in+' + area1)

                                soup = BeautifulSoup(r.text, 'lxml')
                                c = 0
                                for A_Tag in soup.select('div[class*="BNeawe iBp4i AP7Wnd"]'):
                                    if c == 1:
                                        break
                                    Degree = A_Tag.get_text()
                                    c += 1
                                c = 0
                                for A_Tag in soup.select('div[class*="BNeawe tAd8D AP7Wnd"]'):
                                    if c == 1:
                                        break
                                    Details = A_Tag.get_text()
                                    c += 1
                                converter.say(Degree)
                                converter.runAndWait()
                                converter.say(Details)
                                converter.runAndWait()
                            elif ("Google search" in text):
                                converter.say("What do you want to search?") 
                                converter.runAndWait()
                                with spr.Microphone() as source:
                                    aud = R.listen(source)
                                    text=R.recognize_google(aud)
                                wb.get(chrome_path).open("https://www.google.com/search?sxsrf=ALeKk013qnQa-UGIShrONYnYPij5-DzSdw%3A1592319137337&source=hp&ei=odzoXquFEqKYmgeuu5PoAw&q="+text)
        exit()
    except:
        pass