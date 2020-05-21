import speech_recognition as sr
import playsound
from gtts import gTTS
import os
import wolframalpha
from selenium import webdriver

num = 1
def assistant_speaks(output):
    global num

    # Global value is updated to ensure that all unique files are named uniquely
    num += 1
    print("Person: " + output)

    ''' Could be further improved to allow slow speech if prompted to repeat'''
    toSpeak = gTTS(text=output, lang='en', slow=False)

    # saving the audio file given by google text to speech
    file = str(num) + ".mp3"
    toSpeak.save(file)

    # playsound package is used to play the same file. Then remove the file.
    playsound.playsound(file, True)
    os.remove(file)



def get_audio():
    rObject = sr.Recognizer()
    audio = ''

    with sr.Microphone() as source:
        print("Speak...")

        # recording the audio using speech recognition
        ''' Could be further improved by making the phrase_time_limit depend on duration of speech '''
        audio = rObject.listen(source, phrase_time_limit=10)
    print("Stop.")  # limit 10 secs

    try:

        text = rObject.recognize_google(audio, language='en-US')
        print("You : ", text)
        return str(text)

    except:

        assistant_speaks("Could not understand your audio, Please try again!")
        return 0


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
        driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query))
        return

    elif 'wikipedia' in input.lower():

        assistant_speaks("Opening Wikipedia")
        indx = input.lower().split().index('wikipedia')
        query = input.split()[indx + 1:]
        driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query))
        return

    else:

        if 'google' in input:

            indx = input.lower().split().index('google')
            query = input.split()[indx + 1:]
            driver.get("https://www.google.com/search?q =" + '+'.join(query))

        elif 'search' in input:

            indx = input.lower().split().index('google')
            query = input.split()[indx + 1:]
            driver.get("https://www.google.com/search?q =" + '+'.join(query))

        else:

            driver.get("https://www.google.com/search?q =" + '+'.join(input.split()))

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

        else:

            assistant_speaks("I can search the web for you, Do you want to continue?")
            ans = get_audio()
            if 'yes' in str(ans) or 'yeah' in str(ans):
                search_web(input)
            else:
                return

    except:

        assistant_speaks("I don't understand, I can search the web for you, Do you want to continue?")
        ans = get_audio()
        if 'yes' in str(ans) or 'yeah' in str(ans):
            search_web(input)


''' Make Big Brother is always watching you said at random - user can select to turn off that functionality '''
# Driver Code
if __name__ == "__main__":
    name = 0
    assistant_speaks("What's your name?")
    while name == 0:
        name = 'Human'
        name = get_audio()
    assistant_speaks("Hello, " + str(name) + '.')

    while (1):

        assistant_speaks("What can i do for you?")
        text = str(get_audio()).lower()

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