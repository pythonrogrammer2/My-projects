from cgitb import lookup
import pyautogui
import speech_recognition as sr
import pyttsx3 
import webbrowser
import time
import subprocess
import os
import smtplib
from email.message import EmailMessage

listener= sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()
def sayLine(input):
    print(input)
    talk(input)
talk("How can I help you")

print("Check")
def take_command():
    command=""
    while("jarvis" not in command):
        try:
            with sr.Microphone() as source:
                print("Listening...")
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command=command.lower()
                
            if "jarvis" in command:     
                com1,com2=command.split("jarvis")
                command=com2
                if("secret timer" not in command):
                    print(command)
                return command
        except:
            pass
def secondary_command():
    command=""
    while(command==""):
        try:
            with sr.Microphone() as source:
                print("Listening...")
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command=command.lower()
        except:
            pass
        print(command)
        return command
    
def end_program():
    pointOne=0
    pointTwo=0
    while(pointOne != 1 or pointTwo != 1):
        try:
            with sr.Microphone() as source:
                print("Listening...")
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command=command.lower()
                
            
        except:
            pass
        if("no" in command):
            print(command)
            return command
        if("yes" in command):
            print(command)
            return command

    
    
def run_jarvis():
    sleepTime=0.33
    volume=engine.getProperty('volume')
    print(volume)
    command=take_command() 
    #beginning of the google section
    #opens the google homepage
    if("open google" in command):
        print("Opening google")
        talk("Opening google")
        time.sleep(sleepTime)
        webbrowser.open_new_tab("https://www.google.com/")
    #searches for something on google(keywords: "open", "on google")
    elif("open" and "on google" in command):
        command=command.replace("on google", "")
        command=command.replace("google", "")
        command=command.replace("open", "")
        command=command.replace("lookup", "")
        command=command.replace("look up", "")
        url="https://www.google.com/search?q=" + command + "&sxsrf=ALiCzsbeeemLb66i278-RLbeOtRWtZzYqg%3A1652566463619&source=hp&ei=vymAYqDFIuOgkPIPvdSbsAY&iflsig=AJiK0e8AAAAAYoA3z6lMO2kpfkK0BBM5bq6W6SAZJvfK&ved=0ahUKEwjgoJ3ogeD3AhVjEEQIHT3qBmYQ4dUDCAk&uact=5&oq=potato&gs_lcp=Cgdnd3Mtd2l6EAMyEQguEIAEELEDEIMBEMcBEK8BMgsIABCABBCxAxCDATIICC4QgAQQsQMyDgguEIAEELEDEIMBENQCMgsILhCABBCxAxCDATIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQMyCAgAEIAEELEDOgQIIxAnOhEILhCABBCxAxCDARDHARCjAjoOCC4QgAQQsQMQxwEQowI6BQgAEIAEOgsILhCxAxCDARDUAjoOCC4QgAQQsQMQxwEQ0QM6BQguEIAEOgsILhCABBDHARCvAVAAWIYGYLUIaABwAHgAgAFniAGvBJIBAzUuMZgBAKABAQ&sclient=gws-wiz"
        print(command)
        print("Opening google")
        talk("Opening google")
        time.sleep(sleepTime)
        webbrowser.open_new_tab(url)
    #searches for something on google(keywords: "lookup", "on google")
    elif("lookup" and "on google" in command):
        command=command.replace("on google", "")    
        command=command.replace("google", "")
        command.command.replace("open", "")
        command=command.replace("lookup", "")
        command=command.replace("look up", "")
        url="https://www.google.com/search?q=" + command + "&sxsrf=ALiCzsbeeemLb66i278-RLbeOtRWtZzYqg%3A1652566463619&source=hp&ei=vymAYqDFIuOgkPIPvdSbsAY&iflsig=AJiK0e8AAAAAYoA3z6lMO2kpfkK0BBM5bq6W6SAZJvfK&ved=0ahUKEwjgoJ3ogeD3AhVjEEQIHT3qBmYQ4dUDCAk&uact=5&oq=potato&gs_lcp=Cgdnd3Mtd2l6EAMyEQguEIAEELEDEIMBEMcBEK8BMgsIABCABBCxAxCDATIICC4QgAQQsQMyDgguEIAEELEDEIMBENQCMgsILhCABBCxAxCDATIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQMyCAgAEIAEELEDOgQIIxAnOhEILhCABBCxAxCDARDHARCjAjoOCC4QgAQQsQMQxwEQowI6BQgAEIAEOgsILhCxAxCDARDUAjoOCC4QgAQQsQMQxwEQ0QM6BQguEIAEOgsILhCABBDHARCvAVAAWIYGYLUIaABwAHgAgAFniAGvBJIBAzUuMZgBAKABAQ&sclient=gws-wiz"
        print(command)
        print("Opening google")
        talk("Opening google")
        time.sleep(sleepTime)
        webbrowser.open_new_tab(url)
    #searches for something on google(keywords: "look up", "on google")
    elif("look up" and "on google" in command):
        command=command.replace("on google", "")
        command=command.replace("google", "")
        command=command.replace("open", "")
        command=command.replace("lookup", "")
        command=command.replace("look up", "")
        url="https://www.google.com/search?q=" + command + "&sxsrf=ALiCzsbeeemLb66i278-RLbeOtRWtZzYqg%3A1652566463619&source=hp&ei=vymAYqDFIuOgkPIPvdSbsAY&iflsig=AJiK0e8AAAAAYoA3z6lMO2kpfkK0BBM5bq6W6SAZJvfK&ved=0ahUKEwjgoJ3ogeD3AhVjEEQIHT3qBmYQ4dUDCAk&uact=5&oq=potato&gs_lcp=Cgdnd3Mtd2l6EAMyEQguEIAEELEDEIMBEMcBEK8BMgsIABCABBCxAxCDATIICC4QgAQQsQMyDgguEIAEELEDEIMBENQCMgsILhCABBCxAxCDATIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQMyCAgAEIAEELEDOgQIIxAnOhEILhCABBCxAxCDARDHARCjAjoOCC4QgAQQsQMQxwEQowI6BQgAEIAEOgsILhCxAxCDARDUAjoOCC4QgAQQsQMQxwEQ0QM6BQguEIAEOgsILhCABBDHARCvAVAAWIYGYLUIaABwAHgAgAFniAGvBJIBAzUuMZgBAKABAQ&sclient=gws-wiz"
        print(command)
        print("Opening google")
        talk("Opening google")
        time.sleep(sleepTime)
        webbrowser.open_new_tab(url)
    #searches for something on google(keywords: "google")
    elif("google" in command):
        command=command.replace("on google", "")
        command=command.replace("google", "")
        command=command.replace("open", "")
        command=command.replace("lookup", "")
        command=command.replace("look up", "")
        url="https://www.google.com/search?q=" + command + "&sxsrf=ALiCzsbeeemLb66i278-RLbeOtRWtZzYqg%3A1652566463619&source=hp&ei=vymAYqDFIuOgkPIPvdSbsAY&iflsig=AJiK0e8AAAAAYoA3z6lMO2kpfkK0BBM5bq6W6SAZJvfK&ved=0ahUKEwjgoJ3ogeD3AhVjEEQIHT3qBmYQ4dUDCAk&uact=5&oq=potato&gs_lcp=Cgdnd3Mtd2l6EAMyEQguEIAEELEDEIMBEMcBEK8BMgsIABCABBCxAxCDATIICC4QgAQQsQMyDgguEIAEELEDEIMBENQCMgsILhCABBCxAxCDATIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQMyCAgAEIAEELEDOgQIIxAnOhEILhCABBCxAxCDARDHARCjAjoOCC4QgAQQsQMQxwEQowI6BQgAEIAEOgsILhCxAxCDARDUAjoOCC4QgAQQsQMQxwEQ0QM6BQguEIAEOgsILhCABBDHARCvAVAAWIYGYLUIaABwAHgAgAFniAGvBJIBAzUuMZgBAKABAQ&sclient=gws-wiz"
        print(command)
        print("Opening google")
        talk("Opening google")
        time.sleep(sleepTime)
        webbrowser.open_new_tab(url)
    #end of the google section

    #beginning of the youtube section
    #opens my youtube homepage
    elif("open youtube" in command):
        print("Opening youtube")
        talk("Opening youtube")
        time.sleep(sleepTime)
        webbrowser.open_new_tab("https://www.youtube.com/")
    #searches for something on youtube(keywords: "open", "on youtube")
    elif("open" and "on youtube" in command):
        command=command.replace("look up", "")
        command=command.replace("lookup", "")
        command=command.replace("open", "")
        command=command.replace("on youtube", "")
        url="https://www.youtube.com/results?search_query=" + command
        print(url)
        print("Opening " + command + " on youtube")
        talk("Opening " + command + " on youtube")
        time.sleep(sleepTime)
        webbrowser.open_new_tab(url)
    #searches for something on youtube(keywords: "lookup", "on youtube")
    elif("lookup" and "on youtube" in command):
        command=command.replace("look up", "")
        command=command.replace("lookup", "")
        command=command.replace("open", "")
        command=command.replace("on youtube", "")
        url="https://www.youtube.com/results?search_query=" + command
        print(url)
        print("Opening " + command + " on youtube")
        talk("Opening " + command + " on youtube")
        time.sleep(sleepTime)
        webbrowser.open_new_tab(url)
    #searches for something on youtube(keywords: "look up", "on youtube")
    elif("look up" and "on youtube" in command):
        command=command.replace("look up", "")
        command=command.replace("lookup", "")
        command=command.replace("open", "")
        command=command.replace("on youtube", "")
        url="https://www.youtube.com/results?search_query=" + command
        print(url)
        print("Opening " + command + " on youtube")
        talk("Opening " + command + " on youtube")
        time.sleep(sleepTime)
        webbrowser.open_new_tab(url)
    #end of the youtube section

    #beginning of the gmail section
    #opens my gmail
    elif("open email" in command):
        print("Opening gmail")
        talk("Opening gmail")
        time.sleep(sleepTime)
        webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#inbox")
    elif("open emails" in command):
        print("Opening gmail")
        talk("Opening gmail")
        time.sleep(sleepTime)
        webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#inbox")
    elif("open gmail" in command):
        print("Opening gmail")
        talk("Opening gmail")
        time.sleep(sleepTime)
        webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#inbox")
    elif("open gmails" in command):
        print("Opening gmail")
        talk("Opening gmail")
        time.sleep(sleepTime)
        webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#inbox")
    #end of the gmail section
    #beginning of the drop my needle section
    elif("drop my needle" in command):
        time.sleep(sleepTime)
        webbrowser.open_new_tab("https://www.youtube.com/watch?v=Ry2bSgai62M")
    #end of the drop my needle section
    #beginning of connor's b-day celebration section
    elif("has something to say" in command):
        print("Happy Birthday Connor!")
        talk("Happy Birthday Connor!")
    #end of the connor's b-day celebration section
    #beginning of the closing section
    elif("i'm done" in command):
        print("Very well")
        talk("Very well")
        return "i'm done"
    #beginning of timer section
    #beginning of the first timer section
    elif("timer 1" in command):
        startMin=60
        startSec=0
        while(startMin != 0 or startSec != 0):
            time.sleep(1)
            if(startSec==0):
                startMin-=1
                startSec=59
            else:
                startSec-=1
            print(str(startMin) + ":" + str(startSec))
        talk("Sir, your first timer is up")
    #end of the first timer section
    #beginning of second timer section
    elif("timer to" in command):
        startMin=15
        startSec=0
        while(startMin != 0 or startSec != 0):
            time.sleep(1)
            if(startSec==0):
                startMin-=1
                startSec=59
            else:
                startSec-=1
            print(str(startMin) + ":" + str(startSec))
        talk("Sir, your second timer is up")
    elif("timer 2" in command):
        startMin=15
        startSec=0
        while(startMin != 0 or startSec != 0):
            time.sleep(1)
            if(startSec==0):
                startMin-=1
                startSec=59
            else:
                startSec-=1
            print(str(startMin) + ":" + str(startSec))
        talk("Sir, your second timer is up")
    elif("second timer" in command):
        startMin=15
        startSec=0
        while(startMin != 0 or startSec != 0):
            time.sleep(1)
            if(startSec==0):
                startMin-=1
                startSec=59
            else:
                startSec-=1
            print(str(startMin) + ":" + str(startSec))
        talk("Sir, your second timer is up")
    #end of second timer section
    elif("secret timer" in command):
        print(" set first timer")
        startMin=30
        startSec=0
        print("understood")
        talk("understood")
        while(startMin != 0 or startSec != 0):
            time.sleep(1)
            if(startSec==0):
                startMin-=1
                startSec=59
            else:
                startSec-=1
            print(str(startMin) + ":" + str(startSec))
        talk("Sir, your first timer is up")
    #end of timer section
    #beginning of the special section
    elif("perfectly imperfect" in command):
        url="https://www.youtube.com/playlist?list=PLL3CDR-N_kZJgcw75RveajUd65fMf6Y9r&jct=9153ERfo5c_V0MHSSL9wA1v87khRIw"
        time.sleep(sleepTime)
        webbrowser.open_new_tab(url)
    #end of the special section
    #beginning of the open app section
    #beginning of the open discord section
    elif("open discord" in command):
        print("Yes sir")
        talk("Yes sir")
        os.startfile("C:\\Users\\Owner\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord")
    #end of the open discord section
    #end of the open app section
    #beginning of the test section
    elif("test" in command):
        command=command.replace("test", "")
        print(command)
    #end of the test section
    #Beginning of my Playlist section
    #first option
    elif("my playlist" in command):
        url="https://www.youtube.com/watch?v=&list=RDMM&start_radio=1"
        time.sleep(sleepTime)
        webbrowser.open_new_tab(url)
        
    #second option
    elif("my mix" in command):
        url="https://www.youtube.com/watch?v=&list=RDMM&start_radio=1"
        time.sleep(sleepTime)
        webbrowser.open_new_tab(url)
    #end of my playlist section
    #beginning of email notification section
    elif(" an email" in command):
        sayLine("Understood")
        time.sleep(sleepTime)
        sayLine("what is the subject?")
        subject=secondary_command()
        sayLine("What will the content be?")
        body=secondary_command()
        body=body.replace("brayden", "braedon")
        body=body.replace("braden", "braedon")
        sayLine("Would you like to send this email?")
        sendEmail=end_program()
        while(sendEmail=="no"):
            sayLine("Is there something else you'd like to add?")
            add=end_program()
            if(add=="yes"):
                sayLine("What else would you like to add?")
                newBody= " " + secondary_command()
                body+=newBody
                body=body.replace("brayden", "braedon")
                body=body.replace("braden", "braedon")
            else:
                sayLine("Would you like to cancel this email?")
                cancelEmail=end_program()
                if(cancelEmail=="yes"):
                    sendEmail="yes"
        if(sendEmail == "yes"):
            email_alert(subject,body)
    elif(" and email" in command):
        sayLine("Understood")
        time.sleep(sleepTime)
        sayLine("what is the subject?")
        subject=secondary_command()
        sayLine("What will the content be?")
        body=secondary_command()
        body=body.replace("brayden", "braedon")
        body=body.replace("braden", "braedon")
        sayLine("Would you like to send this email?")
        sendEmail=end_program()
        while(sendEmail=="no"):
            sayLine("Is there something else you'd like to add?")
            add=end_program()
            if(add=="yes"):
                sayLine("What else would you like to add?")
                newBody= " " + secondary_command()
                body+=newBody
                body=body.replace("brayden", "braedon")
                body=body.replace("braden", "braedon")
            else:
                sayLine("Would you like to cancel this email?")
                cancelEmail=end_program()
                if(cancelEmail=="yes"):
                    sendEmail="yes"
        if(sendEmail == "yes"):
            email_alert(subject,body)
    #end of email section
    #beginning of text section
    elif(" a text" in command):
        sayLine("Understood")
        time.sleep(sleepTime)
        sayLine("What will the content be?")
        textContent=secondary_command()
        textContent=textContent.replace("brayden", "braedon")
        textContent=textContent.replace("braden", "braedon")
        sayLine("Would you like to send this text?")
        sendText=end_program()
        while(sendText=="no"):
            sayLine("Is there something else you'd like to add?")
            add=end_program()
            if(add=="yes"):
                sayLine("What else would you like to add?")
                newBody= " " + secondary_command()
                textContent+=newBody
                textContent=textContent.replace("brayden", "braedon")
                textContent=textContent.replace("braden", "braedon")
            else:
                sayLine("Would you like to cancel this email?")
                cancelText=end_program()
                if(cancelText=="yes"):
                    sendText="yes"
        if(sendText == "yes"):
            text_alert(textContent)




#beginning of repeat section
continueCheck=run_jarvis()
if(continueCheck != "i'm done"):
    print("Anything else?")
    talk("Anything else?")
    command=end_program()
    while(command=="yes"):
        print("What else can I do for you?")
        talk("What else can I do for you?")
        run_jarvis()
        print("Anything else?")
        talk("Anything else?")
        command=end_program()
