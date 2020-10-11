import playsound
from gtts import gTTS
import os
import wolframalpha
from selenium import webdriver
import speech_recognition as sr
import os
import sys
import re
import webbrowser
import smtplib
import requests
import subprocess
from pyowm import OWM
import youtube_dl
import vlc
import urllib
#import urllib2
import json
from bs4 import BeautifulSoup as soup
#from urllib2 import urlopen
from urllib.request import urlopen
import wikipedia
import random
from time import strftime

num = 1
def assistant_speaks(output):
    global num

    # Global value is updated to ensure that all unique files are named uniquely
    num += 1
    print("Assistant: " + output)

    ''' Could be further improved to allow slow speech if prompted to repeat'''
    toSpeak = gTTS(text=output, lang='en', slow=False)

    # saving the audio file given by google text to speech
    file = str(num) + ".mp3"
    toSpeak.save(file)

    # playsound package is used to play the same file. Then remove the file.
    playsound.playsound(file, True)
    os.remove(file)



def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say something...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
    except sr.UnknownValueError:
        print('....')
        command = myCommand()
    return command


# function used to open application
# present inside the system.                        We also want relative paths for github
def open_application(input):
    if "chrome" in input:
        assistant_speaks("Opening Google Chrome")
        os.startfile('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe')
        return

    elif "firefox" in input or "mozilla" in input:
        assistant_speaks("Opening Mozilla Firefox")
        os.startfile('C:/Program Files/Mozilla Firefox/firefox.exe')
        return

    elif "word" in input:
        assistant_speaks("Opening Microsoft Word")
        os.startfile('C:/Program Files (x86)/Microsoft Office/root/Office16/WINWORD.EXE')
        return

    elif "virtualbox" in input or "virtual machine" in input:
        assistant_speaks("Opening Oracle VM Virtual Box")
        os.startfile('C:/Program Files/Oracle/VirtualBox/VirtualBox.exe')
        return

    elif "command prompt" in input:
        assistant_speaks("Opening the Command Prompt")
        os.startfile('C:/Users/Denis/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/System Tools/Command Prompt.lnk')
        return

    elif "snipping tool" in input:
        assistant_speaks("Opening the snipping tool")
        os.startfile('C:/Windows/System32/SnippingTool.exe')
        return

    elif "control panel" in input:
        assistant_speaks("Opening the control panel")
        os.startfile('C:/Users/Denis/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/System Tools/Control Panel.lnk')
        return

    elif "file explorer" in input or "files" in input:
        assistant_speaks("Opening the file explorer")
        os.startfile('C:/Users/Denis/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/System Tools/File Explorer.lnk')

    else:
        assistant_speaks("Application not available, or not currently supported by me")
        return


def search_web(input):
    driver = webdriver.Firefox()
    driver.implicitly_wait(1)
    driver.maximize_window()

    if 'youtube' in input.lower() or 'play' in input.lower():

        assistant_speaks("Opening in youtube")
        indx = input.lower().split().index('youtube')
        query = input.split()[indx + 1:]
        print("http://www.youtube.com/results?search_query=" + '+'.join(query))
        driver.get("http://www.youtube.com/results?search_query=" + '+'.join(query))
        return

    elif 'wikipedia' in input.lower():

        assistant_speaks("Opening in Wikipedia")
        indx = input.lower().split().index('wikipedia')
        query = input.split()[indx + 1:]
        driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query))
        return

    else:

        if 'google' in input.lower():
            assistant_speaks("Opening with Google")
            indx = input.lower().split().index('google')
            query = input.split()[indx + 1:]
            driver.get("https://www.google.com/search?q=" + '+'.join(query))

        elif 'search' in input.lower():
            assistant_speaks("Opening with Google")
            indx = input.lower().split().index('google')
            query = input.split()[indx + 1:]
            driver.get("https://www.google.com/search?q=" + '+'.join(query))

        else:

            driver.get("https://www.google.com/search?q=" + '+'.join(input.split()))

        return


wolframalpha_id = "WOLFRAMALPHA_APP_ID"             # Don't know it yet

def process_text(input):
    try:
        if 'search' in input or 'play' in input:
            # a basic web crawler using selenium
            search_web(input)
            return

        elif "who are you" in input or "define yourself" in input:
            speak = '''Hello, I am your personal Assistant. 
            I am here to make your life easier. You can command me to perform 
            various tasks such as calculating sums or opening applications etcetra'''
            assistant_speaks(speak)
            return

        elif "who made you" in input or "created you" in input:
            speak = "I have been created by Denis Rozhnov."
            assistant_speaks(speak)
            return

        elif 'open' in input:

            # another function to open
            # different application availaible
            open_application(input.lower())
            return

        elif "calculate" in input.lower():

            # write your wolframalpha app_id here
            app_id = wolframalpha_id
            client = wolframalpha.Client(app_id)

            indx = str(input).lower().split().index('calculate')
            query = str(input).split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            assistant_speaks("The answer is " + answer)
            return

        elif 'open' in input.lower():
            reg_ex = re.search('open (.+)', input)
            if reg_ex:
                domain = reg_ex.group(1)
                print(domain)
                url = 'https://www.' + domain
                webbrowser.open(url)
                assistant_speaks('The website you have requested has been opened for you Sir.')
            else:
                pass

        elif 'current weather in' in input.lower():
            reg_ex = re.search('current weather in (.*)', input)
            if reg_ex:
                try:
                    city = reg_ex.group(1)
                    owm = OWM(API_key='ab0d5e80e8dafb2cb81fa9e82431c1fa')
                    obs = owm.weather_at_place(city)
                    w = obs.get_weather()
                    k = w.get_status()
                    x = w.get_temperature(unit='celsius')
                    assistant_speaks(
                        'Current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius' % (
                            city, k, x['temp_max'], x['temp_min']))
                except:
                    assistant_speaks("You must say current weather in city")

        elif 'time' in input.lower():
            import datetime
            now = datetime.datetime.now()
            assistant_speaks('Current time is %d hours %d minutes' % (now.hour, now.minute))

        elif 'hello' in input.lower():
            day_time = int(strftime('%H'))
            if day_time < 12:
                assistant_speaks('Hello Sir. Good morning')
            elif 12 <= day_time < 18:
                assistant_speaks('Hello Sir. Good afternoon')
            else:
                assistant_speaks('Hello Sir. Good evening')

        elif 'news for today' in input.lower() or 'news' in input.lower() or "what's happening" in input.lower():
            try:
                news_url = "https://news.google.com/news/rss"
                Client = urlopen(news_url)
                xml_page = Client.read()
                Client.close()
                soup_page = soup(xml_page, "xml")
                news_list = soup_page.findAll("item")
                for news in news_list[:15]:
                    assistant_speaks(str(news.title.text))
            except Exception as e:
                print(e)

        elif 'tell me about' in input.lower():
            reg_ex = re.search('tell me about (.*)', input)
            try:
                if reg_ex:
                    topic = reg_ex.group(1)
                    ny = wikipedia.page(topic)
                    end_char = 1000
                    while(ny.content[end_char] != '.'):
                        end_char += 1
                    assistant_speaks(ny.content[:end_char])
            except Exception as e:
                assistant_speaks(e)

        else:

            assistant_speaks("I can search the web for you for " + str(input) + ", Do you want to continue?")
            ans = myCommand()
            if 'yes' in str(ans) or 'yeah' in str(ans):
                search_web(input)
            else:
                return

        '''elif 'play me a song' in command:
            path = 'C:/Users/Denis/Personal Projects/Virtual Personal Assistant'
            folder = path
            for the_file in os.listdir(folder):
                file_path = os.path.join(folder, the_file)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                except Exception as e:
                    print(e)
            sofiaResponse('What song shall I play Sir?')
            mysong = myCommand()
            if mysong:
                flag = 0
                url = "https://www.youtube.com/results?search_query=" + mysong.replace(' ', '+')
                response = urllib2.urlopen(url)
                html = response.read()
                soup1 = soup(html, "lxml")
                url_list = []
                for vid in soup1.findAll(attrs={'class': 'yt-uix-tile-link'}):
                    if ('https://www.youtube.com' + vid['href']).startswith("https://www.youtube.com/watch?v="):
                        flag = 1
                        final_url = 'https://www.youtube.com' + vid['href']
                        url_list.append(final_url)
                        url = url_list[0]
                ydl_opts = {}
                os.chdir(path)
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                vlc.play(path)
                if flag == 0:
                    sofiaResponse('I have not found anything in Youtube ')'''

    except:

        assistant_speaks("I don't understand, I can search the web for you, Do you want to continue?")
        ans = myCommand()
        if 'yes' in str(ans) or 'yeah' in str(ans):
            search_web(input)


''' Make Big Brother is always watching you said at random - user can select to turn off that functionality '''
# Driver Code
if __name__ == "__main__":
    name = 0
    assistant_speaks("What's your name?")
    while name == 0:
        name = 'Human'
        name = myCommand()
    assistant_speaks("Hello, " + str(name) + '.')

    while (1):

        assistant_speaks("What can i do for you?")
        text = str(myCommand()).lower()

        if text == 0:
            continue

        if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text):
            assistant_speaks("Ok bye, " + str(name) + '.')
            break

        if "be quiet computer" in str(text) or "computer be quiet" in str(text):
            print("Done")
            assistant_speaks("Sorry")
            break

        # calling process text to process the query
        process_text(text)
