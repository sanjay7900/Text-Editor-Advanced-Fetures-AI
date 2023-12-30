from tkinter import *
from tkinter import ttk
import tkinter as tk
import json
import requests
from textblob import TextBlob as tr

from tkinter import font
from tkinter import filedialog as fd
import os
import PyPDF2 
from tkinter.colorchooser import askcolor
import speech_recognition as sr

from gtts import gTTS
#eng = pyttsx3.init()

from spellchecker import SpellChecker
from gingerit.gingerit import GingerIt
from googletrans import Translator
import googletrans as gt
from tkinter import messagebox


class text:
    file_status=""
    datalist=[]
    cut_copy=''
    all_lang=''

    
    mylang={'Afrikaans':'af',
       'Irish':'ga',
        'Albanian':'sq',
         'Italian':'it',
         'Arabic':'ar',
         'Japanese':'ja',
          'Azerbaijani':'az',
        'Kannada':'kn',
           'Basque':'eu',
          'Korean':'ko',
            'Bengali':'bn',
          'Latin':'la',
             'Belarusian':'be',
          'Latvian':'lv',
          'Bulgarian':'bg',
          'Lithuanian':'lt',
           'Catalan':'ca',
            'Macedonian':'mk',
            'Chinese Simplified':'zh-CN',
             'Malay':'ms',
              'Chinese Traditional':'zh-TW',
              'Maltese':'mt',
             'Croatian':'hr',
                  'Norwegian  ':'no',
              'Czech':'cs',
                'Persian':'fa',
                'Danish':'da',
                'Polish':'pl',
               'Dutch':'nl',
                'Portuguese':'pt',
                'English':'en',
                     'Romanian':'ro',
                'Esperanto':'eo',
                'Russian':'ru',
               'Estonian':'et',
                     'Serbian':'sr',
              'Filipino':'tl',
                 'Slovak':'sk',
               'Finnish':'fi',
             'Slovenian':'sl',
             'French':'fr',
                 'Spanish':'es',
             'Galician':'gl',
              'Swahili':'sw',
              'Georgian':'ka',
              'Swedish':'sv',
                  'German	':'de',
                  'Tamil':'ta',
                 'Greek':'el',
                    'Telugu':'te',
                      'Gujarati':'gu',
                     'Thai':'th',
                   'Haitian Creole':'ht',
                   'Turkish':'tr',
                      'Hebrew':'iw',
                      'Ukrainian':'uk',
                      'Hindi':'hi', 
                      'Urdu':'ur',
                     'Hungarian':'hu',
                     'Vietnamese':'vi',
                  'Icelandic':'is',
                   'Welsh':'cy',
                    'Indonesian':'id',
                     'Yiddish':'yi',}
    
        
    
    
    def __init__(self,window):
        self.window=window
        self.window.geometry('1200x900')
        self.menubar=Menu(window)
        self.window.minsize(1350,2000)
        self.window.title("Voice Text Editor "+self.file_status)
        self.window.option_add("*Font", 'Verdana 14')
        self.fontst_var = tk.StringVar()
        self.find_lang=tk.StringVar()
        self.fontsize_var=tk.StringVar()
        self.ch=GingerIt()

    
        # All ICON IS HERE
        
        

        
        self.window.config(menu=self.menubar)
        
        
        self.frame1 =Frame(self.window, bd=10,relief=GROOVE, bg="#074463")
        self.frame1.place(x=0, y=0, width=1350,height=100)
        
        self.frame2 =Frame(self.window, bd=10,relief=GROOVE, bg="white")
        self.frame2.place(x=0, y=100, width=1350,height=550)
        self.frame2.pack_propagate(False)
        self.frame2.grid_propagate(False)

        self.text=Text(self.frame2,width=108,height=22,undo=True,wrap=WORD)
        self.text.focus_set()

        self.hscroll = ttk.Scrollbar(self.frame2, orient=HORIZONTAL,command=self.text.xview)
        self.vscroll = ttk.Scrollbar(self.frame2,orient=VERTICAL,command=self.text.yview)
        
        self.hscroll.pack(side=BOTTOM,fill=X)
        self.vscroll.pack(side=RIGHT,fill=Y)
        
        self.text.pack()
        self.text['xscrollcommand'] = self.hscroll.set
        self.text['yscrollcommand'] = self.vscroll.set
        self.text.insert(INSERT,"welcme to gla universty")
        
        def aud():
            
            text=""
            r= sr.Recognizer()
            with sr. Microphone() as source:
                print("say something")
                r.pause_threshold=1
                audio=r.listen(source)
            try:
                text= r.recognize_google(audio)
                print(text)
                text=" "+text
                self.text.insert(INSERT,text)

                #i=gTTS(text)
                # i.save("muc.mp3")
                # pygame.mixer.music.load('muc.mp3')
                # pygame.mixer.music.play()
      
 
            except Exception as es:
                 messagebox.showinfo("there is problem try again...")       
        
        def select():
            try:
                t=self.text.selection_get()
                print(t)
            except Exception as e:
                pass
                
                
        def check():
            try:
            
                
                item=str(self.text.get(1.0,END))
                print(item)
                t=chAgain(item)#str(GingerIt().parse('welcme to gla universty'))
                print(t)
                h=t#['corrections']
                print(h)
                for i in h:
                    print(i)
                    idx = '1.0'
                    while 1:
                        
                        # searches for desired string from index 1
                        #idx = self.text.search(i['text'], idx, nocase = 1,stopindex = END)
                        idx = self.text.search(i, idx, nocase = 1,stopindex = END)

                        if not idx: break
                        # last index sum of current index and
                        # length of text
                        #lastidx = '% s+% dc' % (idx, len(i['text']))
                        lastidx = '% s+% dc' % (idx, len(i))
             
 
                        # overwrite 'Found' at idx
                        self.text.tag_add('found', idx, lastidx)
                        idx = lastidx
                        # mark located string as red
                        self.text.tag_config('found', foreground ='red')
            except Exception as e:
                 print(e)
                
        def chAgain(data):
            misspelled=[]
            string_to_List=data.split(" ")
            misspelled=SpellChecker().unknown(string_to_List)
            res = []
            for sub in misspelled:
                res.append(sub.replace("\n", ""))
            return res
            
            
        def msginfo(msg):
            messagebox.showinfo('information',msg)        
        def bold_it():
            
            try:
                bold_font=font.Font(self.text,self.text.cget("font"))
                bold_font.configure(weight="bold")
                self.text.tag_configure("bold",font=bold_font)
                curtag=self.text.tag_names("sel.first")
                if "bold" in curtag:
                    self.text.tag_remove("bold","sel.first","sel.last")

                else:
                    self.text.tag_add("bold","sel.first","sel.last")
                
                #correct(self.text.get(1.0,END))
            except Exception as e:
                msginfo(" You hava to select an area to change the color of that area")
                
        def italic_it():
            try:
                italic_font=font.Font(self.text,self.text.cget("font"))
                italic_font.configure(slant="italic")
                self.text.tag_configure("italic",font=italic_font)
                curtag=self.text.tag_names("sel.first")
                if "italic" in curtag:
                    self.text.tag_remove("italic","sel.first","sel.last")

                else:
                    self.text.tag_add("italic","sel.first","sel.last")
                
                #correct(self.text.get(1.0,END))
            except Exception as e:
                msginfo(e)
            
        def under_line():
            try:
                italic_font=font.Font(self.text,self.text.cget("font"))
                italic_font.configure(underline=1)
                self.text.tag_configure("under",font=italic_font)
                curtag=self.text.tag_names("sel.first")
                if "under" in curtag:
                    self.text.tag_remove("under","sel.first","sel.last")

                else:
                    self.text.tag_add("under","sel.first","sel.last")
                
                #correct(self.text.get(1.0,END))
            except Exception as e:
                msginfo(e)
            
        def color():
            try:
                clr=askcolor()[1]
                if clr:
                    color_font=font.Font(self.text,self.text.cget("font"))
                    #color_font.configure(fg=clr)
                    self.text.tag_configure("color",font=color_font,foreground=clr)
                    self.text.tag_add("color","sel.first","sel.last")
            except Exception as e:
                msginfo(e)
        def colorfont():
            try:
                clr=askcolor()[1]
                if clr:
                    self.text['foreground']=clr

            except Exception as e:
                
                msginfo(e)
                                
        def correct():
            #ch=GingerIt()

        
            data=self.text.get(1.0,END)
            if not(self.text.compare("end-1c","==","1.0")):
                item=str(self.text.get(1.0,END))
                t=tr(item)#self.ch.parse(item)
                
                h=t.correct()#['result']
                self.text.delete(1.0,END)
                self.text.insert(END,h)
                print("oo")
            else:
                messagebox.showinfo("text box epeaty or may be an issu...")       

        def all_font_fam():
            return font.families()
        

        def find_all_lang():
            
            return self.mylang
        self.all_lang=[j for j in find_all_lang()]

        def transltr(e):
            try:
                goto_translate=Translator()
                self.change_data=str(self.text.get(1.0,END))
                if self.change_data!="":
                    self.text.delete(1.0,END)
                    dis=self.mylang[self.find_lang.get()]
                    data = goto_translate.translate(self.change_data,dest=dis)
                    self.text.insert(1.0,data.text)
                else:
                    messagebox.showinfo("empaty text box...")       

            except Exception as e:
                messagebox.showinfo("there",e)       

        def previous_data():
            self.text.delete(1.0,END)
            self.text.insert(1.0,self.change_data)
            
        new_image = tk.PhotoImage(file='new-document.png')
        cut_image = tk.PhotoImage(file='C:/sanjaypersonal/ssl.PNG')
        print(cut_image)
        save_image = tk.PhotoImage(file='save.png')
        paste_image = tk.PhotoImage(file='paste.png')
        copy_image = tk.PhotoImage(file='copy.png')
        def align_center():
            getdata=self.text.get(1.0,END)
            self.text.tag_config("center", justify=tk.CENTER)
            self.text.delete(1.0,END)
            self.text.insert(tk.INSERT,getdata,"center")
        def align_right():
            getdata=self.text.get(1.0,END)
            self.text.tag_config("right", justify=tk.RIGHT)
            self.text.delete(1.0,END)
            self.text.insert(tk.INSERT,getdata,"right")    
            
        def align_left():
            getdata=self.text.get(1.0,END)
            self.text.tag_config("left", justify=tk.LEFT)
            self.text.delete(1.0,END)
            self.text.insert(tk.INSERT,getdata,"left")    
        but_1=Button(self.frame1, text=' start Listen',width=20,height=1,command=aud,font=( 'aria' ,8, 'bold' ),bg='brown', fg='white').grid(row=1,column=8,padx=5)
        
        select_left=Button(self.frame1, text='ALIGN LEFT',command=align_left,width=12,font=( 'aria' ,8, 'bold' ),bg='brown', fg='white').grid(row=0,column=3,padx=1)
        select_center=Button(self.frame1, text='ALIGN CENTER',command=align_center,width=12,font=( 'aria' ,8, 'bold' ),bg='brown', fg='white').grid(row=0,column=4,padx=1)
        select_right=Button(self.frame1, text='ALIGN RIHGT',command=align_right,width=12,font=( 'aria' ,8, 'bold' ),bg='brown', fg='white').grid(row=0,column=5,padx=1)

        
        change_text=Button(self.frame1, width=20,text='check grammerlly',height=1,command=check,font=( 'aria' ,8, 'bold' ),bg='brown', fg='white').grid(row=0,column=8,padx=5)
        select_foclr=Button(self.frame1, text='font color',command=colorfont,width=12,height=2,font=( 'aria' ,8, 'bold' ),bg='brown', fg='white').grid(row=1,column=5,padx=1)
        
        change_color_text=Button(self.frame1, width=12,height=2,text='text color',command=color,font=( 'aria' ,8, 'bold' ),bg='brown', fg='white').grid(row=1,column=4,padx=5)
        
        but_1=Button(self.frame1, text='bold',width=12,command=bold_it,font=( 'aria' ,8, 'bold' ),bg='#9896AD', fg='black').grid(row=0,column=2)
        
        select_text=Button(self.frame1, text='italic',width=12,height=2,command=italic_it,font=( 'aria' ,8, 'bold' ),bg='#EE0AF5', fg='white').grid(row=1,column=2,padx=5)
        
        change_text=Button(self.frame1,text="Under line",width=12,height=2,command=under_line,font=( 'aria' ,8, 'bold' ),bg='brown', fg='white').grid(row=1,column=3,padx=5)
        
        change_color_text=Button(self.frame1, text='Correct Error',height=5,command=correct,font=( 'aria' ,8, 'bold' ),bg='brown', fg='white').grid(row=0,rowspan=2,column=9,padx=5)
        trans_label =Label(self.frame1,text="Translate",font=( 'aria' ,8, 'bold' ),bg='brown', fg='white').grid(row=1,column=1,padx=5)
        self.datalist=list(all_font_fam())
        change_sp=Label(self.frame1,height=1).grid(row=0,column=7,padx=5)
        change_sp=Label(self.frame1,height=2).grid(row=1,column=7,padx=5)


        
        font_style = ttk.Combobox(self.frame1,values=self.datalist,textvariable=self.fontst_var)
        font_style.grid(row=0,column=0,padx=5)
        font_style.set("Arial")
        lang = ttk.Combobox(self.frame1,values=self.all_lang,textvariable=self.find_lang)
        lang.grid(row=1,column=0)
        def change_style(e):
            style=self.fontst_var.get()
            sset=font.Font(family=style,size=self.fontsize_var.get())
            size=font.Font(size=14)
            self.text.configure(font=size)

            self.text.configure(font=sset)

            print(sset)
        def size_chng(e):
            
            change_style(e)

            
        font_style.bind("<<ComboboxSelected>>", change_style)
        lang.bind("<<ComboboxSelected>>", transltr)
        lang.set("English")
        font_size = ttk.Combobox(self.frame1,values=[2,4,8,12,14,16,18,20,22,28,32,34,36,40],textvariable=self.fontsize_var)
        font_size.grid(row=0,column=1,padx=5)
        font_size.bind("<<ComboboxSelected>>", size_chng)
        font_size.set(20)
        
        #trans_value=ttk.Combobox(
        
        def all_icon_button():pass


        
        #b=Button(self.frame1,text="jjfi").grid()'''
        
        
    
        
           
    def makemenubar(self,name,*args):
        def hello():
            
            print("fghjkl")
        # all icon here
        def open_files():
            new_f=fd.askopenfilename(title="Open new file")
            #print(self.text.get(1.0,END),new_f)
            #self.text.delete(1.0,END)
            #self.file_status=new_f
            
            
            try:
                
                self.file_status=new_f
                split_tup = os.path.splitext(new_f)
                ext=split_tup[1]
                if ext=='.pdf' or ext=='.PDF':
                    pdf_file= PyPDF2.PdfFileReader(new_f)
                    #Select a Page to read
                    page= pdf_file.getPage(0)
                    #Get the content of the Page
                    content=page.extractText()
                    #Add the content to TextBox
                    self.text.delete(1.0,END)
                    self.window.title("Voice Text Editor "+self.file_status)

                    self.text.insert(1.0,content)

                
                else:
                    
                    with open(new_f,'r') as file:
                        self.window.title("Voice Text Editor "+self.file_status)
                        content = file.read()
                        self.text.delete(1.0,END)
                        self.text.insert(END,content)
                        file.close()
            except Exception as e:
                messagebox.showinfo(e,'error accur')
            
        def save_file():
            try:
                if self.file_status=='':
                    self.file_status=fd.asksaveasfile(mode='w' ,defaultextension="txt" ,filetypes=(("text file","*.txt"),("All files","*.*s")))
                    self.file_status=self.file_status.name
                    with open(self.file_status,'w') as wr:
                        wr.write(self.text.get(1.0,END))
                        wr.close()
                    
                else:
                    with open(self.file_status,'w') as wr:
                        wr.write(self.text.get(1.0,END))
                        wr.close()
            except Exception as e:
                print(e)
                
            
            
        def save_as_file():
            try:
                os.remove(self.file_status)
                self.file_status=fd.asksaveasfile(mode='w' ,defaultextension=".txt" ,filetypes=(("text file","*.txt"),("All files","*.*")))
                #print(self.file_status)
                if self.file_status:
                    self.file_status=self.file_status.name
                    self.window.title("Voice Text Editor "+self.file_status)

                    with open(self.file_status,'w') as wr:
                        wr.write(self.text.get(1.0,END))
                        wr.close()
                
            except Exception as e:
                print(e)
        def new_file():
            data=str(self.text.get(1.0,END))
            if not self.file_status:
                content='# new file write here'
                self.text.insert(1.0,content)
                self.file_status=''
            else:
                save_file()
                self.text.delete(1.0,END)
                content=('# new file write here2')
                self.text.insert(1.0,content)
                self.file_status=''
                self.window.title("Voice Text Editor "+self.file_status)

                
                

                
        def color_thm():
            clr=askcolor()[1]
            if clr:
                self.text['background']=clr

        def copy_text(e):
            if self.text.selection_get():
                self.cut_copy=self.text.selection_get()
                
        def paste_text(e):
            if self.cut_copy:
                position=self.text.index(INSERT)
                self.text.insert(position,self.cut_copy)
        def cut_text(e):
            if self.text.selection_get():
                self.cut_copy=self.text.selection_get()
                self.text.delete("sel.first","sel.last")
        
        
        '''new_image = tk.PhotoImage(file='new-document.png')
        cut_image = tk.PhotoImage(file='C:/sanjaypersonal/ssl.PNG')
        print(cut_image)
        save_image = tk.PhotoImage(file='save.png')
        paste_image = tk.PhotoImage(file='paste.png')
        copy_image = tk.PhotoImage(file='copy.png')'''
        
        '''saveas_image = tk.PhotoImage(file='saveas.png')
        bold_image = tk.PhotoImage(file='bold.png')
        italic_image = tk.PhotoImage(file='italic.png')
        underline_image = tk.PhotoImage(file='underline.png')
        right_float_image = tk.PhotoImage(file='r_float.png')'''
        
        # This is file menu
        Filemenu=Menu(self.menubar)
        self.menubar.add_cascade(label="File",menu=Filemenu)
        Filemenu.add_command(label="New File",accelerator='Ctrl+o',compound=tk.LEFT,command=new_file)
        Filemenu.add_command(label="Open File",command=open_files)
        Filemenu.add_command(label="Save File",command=save_file)
        Filemenu.add_command(label="Save as",command=save_as_file)

          #This is Editmenu
        Editmenu=Menu(self.menubar)
        self.menubar.add_cascade(label="Edit",menu=Editmenu)
        Editmenu.add_command(label="Cut ",command=lambda:cut_text(False))
        Editmenu.add_command(label="Copy",command=lambda:copy_text(False))
        Editmenu.add_command(label="Paste",command=lambda:paste_text(False))
        Editmenu.add_command(label="Redo",command=self.text.edit_redo)
        Editmenu.add_command(label="Undo",command=self.text.edit_undo)
        #This is Format menu
        Formatmenu=Menu(self.menubar)
        self.menubar.add_cascade(label="color theam",menu=Formatmenu)
        Formatmenu.add_command(label="choose color",command=color_thm)
        
        #Editmenu.add_command(label="Save as",command=hello)
        
        
          

        #for i in args:
           # namemenu.add_command(label=i,command=hello)
  
        
      

def mainfun():
    
    
    root=Tk()
    userinterface=text(root)
    userinterface.makemenubar("hello",'edit','paste')
    #userinterface.makemenubar("dssdd")

    #root.resizable(0, 0)
    mainloop()

    
mainfun()    
    
