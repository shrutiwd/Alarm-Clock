#Python program to set an alarm

#Importing required libraries
from datetime import *
import time,sys,winsound,pyttsx3

#Taking format input from user 
form= int(input("""Select 1 for: To enter in 12Hrs-Format
Select 2 for: To enter in 24Hrs-Format
>"""))
print(80*'=')

#Save date in day-month-year format
date=datetime.now().strftime("%d %b %Y")

class Alarm:

    '''A class to represent the working of an Alarm clock '''
    
    def __init__(self,h,m):
        
        '''Intializing instance variables '''

        self.h=h
        self.m=m

    def h12(self):
        """Allows user to enter in 12Hrs format of clock"""
        
        #to check if current time is equal to time entered by user
        while True:
            now= datetime.now().strftime('%I:%M %p')
            if now[:2]==("%02d"%h) and now[3:5]==("%02d"%m) and now[6:8]==am_pm:
                print('Your Message:',label)
                
                #text to speech when alarm goes off
                audio = pyttsx3.init()
                audio.say(f"It is {h} {m} {am_pm}")
                audio.runAndWait()
                
                #play sound for given time, if no loop is given it will play according to the music filelength
                for i in range(5):
                    winsound.PlaySound(ring,winsound.SND_ASYNC)
                    
                #Dismissing or Snoozing the alarm    
                while True:
                    a=int(input('''Press 1 for: Dismiss
Press 2 for: Snooze 10secs
>'''))
                    if a==1:
                        winsound.PlaySound(None,winsound.SND_PURGE)
                        sys.exit()

                    elif a==2:
                        winsound.PlaySound(None,winsound.SND_PURGE)
                        time.sleep(10)
                        winsound.PlaySound(ring,winsound.SND_ASYNC)
                    else:
                        print('Enter valid number!')
            else:
                time.sleep(10)


    def h24(self):
        """Allows user to enter in 24Hrs format of clock"""

        #to check if current time is equal to time entered by user
        while True:
            now= datetime.now().strftime('%H:%M')
            if now[:2]==("%02d"%h) and now[3:5]==("%02d"%m): 
                print('Your message:',label)
                
                audio = pyttsx3.init()
                audio.say(f"It is {h} {m} Hours")
                audio.runAndWait()
                
                for i in range(5):
                    winsound.PlaySound(ring,winsound.SND_ASYNC)
                
                #Dismissing or Snoozing the alarm    
                while True:
                    a=int(input('''Press 1 for: Dismiss
Press 2 for: Snooze 10 secs
>'''))
                    if a==1:
                        winsound.PlaySound(None,winsound.SND_PURGE)
                        sys.exit()

                    elif a==2:
                        winsound.PlaySound(None,winsound.SND_PURGE)
                        time.sleep(10)
                        winsound.PlaySound(ring,winsound.SND_ASYNC)
                    else:
                        print('Enter valid number!')
            else:
                time.sleep(10)

#Calling the function
#if user enters form=1, taking input in 12Hr format
if form==1:
    #Taking time inputs from the user 
    h,m= [int(x) for x in input('\t\tSet hour and minutes with colon:').split(':')]
    am_pm= input('\t\tAM or PM?:').upper()
    print(80*'=')

    #Taking display message from user
    label=input('\t\tAdd alarm message:')
    print(80*'=')

    #Taking ringtone from user
    ring= input('''\tAvailable ringtones:
                              1>fast.wav
                              2>heavy.wav
                              3>classic.wav
                              4>waves.wav
                         Choose ringtone:''')
    if ring == '1' or ring == 'fast.wav':
        ring = fast.wav
    elif ring == '2' or ring == 'heavy.wav':
        ring = 'heavy.wav'
    elif ring == '3' or ring == 'classic.wav':
        ring = 'classic.wav'
    elif ring == '4' or ring == 'waves.wav':
        ring = 'waves.wav'
    else:
        print('Invalid')
    print(80*'=')
    #Displaying the set alarm time and date, and saving the data in a file
    # will save the alarm history
    f=open('History.txt','a')
    x=(f'\t\tALARM SET AT {"%02d"%h}:{"%02d"%m} {am_pm} on {date}        ')
    print(x)

    #enter new line in file
    f.write('\n')
    f.write(x)
    f.close()
    print(80*'=')
    a=Alarm(h,m)
    a.h12()

#if user enters form=2, taking input in 24Hr format
elif form==2:
    #Taking time inputs from the user 
    h,m= [int(x) for x in input('\t\tSet hour and minutes with colon:').split(':')]
    print(80*'=')

    #Taking display message from user
    label=input('\t\tAdd alarm message:')
    print(80*'=')

    #Taking ringtone from user
    ring= input('''\tAvailable ringtones:
                              1>fast.wav
                              2>heavy.wav
                              3>classic.wav
                              4>waves.wav
                         Choose ringtone:''')
    if ring == '1' or ring == 'fast.wav':
        ring = fast.wav
    elif ring == '2' or ring == 'heavy.wav':
        ring = 'heavy.wav'
    elif ring == '3' or ring == 'classic.wav':
        ring = 'classic.wav'
    elif ring == '4' or ring == 'waves.wav':
        ring = 'waves.wav'
    else:
        print('Invalid')
    print(80*'=')
    #Displaying the set alarm time and date, and saving the data in a file
    #  will save the alarm history
    f=open('History.txt','a')
    x=(f'\t\tALARM SET AT {"%02d"%h}:{"%02d"%m} Hours on {date}        ')
    print(x)

    #enter new line in file
    f.write('\n')
    f.write(x)
    f.close()
    print(80*'=')
    a=Alarm(h,m)
    a.h24()
else:
    print('Invalid!!!')









