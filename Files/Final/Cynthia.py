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
import pyaudio
import struct
import wave
import sounddevice as sd
from scipy.io.wavfile import write
from playsound import playsound

print("Hello User, welcome to ""Cynthia"", your computer assistant!")
print("Please make sure that you are connected with your internet because, many of the functions can only be performed with internet connectivity.")
print("If you require some help with the program, type ""help"" as the command.")
print("To see all the commands Cynthia has, type  in the number '2' as the command.")
print("If you want to exit this application, just type ""exit"" as the command.\n")

#Name and Details Check
if os.path.exists('Name.txt'):
    name=open('Name.txt','r')
    your_name=name.read()
    name.close()
    print ("Welcome!",your_name)

else:
    your_name=input("Enter your name please:")
    name=open('Name.txt','w')
    name.write(your_name)
    name.close()
    details=open('Details.txt','w') 
    details.write('Name:')
    details.write(your_name)
    details.close()
    print("Welcome!", your_name)
    notification.notify(title = 'Cynthia', message = 'Welcome to Cynthia', app_name = 'Cynthia', app_icon = 'icon.ico', timeout = 10)

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

#Inapp Input
def myCommand():
        enter=input("Enter the text:")

#Main Input
def enter():
        a=input("\nPlease enter a command:")
        command = a.lower()
        return command
        
#Main Command
def assistant(command):
        
        name=open('Name.txt','r')
        your_name=name.read()
        name.close()

        #Google Facility
        if 'open google' in command:
            url = 'https://www.google.com/'
            webbrowser.open(url)
            print('Done',your_name,',What else can I do for you?')

        #Website Opener
        elif 'open website' in command:
            reg_ex = re.search('open website (.+)', command)
            if reg_ex:
                domain = reg_ex.group(1)
                url = 'https://www.' + domain + '.com'
                webbrowser.open(url)
                print('That is done,',your_name)
            else:
                pass

        #Search on Google
        elif 'search' in command:
            reg_ex = re.search('search (.+)', command)
            if reg_ex:
                domain = reg_ex.group(1)
                url = 'https://www.google.com/search?q=' + domain
                webbrowser.open(url)
                print('Searching for it',your_name)
                
        #How are you
        elif 'how are you' in command:
            print('I am very good!') 

        #Hello
        elif 'hello' in command:
                print("Hello, How are you?",your_name)

        #Domain opener with 'www'
        elif 'www' in command:
                reg_ex = re.search('www (.*)', command)
                url = command
                webbrowser.open(url)
                print('That is being opened',your_name)

        #News Reader
        elif 'news' in command:
                news=input("Do you want to see International or National News? (type i/n):")
                if news == "i":
                        url = 'https://www.indiatoday.in/world'
                        webbrowser.open(url)
                        print("Opening International News")
                elif news == "n":
                        url = 'https://in.reuters.com/'
                        webbrowser.open(url)
                        print("Opening National News")
                else:
                        print("Since a valid news type wasn't selected, here is some random news",your_name,"keep reading :)")
                        url = 'https://in.reuters.com/'
                        webbrowser.open(url) 

        #Music Player
        elif 'music' in command:
                music=input("Would you like to listen to International or Hindi music? (type i/h):")
                if music == "i":
                        url = 'https://gaana.com/playlist/gaana-dj-gaana-international-top-50'
                        webbrowser.open(url)
                        print("Playing International Music")
                elif music == "h":
                        url = 'https://gaana.com/playlist/gaana-dj-bollywood-top-50-1'
                        webbrowser.open(url)
                        print("Playing Hindi Music")
                else:
                        print("Since no valid selection was made, here is some random music you might like,",your_name,",keep listening :)")
                        url = 'https://gaana.com/playlist/gaana-dj-todays-top-5-international'
                        webbrowser.open(url)

        #Introduction
        elif '1' == command:
                print("\nCynthia is a python based computer assistant which will help you in various kinds of things and reduce your effort of opening and executing things. \nFrom some basic functions like executing a countdown and telling about the weather, Cynthia can help you take down notes and read them too. \nCynthia  is an interactive assistant so asking some questions like (How are you), Cynthia will respond back to you. \nTo understand and know about the various commands that Cynthia has, you can type in the number '2' as your command. \nStay Healthy!\nSpiral Cosmos, Copyright 2021\n")

        #List of all commands (Useless)
        elif '2' == command:
                print('\nWe request you to please type in all the keywords starting with a small letter (eg: memo and not Memo, clock and not Clock)\nThank you for your cooperation\n\nList of Commands:\n\n1.)To open any website on your computer, use "open website" and the website you want to open. (eg: open website youtube)\n2.)To take down a memo, use "memo" as your command.\n3.)To read out the written memo, use "read" and then type in the file you want to read. \n4.)To know the weather of a place, use "weather"\n5.)To search something on Google, use "search" followed by whatever you want to search.\n6.)For countdown, use "timer" as your command.\n7.)To open any website at all, you can directly type in the url starting with "www".\n8.)To use the calculator, type in "calculator" as the command.\n9.)To restart or shutdown your computer, enter "restart" or "shutdown" as your command.\n10.)To translate any of your text, put "translator" as your command.\n11.)To listen to fresh music, type "music" as your command.\n12.)To read latest news, type "news" as your command.\n13.)To open any desktop application, type in "application" as your command.\n14.)To search and go to a specific path, enter "path" as your command.\n15.)To view the clock, enter "clock" as your command.\n16.)To search a word in the dictionary, search "dictionary" as your command.\n17.)To roll a dice or flip a coin, put "roll" or "flip" as your command respectively.\n18.)To set up a pop-up notification, use "notification" in your command.\n19.)To check you battery status, use "battery" as your command.\n20.)To get amused, use "joke" as your command.\n21.)To learn something new, use "fact" as your command.\n22.)To view the calendar, use "calendar" in your command.\n23.)To check your flight status, use "flight" in your command.\n24.)To add a new folder in your computer, use "folder" in your command.\n25.)To make a To-Do-List, use "list" in your command.\n26.)To check your details, use "detail" in your command\n27.)To edit your current name, use "name" as the command.\n')                

        #List of sample commands (Useless)
        elif '3' == command:
                print("\nWe request you to please type in all the keywords starting with a small letter (eg: memo and not Memo, clock and not Clock)\nThank you for your cooperation\n\nHere are some sample commands which can be used in Cynthia:\n1.)open website youtube\n2.)Take down a memo\n3.)read a memo\n4.)tell the weather\n5.)search xyz\n6.)start a timer\n7.)www.facebook.com\n8.)open calculator\n9.)restart computer\n10.)shutdown computer\n11.)listen to music\n12.)show the news\n13.)open application\n14.)open translator\n15.)open path\n16.)show clock\n17.)roll a dice\n18.)Flip a coin\n19.)make a notification\n20.)tell me a joke\n21.)my battery status\n22.)tell me an interesting fact\n23.)show me the calendar\n24.)check my flight status\n25.)add a folder\n26.)make a list\n27.)show my details\n28.)change my name\n29.)open dictionary\n30.)help me with cynthia\n31.)exit cynthia")

        #Exit from the assistant
        elif 'exit' in command:
            sys.exit()

        #Help function
        elif 'help' in command:
                print("\nWhat do you require Help in:\nPlease type in (1/2/3)\n \n 1.)Basic Information\n 2.)List of Commands\n 3.)Example Commands\n")

       #Set a Timer        
        elif 'timer' in command:
                n=int(input("Enter the time (in Seconds):"))
                s=0
                while s<=n:
                    os.system('cls')
                    print (s, 'Seconds')
                    time.sleep(1)
                    s+=1
                print("Time's Up!")
                
        #Shutdown the device
        elif 'shutdown' in command:
                print("Are you sure you want to shutdown your computer? (y/n)")
                choice = input("Enter your choice:");
                if choice == 'y':
                        os.system("shutdown /s /t 1")

                elif choice == 'n':
                        print("Okay!")
                        
                else:
                        print("Wrong command entered")

        #Restart the device
        elif 'restart' in command:
                print("Are you sure you want to restart your computer? (y/n)")
                choice = input("Enter your choice:");
                if choice == 'y':
                        os.system("shutdown /r /t 1")
                elif choice == 'n':
                        print("Okay!")
                        
                else:
                        print("Wrong command entered")

        #Text Translator
        elif 'translator' in command:
                print("The list of available languages and their codes have been opened in your web browser, please put the codes accordingly")
                url = 'https://cloud.google.com/translate/docs/languages'
                webbrowser.open(url)
                text=input("Enter the text you want to translate:")
                lang=input("Enter the language you want to translate it into(Code):")
                transtext = Translator().translate(text, dest=lang).text
                print("The translation of the text ","'",text,"'"," in the language ","'",lang,"'"," is: ",transtext)     

        #Calculator App
        elif 'calculator' in command:
                os.startfile('calc.exe')
         
        #Memo Toolbar
        elif 'memo' in command:
            if not os.path.exists('Memos'):
                os.makedirs('Memos')
            else:
                pass

            option = input('Would you like to read, create or delete a memo:')

            #Reading a memo
            if 'read' in option:
                print('Okay, The memos you have are:\n')
                memos = os.listdir('Memos\\')
                for i in memos:
                    print(i.replace('.txt',''))
                name=input("\nThe file which you want to read:")
                if os.path.exists("Memos\\"+name + '.txt'):
                    m=open("Memos\\"+name + '.txt','r')
                    text=m.read()
                    print(text)
                    m.close()
                else:
                    print("File doesn't exist")

            #Creating a memo
            elif 'create' in option:
                print('Okay')
                name=input("Enter which file name you want it in:")
                
                if os.path.exists('Memos\\'+name+'.txt'):
                    print('The name already exists, please change the name')
                    print('For future purposes, here are all the file names you already have:')
                    memo = os.listdir('Memos\\')
                    for i in memo:
                        print(i.replace('.txt',''))
                    assistant('memo')

                else:
                    with open("Memos\\" + name + ".txt","a") as m:
                        text = input("Enter the Body:")
                        date=datetime.now().replace(second=0, microsecond=0)
                        m.write('\n')
                        m.write('{}'.format(date))
                        m.write('\n')
                        m.write(text)
                        notification.notify(title = 'Memo', message = 'A new memo has been saved', app_name = 'Cynthia', app_icon = 'icon.ico', timeout = 10)

            #Deleting a memo
            elif 'delete' in option:
                print('Okay, The memos you have are:\n')
                memos = os.listdir('Memos\\')
                for i in memos:
                    print(i)
                name = input('\nWhich one do you want to delete?')
                if os.path.exists("Memos\\"+name + '.txt'):
                    os.remove("Memos\\"+name + '.txt')
                else:
                    print("File doesn't exist")

            else:
                print('Invalid Command')
                
        #Open a specified path
        elif 'path' in command:
                a=input("Enter the path which you want to open:")
                os.startfile(a)
                print("Opened")

        #Current Datetime
        elif 'clock' in command:
                print("The time is (Hours/Min/Second): ", datetime.now().time())
                print("The date is (Year/Month/Date: ", datetime.now().date())
                print("The day is (0=Mon,1=Tues,..): ", datetime.now().weekday())

        #English Dictionary
        elif 'dictionary' in command:
                print("Welcome to the English Dictionary")
                a=input("Enter the word whose meaning you desire:")
                meaning=PyDictionary.meaning(a)
                print(meaning)

        #Rolling a Dice
        elif 'roll' in command:
                print("Welcome to roll a dice")
                a=input("Should I roll the dice? (y/n)")
                if a=='y':
                        selected=random.randint(1,6)
                        print("The dice has the outcome:",selected)
                else:
                        print("No problem.")

        #Flipping a Coin
        elif 'flip' in command:
                print("Welcome to flip a coin")
                a=input("Should I flip a coin? (y/n)")
                def flip():
                        flip=random.randint(1,2)
                        if flip==1:
                                print("The outcome of the coin is: Heads")
                        else:
                                print("The outcome of the coin is: Tails")

                if a=='y':
                        flip()

                else:
                        print("No problem.")

        #Random useless facts
        elif 'fact' in command:
                print("\nHere is an interesting fact",your_name,"!\n")
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
                        print(select)
                        
                fact()

        #Random non-funny jokes
        elif 'joke' in command:
                print("\nHere is a joke for you",your_name,"!\n")
                jokes=["A guy shows up late for work. The boss yells, ‘You should’ve been here at 8.30!’ He replies. ‘Why? What happened at 8.30?’",
                       "I forgot my cell phone when I went to the toilet yesterday. We have 245 tiles",
                       "I’ve always thought my neighbors were quite nice people. But then they put a password on their Wi-Fi.",
                       "My wife is a bit weird. She always starts her talking with “Michael, are you listening to me?”",
                       "What if dogs fetch the ball back only because they think you really like throwing it?",
                       "Level of cooking expertise: Using smoke alarm as timer."]
                
                def joke():
                        select=random.choice(jokes)
                        print(select)
                        
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
                print('Battery Percentage:',percent+'%')
                print('Charger:',charger)


        #Notification Creator
        elif 'notification' in command:
                title1=input("Enter the Title:")
                text=input("Enter the Text:")
                notification.notify(title = title1, message = text, app_name = 'Cynthia', app_icon = 'icon.ico', timeout = 10)

        #Calendar/Holidays
        elif 'calendar' in command:
                primary=input("Would you like to see the calendar or the upcoming holidays? (c/h):")
                if primary == 'c':
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
                elif primary == 'h':
                        command='holiday'
                        
                        assistant(command)
                else:
                        print("Since no valid selection was made, here is this year's calendar")
                        current_year= datetime.now().year
                        print("\n", calendar.calendar(current_year))

        #Holidays List
        elif 'holiday' in command:
                print("Here is a uselful website for the same")
                url = ('https://www.calendarlabs.com/holidays/india/')
                webbrowser.open(url)

        #Flight Status
        elif 'flight' in command:
                flight=input("Enter the Flight Number:")
                url = ('https://www.google.com/search?q=' + 'Flight status of ' + flight)
                webbrowser.open(url)
                print("Your flight information has been opened",your_name)

        #Creating a folder
        elif 'folder' in command:
                name=input("Enter the name of the folder:")
                path=input("Enter the path you want to make the folder:")
                cpath=(path + '/' + name)
                if not os.path.exists(cpath):
                    os.makedirs(cpath)
                    print("The new folder has been made")

                else:
                        print("The folder already exists")
                        notification.notify(title = 'Folder', message = 'Folder Already Exists', app_name = 'Cynthia', app_icon = 'icon.ico', timeout = 10)

        #List Toolbar
        elif 'list' in command:
                m = open('Lists.txt','a')
                m.close()
                
                stack=[]
                print("\nWelcome to your To-Do-List")
                choice= input("\nWhat would you like to do?(1/2/3)\n1.)Make a list\n2.)View your lists\n3.)Delete today's list(if any)\n\nEnter:")

                #Creating a list
                if choice == '1':
                        n=int(input("\nEnter the number of elements you want to put in your list:"))
                        num = str(n)
                        while n>0:
                                element=input("\nEnter the element:")
                                stack.append(element)
                                n=n-1
                        print("\nYour list is:",stack)
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
                elif choice == '2':
                    print('Here is your list for the day.')
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
                        else:
                            pass
                        i = i+1

                    if f == 1:
                        pass
                    else:
                        print('You do not have any lists for today, enjoy')

                #Delete today's list
                elif choice == '3':
                    def replace_line(file_name, line_num, text):
                        lines = open(file_name, 'r').readlines()
                        lines[line_num] = text
                        out = open(file_name, 'w')
                        out.writelines(lines)
                        out.close()

                    print('\nOkay')
                    lists = open('Lists.txt','r+')
                    lines = lists.readlines()
                    today1 = datetime.today()
                    today = today1.strftime("%d/%m/%Y")
                    n = len(lines)
                    i=0
                    while i<n:
                        if today == lines[i].rstrip():
                            s = lines[i+1].rstrip()
                            s1 = int(s)
                            p = i+s1
                            for j in range(i,p+2):
                                replace_line('Lists.txt',j, '\n')
                        else:
                            pass
                        i = i+1
                    
                else:
                    print("Select a valid choice")


        #Name Changer
        elif 'name' in command:
            def replace_line(file_name, line_num, text):
                lines = open(file_name, 'r').readlines()
                lines[line_num] = text
                out = open(file_name, 'w')
                out.writelines(lines)
                out.close()
                
            name=open('Name.txt','w')
            your_name=input("Enter your correct name / edited name:")
            name.write(your_name)
            name.close()
            print("Okay, your name has been corrected -",your_name)

            detail = ('Name:'+your_name+'\n')
            replace_line('Details.txt',0,detail)

        #All Details
        elif 'detail' in command:
                print("Do you want to view your current details or add another one? (cd/ad):")

        #Add a detail
        elif command == 'ad':
                title=input("Enter the name of the Detail:")
                text=input("Enter the detail associated with it:")
                details=open('Details.txt','a')
                details.write('\n')
                details.write(title)
                details.write(':')
                details.write(text)

        #Delete a detail
        elif command == 'cd':
                details=open('Details.txt','r')
                text=details.read()
                print(text)
                details.close()

        #VIT Folder
        elif command == 'vit':
            path = 'D:\Academics\VIT'
            os.startfile(path)

        #Downloads Folder
        elif command == 'dl':
            path = "C:\\Users\\Yashvardhan Gupta\\Downloads"
            os.startfile(path)

        #Calculator App (Again)
        elif command == 'calc':
            os.startfile('calc.exe')

        #Source Files
        elif command == 'src':
            os.startfile('D:\Programming\Cynthia')

        #Setting a Reminder
        elif 'reminder' in command:
            with open('reminder.txt','a') as m:
                text = input("Enter the Body:")
                date = input("When do you want to be reminded:")
                m.write('\n')
                m.write(date)
                m.write('\n')
                m.write(text)
                notification.notify(title = 'Reminder', message = 'Reminder has been set', app_name = 'Cynthia', app_icon = 'icon.ico', timeout = 10)

        #Audio Notes Toolbar
        elif 'audio' in command:
            if os.path.exists('Records'):
                pass
            else:
                os.mkdir('Records')

            option = input('Would you like to record, listen or delete a recorded audio? ')

            #Recording an audio
            if 'record' in option:
                sub = input('Okay, Specific time or auto detect?')

                if 'auto' in sub:
                    import time
                    name = input('Enter the name of the file:')
                    
                    if os.path.exists('Records\\'+name+'.wav'):
                        print('The name already exists, please change the name')
                        print('For future purposes, here are all the file names you already have:')
                        audio = os.listdir('Records\\')
                        for i in audio:
                            print(i.replace('.wav',''))
                        assistant('audio')
                        
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
                                print('Recording has ended')
                                print('Written to file: ' , (name+'.wav'))

                        a = Recorder()
                        a.record()

                else:
                    name = input('Enter the name:')
                    time = int(input('Enter the time (in seconds):'))
                    print('Recording Started')
                    fs = 44100
                    seconds = time
                    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
                    sd.wait()
                    f = ('Records\\'+name+'.wav')
                    write(f, fs, myrecording)
                    print('Recording Ended')

            #Listening to an audio
            elif 'listen' in option:
                print('The audios you have are')
                audio = os.listdir('Records\\')
                for i in audio:
                    print(i.replace('.wav',''))
                name=input("\nThe file which do you want to listen to? ")
                if os.path.exists("Records\\"+name + '.wav'):
                    print('Playing')
                    playsound("Records\\"+name + '.wav')
                else:
                    print("Audio doesn't exist")

            #Deleting an audio
            elif 'delete' in option:
                print('The audios you have are:\n')
                audio = os.listdir('Records\\')
                for i in audio:
                    print(i.replace('.wav',''))
                name=input("\nThe audio which do you want to delete? ")
                if os.path.exists("Records\\"+name + '.wav'):
                    os.remove("Records\\"+name + '.wav')
                else:
                    print("File doesn't exist")

            else:
                print('Try again')

        #Changing mode (Text/Voice)
        elif 'change mode' in command:
            os.system('cls')
            import Main
                        
        #Google Search not found command
        else:
                print("Since no valid commands were entered, Cynthia is searching the web for it")
                url = ('https://www.google.com/search?q=' + command)
                webbrowser.open(url)
                print("If you require any help with this program like viewing the list of commands, please enter (help) as your command :)")
                        
#Infinte Loop
while True:
    assistant(enter())
