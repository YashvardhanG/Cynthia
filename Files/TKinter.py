import tkinter as tk
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

root= tk.Tk()
root.title('Cynthia')

canvas1 = tk.Canvas(root, width = 1580,  height = 760 , relief = 'raised', bg= 'Azure')
canvas1.pack()

label1 = tk.Label(root, text='Cynthia', bg='Azure', fg='Darkcyan')
label1.config(font=('Century Gothic', 20, 'bold'))
canvas1.create_window(760, 100, window=label1)

label2 = tk.Label(root, text='Some Instructions:', bg='Azure', fg='Darkcyan', relief= 'raised')
label2.config(font=('Century Gothic', 10, 'bold'))
canvas1.create_window(245, 170, window=label2)

label3 = tk.Label(root, text= 'Hello User, welcome to ""Cynthia"", your computer assistant!\nPlease make sure that you are connected with your internet because, many of the functions can only be performed with internet connectivity.\nIf you require some help with the program, type ""help"" as the command.\nTo see all the commands Cynthia has, type  in the number "2" as the command.\nIf you want to exit this application, just type ""exit"" as the command.\n',font=('Century Gothic', 10), bg='Azure', fg='Darkcyan', justify = 'left')
canvas1.create_window(760, 270, window=label3) 
                                             
label4 = tk.Label(root, text='Type a Command:', bg='Azure', fg='Darkcyan', relief= 'raised')
label4.config(font=('Century Gothic', 10, 'bold'))
canvas1.create_window(247, 350, window=label4)

entry1 = tk.Entry (root, width = 150) 
canvas1.create_window(760, 400, window=entry1)

label5 = tk.Label(root, text='Output:', bg='Azure', fg='Darkcyan', relief= 'raised')
label5.config(font=('Century Gothic', 10, 'bold'))
canvas1.create_window(200, 500, window=label5)

def enterc (event=None):
    text= entry1.get()

def enterf (event=None):

    command= entry1.get()
    entry1.delete(first=0, last='end')

    var = tk.StringVar()
    label6 = tk.Label(root, textvariable=var, font=('Century Gothic', 10), bg='Azure', fg='Darkcyan')
    canvas1.create_window(760,550, window=label6)

    if 'open google' in command:
        
        url = 'https://www.google.com/'
        webbrowser.open(url)
        
        var.set('Done, What else can I do for you?')

    elif 'open website' in command:
        
        reg_ex = re.search('open website (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain + '.com'
            webbrowser.open(url)
            
            var.set('That is done!')
        else:
            pass

    elif 'search' in command:
        
        reg_ex = re.search('search (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.google.com/search?q=' + domain
            webbrowser.open(url)
            
            var.set('Searching for it')
                
    elif 'how are you' in command:

        var.set('I am very good!')


    elif 'hello' in command:
        
        var.set("Hello, How are you?")

    elif 'www' in command:
        
        reg_ex = re.search('www (.*)', command)
        url = command
        webbrowser.open(url)
        
        var.set('That is being opened')

    elif 'news' in command:

        
        var.set('Select and then click the "Okay" Button')
        
        s = tk.OptionMenu(root, var, "Select", "International", "National")
        s.config(width=90, font=('Century Gothic', 10, 'bold'), bg = 'Teal' , fg= 'White')
        s.pack(side = 'bottom')
        canvas1.create_window(775,600, window=s)

        def callback(*args):
            label6.configure(text= var.get())

        var.trace("w", callback)


        def enterc():

            news = label6.cget("text")
            
            if news == "International":
                url = 'https://www.indiatoday.in/world'
                webbrowser.open(url)
                var.set("Opening International News")
                button2.destroy()
                s.destroy()
                label6.destroy()

            elif news == "National":
                url = 'https://in.reuters.com/'
                webbrowser.open(url)
                var.set("Opening National News")

                button2.destroy()
                s.destroy()
                label6.destroy()

            else:
                None

        button2 = tk.Button(text='Okay', command=enterc, bg='Teal', fg='White', font=('Century Gothic', 9, 'bold'), width= 30)
        canvas1.create_window(760, 650, window=button2)

        

    elif 'music' in command:
        
        var.set('Select and then click the "Okay" Button')
        
        s = tk.OptionMenu(root, var, "Select", "Hindi", "International")
        s.config(width=90, font=('Century Gothic', 10, 'bold'), bg = 'Teal' , fg= 'White')
        s.pack(side = 'bottom')
        canvas1.create_window(775,600, window=s)

        def callback(*args):
            label6.configure(text= var.get())

        var.trace("w", callback)

        def enterc():

            music = label6.cget("text")
            
            if music == "International":
                url = 'https://gaana.com/playlist/gaana-dj-gaana-international-top-50'
                webbrowser.open(url)
                
                var.set("Playing International Music")
                button2.destroy()
                s.destroy()
                label6.destroy()
                
            elif music == "Hindi":
                    url = 'https://gaana.com/playlist/gaana-dj-bollywood-top-50-1'
                    webbrowser.open(url)
        
                    var.set("Playing Hindi Music")
                    button2.destroy()
                    s.destroy()
                    label6.destroy()
                    
            else:
                   None

        button2 = tk.Button(text='Okay', command=enterc, bg='Teal', fg='White', font=('Century Gothic', 9, 'bold'), width= 30)
        canvas1.create_window(760, 650, window=button2)

    elif '1' == command:
        scrollbar = tk.Scrollbar(root)
        scrollbar.pack( side = "right", fill = 'y' )

        listbox = tk.Listbox(root)
        listbox.pack()

        list1= ("Cynthia is a python based computer assistant which will help you in various kinds of things and reduce your effort of opening and executing things.","From some basic functions like executing a countdown and telling about the weather, Cynthia can help you take down notes and read them too.","Cynthia  is an interactive assistant so asking some questions like (How are you), Cynthia will respond back to you.","To understand and know about the various commands that Cynthia has, you can type in the number '2' as your command.","Cynthia is developed by Yashvardhan Gupta, Spiral Cosmos.","Copyright 2020", '', 'Click on "Okay" button when done')

        for i in list1:
            listbox.insert('end',i)
            listbox.config(bg='Azure', fg='Darkcyan', width= 150, font=('Century Gothic', 10))
            canvas1.create_window(760, 650, window= listbox)

        listbox.config(yscrollcommand = scrollbar.set) 

        scrollbar.config( command = listbox.yview )

        def clear():
            listbox.destroy()
            button2.destroy()
            label6.destroy()

        button2 = tk.Button(text='Okay', command=clear, bg='Teal', fg='White', font=('Century Gothic', 9, 'bold'), width= 10)
        canvas1.create_window(1500, 740, window=button2)

    elif '2' == command:
        
        scrollbar = tk.Scrollbar(root)
        scrollbar.pack( side = "left", fill = 'y' )

        listbox = tk.Listbox(root)
        listbox.pack()
        
        list1=('We request you to please type in all the keywords starting with a small letter (eg: memo and not Memo, clock and not Clock)','Thank you for your cooperation','','*This list is scrollable, please use the down arrow key to go down*','Click on "Okay" button when done','','List of Commands:','','1.)To open any website on your computer, use "open website" and the website you want to open. (eg: open website youtube)','2.)To take down a memo, use "memo" as your command.','3.)To read out the written memo, use "read" and then type in the file you want to read.','4.)To know the weather of a place, use "weather"','5.)To search something on Google, use "search" followed by whatever you want to search.','6.)For countdown, use "timer" as your command.','7.)To open any website at all, you can directly type in the url starting with "www".','8.)To use the calculator, type in "calculator" as the command.','9.)To restart or shutdown your computer, enter "restart" or "shutdown" as your command.','10.)To translate any of your text, put "translator" as your command.','11.)To listen to fresh music, type "music" as your command.','12.)To read latest news, type "news" as your command.','13.)To open any desktop application, type in "application" as your command.','14.)To search and go to a specific path, enter "path" as your command.','15.)To view the clock, enter "clock" as your command.','16.)To search a word in the dictionary, search "dictionary" as your command.','17.)To roll a dice or flip a coin, put "roll" or "flip" as your command respectively.','18.)To set up a pop-up notification, use "notification" in your command.','19.)To check you battery status, use "battery" as your command.','20.)To get amused, use "joke" as your command.','21.)To learn something new, use "fact" as your command.','22.)To view the calendar, use "calendar" in your command.','23.)To check your flight status, use "flight" in your command.','24.)To add a new folder in your computer, use "folder" in your command.','25.)To make a To-Do-List, use "list" in your command.','26.)To check your details, use "detail" in your command','27.)To edit your current name, use "name" as the command.')                
 
        for i in list1:
            listbox.insert('end',i)
            listbox.config(bg='Azure', fg='Darkcyan', width= 150, font=('Century Gothic', 10))
            canvas1.create_window(760, 650, window= listbox)

        listbox.selection_set( first = 4 )
        listbox.config(yscrollcommand = scrollbar.set) 

        scrollbar.config( command = listbox.yview )

        def clear():
            listbox.destroy()
            button2.destroy()
            label6.destroy()

        button2 = tk.Button(text='Okay', command=clear, bg='Teal', fg='White', font=('Century Gothic', 9, 'bold'), width= 10)
        canvas1.create_window(1500, 740, window=button2)

    elif '3' == command:
        scrollbar = tk.Scrollbar(root)
        scrollbar.pack( side = "left", fill = 'y' )

        listbox = tk.Listbox(root)
        listbox.pack()
        
        list1=('We request you to please type in all the keywords starting with a small letter (eg: memo and not Memo, clock and not Clock)','Thank you for your cooperation','','*This list is scrollable, please use the down arrow key to go down*','Click on "Okay" button when done','Here are some sample commands which can be used in Cynthia:','','1.)open website youtube','2.)Take down a memo','3.)read a memo','4.)tell the weather','5.)search xyz','6.)start a timer','7.)www.facebook.com','8.)open calculator','9.)restart computer','10.)shutdown computer','11.)listen to music','12.)show the news','13.)open application','14.)open translator','15.)open path','16.)show clock','17.)roll a dice','18.)Flip a coin','19.)make a notification','20.)tell me a joke','21.)my battery status','22.)tell me an interesting fact','23.)show me the calendar','24.)check my flight status','25.)add a folder','26.)make a list','27.)show my details','28.)change my name','29.)open dictionary','30.)help me with cynthia','31.)exit cynthia')
                   
        for i in list1:
            listbox.insert('end',i)
            listbox.config(bg='Azure', fg='Darkcyan', width= 150, font=('Century Gothic', 10))
            canvas1.create_window(760, 650, window= listbox)

        listbox.config(yscrollcommand = scrollbar.set)
        listbox.selection_set( first = 4 )

        scrollbar.config( command = listbox.yview )

        def clear():
            listbox.destroy()
            button2.destroy()
            label6.destroy()

        button2 = tk.Button(text='Okay', command=clear, bg='Teal', fg='White', font=('Century Gothic', 9, 'bold'), width= 10)
        canvas1.create_window(1500, 740, window=button2)

    elif 'help' in command:

        var.set('What do you require Help in: \n Please type in (1/2/3) as the command and hit Enter \n\n1.)Basic Information \n2.)List of Commands \n3.)Example Commands')

    elif 'exit' in command:

        var.set('Are you sure?')
        
        s = tk.OptionMenu(root, var, "Select", "Yes", "No")
        s.config(width=90, font=('Century Gothic', 10, 'bold'), bg = 'Teal' , fg= 'White')
        s.pack(side = 'bottom')
        canvas1.create_window(775,600, window=s)

        def callback(*args):
            label6.configure(text= var.get())

        var.trace("w", callback)

        def enterc():

            choice = label6.cget("text")
            
            if choice == "Yes":
                
                var.set('Thank You!')
                button2.destroy()
                s.destroy()

                root.destroy()
                
            elif choice == "No":
                
                var.set("Continue enjoying the assistant")
                button2.destroy()
                s.destroy()
                    
            else:
                   None

        button2 = tk.Button(text='Okay', command=enterc, bg='Teal', fg='White', font=('Century Gothic', 9, 'bold'), width= 30)
        canvas1.create_window(760, 650, window=button2)

    elif 'timer' in command:

        var.set('Enter the time in seconds, and click Okay')

        var1 = tk.StringVar()
        label7 = tk.Label(root, textvariable=var1, font=('Century Gothic', 10), bg='Azure', fg='Darkcyan')
        canvas1.create_window(760,700, window=label7)

        var1.set('0')

        def enterc():

            entry=entry1.get()
            
            n=int(entry)
            s=0
            while s<=n:
                
                os.system('cls')
                time.sleep(1)
                s+=1
                l=str(s)
                var1.set(l)
                int(s)
                
            var.set("Time's Up!")

            label7.destroy()
            button2.destroy()
            
        button2 = tk.Button(text='Okay', command=enterc, bg='Teal', fg='White', font=('Century Gothic', 9, 'bold'), width= 30)
        canvas1.create_window(760, 650, window=button2)

    elif 'shutdown' in command:
        
        var.set("Are you sure you want to shutdown your computer?")
        
        s = tk.OptionMenu(root, var, "Select", "Yes", "No")
        s.config(width=90, font=('Century Gothic', 10, 'bold'), bg = 'Teal' , fg= 'White')
        s.pack(side = 'bottom')
        canvas1.create_window(775,600, window=s)

        def callback(*args):
            label6.configure(text= var.get())

        var.trace("w", callback)

        def enterc():

            choice = label6.cget("text")

            if choice == 'Yes':

                root.destroy()
                os.system("shutdown /s /t 1")  

            elif choice == 'No':
                var.set("Okay!")
                s.destroy()
                button2.destroy()
                label6.destroy()
                    
            else:
                None
                    

        button2 = tk.Button(text='Okay', command=enterc, bg='Teal', fg='White', font=('Century Gothic', 9, 'bold'), width= 30)
        canvas1.create_window(760, 650, window=button2)


    elif 'restart' in command:

        var.set("Are you sure you want to restart your computer?")
        
        s = tk.OptionMenu(root, var, "Select", "Yes", "No")
        s.config(width=90, font=('Century Gothic', 10, 'bold'), bg = 'Teal' , fg= 'White')
        s.pack(side = 'bottom')
        canvas1.create_window(775,600, window=s)

        def callback(*args):
            label6.configure(text= var.get())

        var.trace("w", callback)

        def enterc():

            choice = label6.cget("text")

            if choice == 'Yes':

                root.destroy()
                os.system("shutdown /r /t 1")  

            elif choice == 'No':
                var.set("Okay!")
                s.destroy()
                button2.destroy()
                label6.destroy()
                    
            else:
                None
                    

        button2 = tk.Button(text='Okay', command=enterc, bg='Teal', fg='White', font=('Century Gothic', 9, 'bold'), width= 30)
        canvas1.create_window(760, 650, window=button2)

    elif 'application' in command:
        var.set("To open any application on your computer just enter its name and click 'Okay' but, please make sure that you ensure the actual file name \nFor eg: To open google chrome, type in ""chrome"" and not ""google chrome"", otherwise the assistant will close itself")

        def app():

            app= entry1.get()
            os.startfile(app+'.exe')
            var.set("Okay!")

        button2 = tk.Button(text='Okay', command=app, bg='Teal', fg='White', font=('Century Gothic', 9, 'bold'), width= 30)
        canvas1.create_window(760, 650, window=button2)


    elif 'path' in command:

        var.set("Insert the path of the file/folder and click 'Okay'")

        def path():

            a= entry1.get()
            os.startfile(a)
            var.set("Opened")
            button2.destroy()
            entry1.delete(first = 0, last='end')

        button2 = tk.Button(text='Okay', command=path, bg='Teal', fg='White', font=('Century Gothic', 9, 'bold'), width= 30)
        canvas1.create_window(760, 650, window=button2)

    elif 'holiday' in command:
                                                                                                                                                    
        var.set("Here is a uselful website for the same")
        url = ('https://www.calendarlabs.com/holidays/india/')
        webbrowser.open(url)

    elif 'joke' in command:
        
        jokes=["A guy shows up late for work. The boss yells, ‘You should’ve been here at 8.30!’ He replies. ‘Why? What happened at 8.30?’",
               "I forgot my cell phone when I went to the toilet yesterday. We have 245 tiles",
               "I’ve always thought my neighbors were quite nice people. But then they put a password on their Wi-Fi.",
               "My wife is a bit weird. She always starts her talking with “Michael, are you listening to me?”",
               "What if dogs fetch the ball back only because they think you really like throwing it?",
               "Level of cooking expertise: Using smoke alarm as timer."]
        
        def joke():
                select=random.choice(jokes)
                var.set(select)
                
        joke()

    elif 'read' in command:

        var.set("Enter the name of the text file which you want to read, then click 'Okay'. \nEg:(C:/Desktop/memo), If it's in the same path, just type the name, ie. (memo).")

        def read():

            name=entry1.get()
            
            scrollbar = tk.Scrollbar(root)
            scrollbar.pack( side = "left", fill = 'y' )

            listbox = tk.Listbox(root)
            listbox.pack()

            m=open(name + '.txt','r')
            text=m.readlines()
                
            for i in text:
                listbox.insert('end',i)
                listbox.config(bg='Azure', fg='Darkcyan', width= 150, font=('Century Gothic', 10))
                canvas1.create_window(760, 650, window= listbox)
                
            listbox.config(yscrollcommand = scrollbar.set) 

            scrollbar.config( command = listbox.yview )

            m.close()

            def clear():
                listbox.destroy()
                button2.destroy()
                button3.destroy()
                label6.destroy()

            button3 = tk.Button(text='Clear', command=clear, bg='Teal', fg='White', font=('Century Gothic', 9, 'bold'), width= 10)
            canvas1.create_window(1500, 740, window=button3)
        

        button2 = tk.Button(text='Okay', command=read, bg='Teal', fg='White', font=('Century Gothic', 9, 'bold'), width= 10)
        canvas1.create_window(760, 650, window=button2)

        
                
    else:
        var.set("Since no valid commands were entered, Cynthia is searching the web for it. \nIf you require any help with this program like viewing the list of commands, please enter (help) as your command")
        url = ('https://www.google.com/search?q=' + command)
        webbrowser.open(url)


button1 = tk.Button(text='Enter', command=enterf, bg='Teal', fg='White', font=('Century Gothic', 9, 'bold'), width= 30)
canvas1.create_window(760, 450, window=button1)

root.bind('<Return>',enterf)
         
root.mainloop()
