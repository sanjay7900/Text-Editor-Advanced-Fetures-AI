import tkinter as tk
import datetime
from tkinter import ttk
import sqlite3
from gtts import gTTS
import pygame
import requests
import json

con=sqlite3.connect("data.db")
cur = con.cursor()

win=tk.Tk()
win.minsize(1300,2000)
#m=tk.menu()

win.title('Reminder Bday App')
#win.caption('sanajy')

#This is heading


caption=ttk.Label(win, text='Add New Bday',font=("Arial Bold", 50))
caption.grid(row=0,column=0,columnspan=10)



year=ttk.Label(win,text="Year",font=("Arial Bold", 24))
year.grid(row=1,column=0,columnspan=1)

year=tk.StringVar()
year_enter=ttk.Entry(win,width=20,textvariable=year,font=("Arial Bold", 18))
year_enter.grid(row=1,column=1)



mon=ttk.Label(win,text="Month",font=("Arial Bold", 24))
mon.grid(row=2,column=0,columnspan=1)

month=tk.StringVar()
month_enter=ttk.Combobox(win,width=20,textvariable=month,state='readonly',font=("Arial Bold", 18))
month_enter['values'] = ('1','2','3','4','5','6','7','8','9','10','11','12')
month_enter.grid(row=2,column=1)



dat=ttk.Label(win,text="Date",font=("Arial Bold", 24))
dat.grid(row=3,column=0,columnspan=1)

date=tk.StringVar()
date_enter=ttk.Combobox(win,width=20,textvariable=date,state='readonly',font=("Arial Bold", 18))
date_enter['values'] = ('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31')
date_enter.grid(row=3,column=1)




bday=ttk.Label(win,text="Name",font=("Arial Bold", 24))
bday.grid(row=4,column=0,columnspan=1)

bday=tk.StringVar()
bday_enter=ttk.Entry(win,width=20,textvariable=bday,font=("Arial Bold", 18))
bday_enter.grid(row=4,column=1)

# this is function  for insert the data  on click add buttton




def action():
    
    #q="""CREATE TABLE bday2(id int,date int, month int, year int,b_name char)"""
    #cur.execute(q)
    l=9
    d=date.get()
    y=year.get()
    m=month.get()
    name=bday.get()
    cur.execute('INSERT INTO bday2(id,date,month,year,b_name)VALUES(?,?,?,?,?)',(l,d,m,y,name))
    print(y)
    con.commit()
    con.close()


    
btn=tk.Button(win,text='ADD',width=40,command=action)
btn.grid(row=5,column=0,columnspan=2)
check=ttk.Label(win,text="Check ToDay's bIRTHday",font=("Arial Bold", 50))
check.grid(row=6,column=0,columnspan=10)


#this function for sound


def sound():
    #i=gTTS.init()
    pygame.mixer.init()
    td=datetime.date.today()
    m=td.month
    d=td.day
    cur.execute('SELECT b_name FROM bday2 WHERE date=? AND month=?',(d,m))
    
    r=cur.fetchall()
    print(r)
    unit=0
    rl=1
    l=['1','2','3','4','5','6']
    for l in r:
        for j in l:
            print(j)
            
            t=j
            unit=unit+1
            
        
                
            
            i=gTTS("today's "+t+" is birthday")
            i.save("ii.mp3")
            rl=0
        
            pygame.mixer.music.load('ii.mp3')
            pygame.mixer.music.play()
      #  print(l)

      
btn2=tk.Button(win,text='Check',width=40,command=sound)
btn2.grid(row=7,column=0,columnspan=2)

#this function for send the message 



def send():
    
    
    td=datetime.date.today()
    m=td.month
    d=td.day
    cur.execute('SELECT b_name FROM bday2 WHERE date=? AND month=?',(d,m))
    
    r=cur.fetchone()
    print(r)
    unit=0
    t=""
    l=['1','2','3','4','5','6']
    for l in r:
        #for j in l:

        print(l)
        t=l
        unit=unit+1
            
    h='HAPPY BIRTHDAY @@@@@'
    wish=h+t
    URL = 'https://www.sms4india.com/api/v1/sendCampaign'

#  get request
    def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
        
        req_params = {
            'apikey':apiKey,
            'secret':secretKey,
            'usetype':useType,
            'phone': phoneNo,
            'message':textMessage,
            'senderid':senderId
            }
        return requests.post(reqUrl, req_params)

# get response
    api='FSHH23L7AC4039ABOZRETLADT62CB9B8'
    secret='HOJOHH9BHNUU3ORN'
#prod
    response = sendPostRequest(URL, api, secret, 'stage', '8477917945', 'SMSIND', wish )



    
btn2=tk.Button(win,text='WIsh',width=40,command=send)
btn2.grid(row=8,column=0,columnspan=2)   
frame=tk.Frame(win,bd=4,bg="crimson")
frame.place(x=850,y=100,width=500,height=1000)



win.mainloop()
