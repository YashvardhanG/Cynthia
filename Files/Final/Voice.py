#Modules
import os
import re
import webbrowser
from datetime import datetime
import pyowm
import sys
import time
from PyDictionary import PyDictionary
import random
import math
import psutil
from plyer import notification
import calendar
from gtts import gTTS
import speech_recognition as sr
from playsound import playsound
import translate
import pyaudio
import struct
import wave
import sounddevice as sd
from scipy.io.wavfile import write
language = 'en'

#Reminder Check
if os.path.exists('reminder.txt'):
    lists = open('reminder.txt','r')
    lines = lists.readlines()
    today1 = datetime.today()
    today = today1.strftime("%d/%m/%Y")
    n = len(lines)
    i=0
    while i<n:
        if today == lines[i].rstrip():
            text = lines[i+1].rstrip()
            notification.notify(title = 'Reminder for today', message = text, app_name = 'Cynthia', app_icon = 'icon.ico', timeout = 10)
        else:
            pass
        i = i+1
        
#Wake Up Keyword
if os.path.exists('wake_up.txt'):
    wake_up = open('wake_up.txt','r')
    lines = wake_up.readlines(1)
    keyword = lines[0]
    
else:
    with open('wake_up.txt', 'a') as a:
        a.write('laptop')
    keyword = 'laptop'    
    print('The default keyword has been set to ',keyword)

          
#Wake Up Command
def wake():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio).lower()

    except sr.UnknownValueError:
        wake()
        
    if keyword in text:
        myCommand()
    else:
        pass

#Assistant Speaking
def speak(command):
    myobj = gTTS(text=command, lang=language, slow=False)
    os.remove("command.mp3")
    myobj.save("command.mp3")
    playsound("command.mp3")

#Main Command Input
def myCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready')
        playsound("wake.mp3")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')
        main(command)

    except sr.UnknownValueError:
        speak("Please Repeat")
        command = myCommand();

#Inapp Command Input
def inapp():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Ready')
        playsound("wake.mp3")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        cd = r.recognize_google(audio).lower()
        return cd
    
    except sr.UnknownValueError:
        speak("Please Repeat")
        inapp();
    
#Main function
def main(command):
    #Youtube Facility
    if 'open youtube' in command:
        reg_ex = re.search('open youtube (.*)', command)
        url = 'https://www.youtube.com/'
        webbrowser.open(url)
        speak('Youtube Is opened')

    #Website Opener
    elif 'open website' in command:
        reg_ex = re.search('open website (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            text = domain.replace(" ", "")
            url = 'https://www.' + text + '.com'
            webbrowser.open(url)
            speak('Domain is opened')
        else:
            pass

    #Hello
    elif 'hello' in command:
        speak('Hello')

    #Search on Google
    elif 'search' in command:
            reg_ex = re.search('search (.+)', command)
            if reg_ex:
                domain = reg_ex.group(1)
                url = 'https://www.google.com/search?q=' + domain
                webbrowser.open(url)
                speak('In the process')

    #How are you
    elif 'how are you' in command:
            speak('I am very good!')

    #Domain opener with 'www'
    elif 'www' in command:
                reg_ex = re.search('www (.*)', command)
                url = command
                text = url.replace(" ", "")
                webbrowser.open(text)
                speak('That is being opened')

    #News Reader
    elif 'news' in command:
                speak("Do you want to see International News or National News?:")
                cd = inapp()
                if "international" in cd:
                        url = 'https://www.indiatoday.in/world'
                        webbrowser.open(url)
                        speak("Opening International News")
                elif "national" in cd:
                        url = 'https://in.reuters.com/'
                        webbrowser.open(url)
                        speak("Opening National News")
                else:
                    url = 'https://www.indiatoday.in/world'
                    webbrowser.open(url) 
                    speak("Here is some random news")


    #Music Player
    elif 'music' in command:
                speak("Would you like to listen to International Music or Hindi music?")
                cd = inapp()
                if "international" in cd:
                        url = 'https://gaana.com/playlist/gaana-dj-gaana-international-top-50'
                        webbrowser.open(url)
                        speak("Playing International Music")
                elif 'hindi' in cd:
                        url = 'https://gaana.com/playlist/gaana-dj-bollywood-top-50-1'
                        webbrowser.open(url)
                        speak("Playing Hindi Music")
                else:
                        url = 'https://gaana.com/playlist/gaana-dj-todays-top-5-international'
                        webbrowser.open(url)
                        speak("Here is some random music you might like")
                        
    #Introduction
    elif 'who are you' == command:
        speak("\nCynthia is a python based computer assistant which will help you in various kinds of things and reduce your effort of opening and executing things. \nFrom some basic functions like executing a countdown and telling about the weather, Cynthia can help you take down notes and read them too. \nCynthia  is an interactive assistant so asking some questions like (How are you), Cynthia will respond back to you. \nTo understand and know about the various commands that Cynthia has, you can say 'sample commands' as your command. \nGood Day!\nSpiral Cosmos, Copyright 2021\n")

    #List of all commands (Useless)
    elif 'list of commands' == command:
            speak('\nList of Commands:\n\n1.)To open any website on your computer, use "open website" and the website you want to open. (eg: open website youtube)\n2.)To take down a memo, use "memo" as your command.\n3.)To read out the written memo, use "read" and then type in the file you want to read. \n4.)To know the weather of a place, use "weather"\n5.)To search something on Google, use "search" followed by whatever you want to search.\n6.)For countdown, use "timer" as your command.\n7.)To open any website at all, you can directly type in the url starting with "www".\n8.)To use the calculator, type in "calculator" as the command.\n9.)To restart or shutdown your computer, enter "restart" or "shutdown" as your command.\n10.)To translate any of your text, put "translator" as your command.\n11.)To listen to fresh music, type "music" as your command.\n12.)To read latest news, type "news" as your command.\n13.)To open any desktop application, type in "application" as your command.\n14.)To search and go to a specific path, enter "path" as your command.\n15.)To view the clock, enter "clock" as your command.\n16.)To search a word in the dictionary, search "dictionary" as your command.\n17.)To roll a dice or flip a coin, put "roll" or "flip" as your command respectively.\n18.)To set up a pop-up notification, use "notification" in your command.\n19.)To check you battery status, use "battery" as your command.\n20.)To get amused, use "joke" as your command.\n21.)To learn something new, use "fact" as your command.\n22.)To view the calendar, use "calendar" in your command.\n23.)To check your flight status, use "flight" in your command.\n24.)To add a new folder in your computer, use "folder" in your command.\n25.)To make a To-Do-List, use "list" in your command.\n26.)To check your details, use "detail" in your command\n27.)To edit your current name, use "name" as the command.\n')                

    #List of sample commands (Useless)
    elif 'sample commands' == command:
            speak("Here are some sample commands which can be used in Cynthia:\n1.)open website youtube\n2.)Take down a memo\n3.)read a memo\n4.)tell the weather\n5.)search xyz\n6.)start a timer\n7.)www.facebook.com\n8.)open calculator\n9.)restart computer\n10.)shutdown computer\n11.)listen to music\n12.)show the news\n13.)open application\n14.)open translator\n15.)open path\n16.)show clock\n17.)roll a dice\n18.)Flip a coin\n19.)make a notification\n20.)tell me a joke\n21.)my battery status\n22.)tell me an interesting fact\n23.)show me the calendar\n24.)check my flight status\n25.)add a folder\n26.)make a list\n27.)show my details\n28.)change my name\n29.)open dictionary\n30.)help me with cynthia\n31.)exit cynthia")

    #Exit from the assistant
    elif 'bye' in command:
        speak('Bye')
        sys.exit()

    #Set a Timer
    elif 'timer' in command:
        speak('For what time in seconds? Please input a number')
        n = int(input("Enter:"))
        s=0
        while s<n:
            os.system('cls')
            print (s, 'Seconds')
            time.sleep(1)
            s+=1
        speak("Time's Up!")

    #Shutdown the device
    elif 'shutdown' in command:
        speak("Are you sure you want to shutdown your computer? Reply in a Yes or a No please")
        choice = inapp()
        if 'yes' in choice:
                os.system("shutdown /s /t 1")
        elif 'no' in choice:
                speak("Okay!")
        else:
                speak("I misheard I think, please try again")

    #Restart the device
    elif 'restart' in command:
        speak("Are you sure you want to restart your computer? Please reply in a Yes or a No")
        choice = inapp()
        if 'yes' in choice:
                os.system("shutdown /r /t 1")
        elif 'no' in choice:
                print("Okay")
        else:
                print("I misheard I think, please try again")

    #Text Translator
    elif 'translator' in command:
        url = 'https://cloud.google.com/translate/docs/languages'
        webbrowser.open(url)
        speak("The list of available languages and their codes have been opened in your web browser, please put the codes accordingly")
        speak('Please enter the text')
        text = input('Enter text:')
        speak('Please enter the code of the language')
        lang = input('Code of the language:')
        transtext = translate.translator('en',lang,text)
        speak("The translation of the text is")
        print(transtext)
        speak(transtext)
         
    #Memo Toolbar
    elif 'memo' in command:
        if not os.path.exists('Memos'):
                os.makedirs('Memos')
        else:
            pass
            
        speak("Do you want to create, read or delete a memo?")
        option = inapp()

        #Creating a memo
        if 'create' in option:
            speak('Please enter the name of the memo you want to create')
            name = input('Enter Name:')
            
            if os.path.exists('Memos\\'+name+'.txt'):
                speak('The name already exists, please change the name')
                speak('For future purposes, here are all the file names you already have')
                memos = os.listdir('Memos\\')
                for i in audio:
                    print(i.replace('.txt',''))
                main('memo')

            else:
                with open("Memos\\"+name + '.txt','a') as m:
                    speak("What should be the contents:")
                    text = inapp()
                    today1 = datetime.today()
                    date = today1.strftime("%d/%m/%Y")
                    m.write('\n')
                    m.write('{}'.format(date))
                    m.write('\n')
                    m.write(text)
                    notification.notify(title = 'Memo', message = 'A new memo has been saved', app_name = 'Cynthia', app_icon = 'icon.ico', timeout = 10)

        #Reading a memo
        elif 'read' in option:
            speak('Okay. The memos you have are')
            memos = os.listdir('Memos\\')
            l = []
            for i in memos:
                l.append(i.replace('.txt',''))
            for j in l:
                print(j)
                speak(j)
            
            speak("Which file do you want to read? Please input its name.")
            name = input('Enter name:')
            if os.path.exists("Memos\\"+name + '.txt'):
                speak("The content of this memo is:")
                m=open("Memos\\"+name + '.txt','r')
                text=m.readlines()
                body = text[2]
                print(body)
                speak(body)
                m.close()
            else:
                speak("File doesn't exist")

        #Deleting a memo
        elif 'delete' in option:
            speak('Okay, The memos you have are')
            memos = os.listdir('Memos\\')
            l = []
            for i in memos:
                l.append(i.replace('.txt',''))

            for j in l:
                print(j)
                speak(j)
                         
            speak("Which file do you want to delete? Please input its name.")
            name = input('\nWhich one do you want to delete?')

            if os.path.exists("Memos\\"+name + '.txt'):
                os.remove("Memos\\"+name + '.txt')
            else:
                speak("File doesn't exist")

        else:
            speak('Please try again')
            myCommand()

    #Open a specified path
    elif 'path' in command:
        speak('Please enter a path:')
        a=input("Enter the path which you want to open:")
        os.startfile(a)
        speak("Opened")

    #English Dictionary
    elif 'dictionary' in command:
        speak("Welcome to the English Dictionary")
        speak("Would you like to speak the word or type it")
        cd = inapp()

        if 'speak' in cd:
            speak('Okay, what is the word?')
            cd = inapp()
            meaning=PyDictionary.meaning(cd)
            for i in meaning.keys():
                text = meaning[i]
            speak('The meaning of the word is')
            print(str(text))
            speak(str(text))

        else:
            speak('Please type the word')
            a=input('Enter:')
            meaning=PyDictionary.meaning(a)
            for i in meaning.keys():
                text = meaning[i]
            speak('The meaning of the word is')
            print(str(text))
            speak(str(text))

    #Rolling a Dice
    elif 'roll a dice' in command:
        speak('Rolling a dice')
        number = random.randint(1,6)
        speak('The outcome of the dice is')
        speak(str(number))

    #Flipping a coin
    elif 'flip a coin' in command:
        speak('flipping a coin')
        flip=random.randint(1,2)
        if flip==1:
                speak("The outcome of the coin is: Heads")
        else:
                speak("The outcome of the coin is: Tails")

    #Random useless facts
    elif 'fact' in command:
        speak("\nHere is an interesting fact")
        facts=["The Earth’s Atmosphere Extends to a Distance of 10,000 km",
               "The Earth’s Molten Iron Core Creates a Magnetic Field",
               "A bolt of lightning contains enough energy to toast 100,000 slices of bread",
               "You can hear a blue whale’s heartbeat from two miles away",
               "The inventor of the frisbee was turned into a frisbee after he died",
               "Marie Curie’s notebooks are still radioactive",
               "The world’s largest pyramid isn’t in Egypt",
               "Coke saved one town from the Depression",
               "Dolphins have actual names",
               "Bottled water expiration dates are for the bottle, not the water",
               "The world’s most successful pirate was a woman",
               "Milk wagons gave us roadway lines",
               "The Aurora Borealis has a sister phenomenon in the southern hemisphere called the Aurora Australis"]
        
        def fact():
                select=random.choice(facts)
                speak(select)
                
        fact()

    #Random non-funny jokes
    elif 'joke' in command:
        speak("Here is a joke for you")
        jokes=["A guy shows up late for work. The boss yells, ‘You should’ve been here at 8.30!’ He replies. ‘Why? What happened at 8.30?’",
               "I forgot my cell phone when I went to the toilet yesterday. We have 245 tiles",
               "I’ve always thought my neighbors were quite nice people. But then they put a password on their Wi-Fi.",
               "My wife is a bit weird. She always starts her talking with “Michael, are you listening to me?”",
               "What if dogs fetch the ball back only because they think you really like throwing it?",
               "Level of cooking expertise: Using smoke alarm as timer."]
        
        def joke():
                select=random.choice(jokes)
                speak(select)
                
        joke()

    #Battery Status
    elif 'battery' in command:
        battery = psutil.sensors_battery()
        charger = battery.power_plugged
        percent = str(battery.percent)
        if charger==False:
                charger="Not Plugged In"
        else:
                charger="Plugged In"
        speak('The battery percentage is')
        speak(percent)
        speak('And the charger is')
        speak(charger)

    #Calendar/Holidays
    elif 'calendar' in command:
        speak("Would you like to see the calendar or the upcoming holidays?")
        primary = inapp()
        if 'calendar' in primary:
            speak('Please enter the details')
            year=int(input("Enter the year (yyyy):"))
            choice=input("Do you want to view the whole year or a specific month? (y/m):")
            if choice == 'y':
                    print("\n", calendar.calendar(year))
            elif choice == 'm':
                    month=int(input("Enter the month (mm):"))
                    print("\n", calendar.month(year,month))
            else:
                    print("Since no valid choices were made, here is the whole year's calendar")
                    print("\n", calendar.calendar(year))

        elif 'holiday' in primary:
            url = ('https://www.calendarlabs.com/holidays/india/')
            webbrowser.open(url)
            speak("Here is a uselful website for the same")
            
        else:
            speak("Since no valid selection was made, here is this year's calendar")
            current_year= datetime.now().year
            print("\n", calendar.calendar(current_year))

    #Holiday List
    elif 'holiday' in command:
        url = ('https://www.calendarlabs.com/holidays/india/')
        webbrowser.open(url)
        speak('Here are all the holidays in India')

    #Flight Status
    elif 'flight' in command:
        speak('Please input the flight number')
        flight=input("Enter the Flight Number:")
        url = ('https://www.google.com/search?q=' + 'Flight status of ' + flight)
        webbrowser.open(url)
        speak('Here is your flight information')

    #List Toolbar
    elif 'list' in command:
        m = open('Lists.txt','a')
        m.close()
        
        stack=[]
        speak("\Would you like to create, read or delete today's list (if any)?")
        choice = inapp()

        #Creating a list
        if 'create' in choice:
            
            speak('Okay, let us create a list. Please fill the details.')
            n=int(input("\nEnter the number of elements you want to put in your list:"))
            num = str(n)
            while n>0:
                    element=input("\nEnter the element:")
                    stack.append(element)
                    n=n-1
            speak('Okay, your list for the day is displayed')
            print(stack)
            with open('Lists.txt','a') as m:
                date=datetime.today().strftime("%d/%m/%Y")
                m.write('\n')
                m.write('{}'.format(date))
                m.write('\n')
                m.write(num)
                m.write('\n')
                for listitem in stack:
                        m.write('%s\n' % listitem)

            notification.notify(title = 'To Do List', message = 'New list is saved, complete your work :)', app_name = 'Cynthia', app_icon = 'icon.ico', timeout = 10)   

        #Reading a list
        elif 'read' in choice:
            speak('Here is your list for the day.')
            lists = open('Lists.txt','r+')
            lines = lists.readlines()
            today1 = datetime.today()
            today = today1.strftime("%d/%m/%Y")
            n = len(lines)
            i = 0
            f = 0
            while i<n:
                if today == lines[i].rstrip():
                    f = 1
                    s = lines[i+1].rstrip()
                    s1 = int(s)
                    p = i+s1
                    for j in range(i+2,p+2):
                        a = lines[j]
                        print(a)
                        speak(a)
                else:
                    pass
                i = i+1

            if f == 1:
                pass
            else:
                speak('You do not have any lists for today, enjoy')


        #Deleting a list
        elif 'delete' in choice:
            def replace_line(file_name, line_num, text):
                lines = open(file_name, 'r').readlines()
                lines[line_num] = text
                out = open(file_name, 'w')
                out.writelines(lines)
                out.close()
            
            lists = open('Lists.txt','r+')
            lines = lists.readlines()
            today1 = datetime.today()
            today = today1.strftime("%d/%m/%Y")
            n = len(lines)
            i=0
            f = 0
            while i<n:
                if today == lines[i].rstrip():
                    f = 1
                    s = lines[i+1].rstrip()
                    s1 = int(s)
                    p = i+s1
                    for j in range(i,p+2):
                        replace_line('Lists.txt',j, '\n')
                else:
                    pass
                i = i+1

            if f == 1:
                speak('Your list for today was deleted')
            else:
                speak('You did not have any lists for today, enjoy')
                
        else:
                speak('I could not understand, sorry')

    #Calculator app
    elif 'calculator' in command:
        os.startfile('calc.exe')

    #VIT Folder
    elif 'academic' in command:
        path = 'D:\Academics\VIT'
        os.startfile(path)

    #VIT Folder
    elif 'academics' in command:
        path = 'D:\Academics\VIT'
        os.startfile(path)

    #Downloads Folder
    elif 'download' in command:
        path = "C:\\Users\\Yashvardhan Gupta\\Downloads"
        os.startfile(path)

    #Source Files
    elif 'source' in command:
        os.startfile('D:\Programming\Cynthia')

    #Setting a Reminder
    elif 'reminder' in command:
        with open('reminder.txt','a') as m:
            speak('Please enter the details for the reminder')
            text = input("Enter the Body:")
            date = input("When do you want to be reminded: (dd/mm/yyyy)")
            m.write('\n')
            m.write(date)
            m.write('\n')
            m.write(text)
            notification.notify(title = 'Reminder', message = 'Reminder has been set', app_name = 'Cynthia', app_icon = 'icon.ico', timeout = 10)

    #Repeating the last command
    elif 'repeat' in command:
        playsound("command.mp3")

    #Auto-Notes Toolbar
    elif 'audio' in command:
        import time
        if os.path.exists('Records'):
            pass
        else:
            os.mkdir('Records')

        speak('Would you like to record, listen or delete a recorded audio?')
        option = inapp()

        #Recording an Audio Note
        if 'record' in option:
            speak('Okay, do you want to record for a specific time or auto detect?')
            sub = inapp()

            if 'auto' in sub:

                speak('Okay, auto detecting. Please Input the name of the file')
                name = input('Enter the name of the file:')

                if os.path.exists('Records\\'+name+'.wav'):
                    speak('The name already exists, please change the name')
                    speak('For future purposes, here are all the file names you already have')
                    audio = os.listdir('Records\\')
                    for i in audio:
                        print(i.replace('.wav',''))
                    main('audio')

                else: 
                    Threshold = 10
                    SHORT_NORMALIZE = (1.0/32768.0)
                    chunk = 1024
                    FORMAT = pyaudio.paInt16
                    CHANNELS = 1
                    RATE = 16000
                    swidth = 2
                    TIMEOUT_LENGTH = 5
                   
                    class Recorder:

                        @staticmethod
                        def rms(frame):
                            count = len(frame) / swidth
                            format = "%dh" % (count)
                            shorts = struct.unpack(format, frame)

                            sum_squares = 0.0
                            for sample in shorts:
                                n = sample * SHORT_NORMALIZE
                                sum_squares += n * n
                            rms = math.pow(sum_squares / count, 0.5)

                            return rms * 1000

                        def __init__(self):
                            self.p = pyaudio.PyAudio()
                            self.stream = self.p.open(format=FORMAT,
                                                      channels=CHANNELS,
                                                      rate=RATE,
                                                      input=True,
                                                      output=True,
                                                      frames_per_buffer=chunk)

                        def record(self):
                            speak('Recording.')
                            print('Recording.\nStart speaking please.')
                            rec = []
                            current = time.time()
                            end = time.time() + TIMEOUT_LENGTH

                            while current <= end:
                                data = self.stream.read(chunk)
                                if self.rms(data) >= Threshold: end = time.time() + TIMEOUT_LENGTH
                                current = time.time()
                                rec.append(data)
                            self.write(b''.join(rec))

                        def write(self, recording):
                            filename = os.path.join('Records' + "\\" + name + '.wav')
                            wf = wave.open(filename, 'wb')
                            wf.setnchannels(CHANNELS)
                            wf.setsampwidth(self.p.get_sample_size(FORMAT))
                            wf.setframerate(RATE)
                            wf.writeframes(recording)
                            wf.close()
                            speak('Recording has ended')
                            print('Written to file: ' , (name+'.wav'))

                    a = Recorder()
                    a.record()

            else:
                speak('Okay, Please enter the name of the file and then the time')
                name = input('Enter the name:')
                time = int(input('Enter the time (in seconds):'))
                speak('Recording Started')
                fs = 44100
                seconds = time
                myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
                sd.wait()
                f = ('Records\\'+name+'.wav')
                write(f, fs, myrecording)
                speak('Recording Ended')
                print('Written to file: ' , (name+'.wav'))

        #Listening to an audio note
        elif 'listen' in option:
            speak('The audios you have are')
            print('Audios:\n')
            audio = os.listdir('Records\\')
            for i in audio:
                j = i.replace('.wav','')
                print(j)
                speak(j)

            speak('Please the enter the name of the file you want to listen to:')
            name=input("\nThe file which do you want to listen to? ")
            if os.path.exists("Records\\"+name + '.wav'):
                speak('Playing the audio now:')
                print('Playing')
                playsound("Records\\"+name + '.wav')
            else:
                speak('I am sorry, the audio does not exist')

        #Deleting an audio note
        elif 'delete' in option:
            speak('The audios you have are:')
            print('Audios:\n')
            audio = os.listdir('Records\\')
            for i in audio:
                j = i.replace('.wav','')
                print(j)
                speak(j)

            speak('Please enter the name of the audio you want to delete')
            name=input("\nThe audio which do you want to delete? ")
            if os.path.exists("Records\\"+name + '.wav'):
                os.remove("Records\\"+name + '.wav')
            else:
                speak('I am sorry the audio does not exist')

        else:
            speak('Try Again')
            main('audio')

    #Changing mode (Text/Voice)
    elif 'change mode' in command:
        os.system('cls')
        import Main

    #Changing the Wake Up Keyword
    elif 'wake up' in command:

        def replace_line(file_name, line_num, text):
            lines = open(file_name, 'r').readlines()
            lines[line_num] = text
            out = open(file_name, 'w')
            out.writelines(lines)
            out.close()
                
        def wakeup():
            wake_up = open('wake_up.txt','r+')
            lines = wake_up.readlines(1)
            keyword = lines[0]
            print(keyword)
            speak(keyword)
                        
        speak('Your current wake up command is:')
        wakeup()
        speak('Would you like to change it? Reply in Yes or No')
        choice = inapp()

        if 'yes' in choice:
            speak('Okay, please input the new wake up command')
            word = input('New wake up command:')
            replace_line('wake_up.txt',0,word)
            speak('The wake up command has been changed to')
            wakeup()
        else:
            speak('Not changing the keyword, carry on')
            
    #Repating the Main Command
    else:
        speak("Try Again")
        myCommand()

#Infinte Loop
while True:
    wake()
