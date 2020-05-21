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

from gtts import gTTS
import playsound

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

# Used method from Geeks-4-Geeks because the method from Towards Data Science only works for Mac
num = 1
def sofiaResponse(output):
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

#sofiaResponse(myCommand())             # This is an echo

def assistant(command):
    if 'open' in command:
        reg_ex = re.search('open (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            print(domain)
            url = 'https://www.' + domain
            webbrowser.open(url)
            sofiaResponse('The website you have requested has been opened for you Sir.')
        else:
            pass

    elif 'current weather' in command:
        reg_ex = re.search('current weather in (.*)', command)
        if reg_ex:
            try:
                city = reg_ex.group(1)
                owm = OWM(API_key='ab0d5e80e8dafb2cb81fa9e82431c1fa')
                obs = owm.weather_at_place(city)
                w = obs.get_weather()
                k = w.get_status()
                x = w.get_temperature(unit='celsius')
                sofiaResponse(
                    'Current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius' % (
                    city, k, x['temp_max'], x['temp_min']))
            except:
                sofiaResponse("You must say current weather in city")

    elif 'time' in command:
        import datetime
        now = datetime.datetime.now()
        sofiaResponse('Current time is %d hours %d minutes' % (now.hour, now.minute))

    elif 'hello' in command:
        day_time = int(strftime('%H'))
        if day_time < 12:
            sofiaResponse('Hello Sir. Good morning')
        elif 12 <= day_time < 18:
            sofiaResponse('Hello Sir. Good afternoon')
        else:
            sofiaResponse('Hello Sir. Good evening')

    elif 'news for today' in command or 'news' in command:
        try:
            news_url = "https://news.google.com/news/rss"
            Client = urlopen(news_url)
            xml_page = Client.read()
            Client.close()
            soup_page = soup(xml_page, "xml")
            news_list = soup_page.findAll("item")
            for news in news_list[:15]:
                sofiaResponse(str(news.title.text.encode('utf-8')))
        except Exception as e:
            print(e)

    elif 'tell me about' in command:
        reg_ex = re.search('tell me about (.*)', command)
        try:
            if reg_ex:
                topic = reg_ex.group(1)
                ny = wikipedia.page(topic)
                sofiaResponse(str(ny.content[:1000].encode('utf-8')))
        except Exception as e:
            sofiaResponse(e)

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

while True:
    assistant(myCommand())