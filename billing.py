import tkinter as tk
from tkinter import *
import tempfile
import os
import time
from tkinter import ttk
from PIL import ImageTk,Image
import sqlite3
import tkinter.messagebox
from tkinter import messagebox
import datetime
global database
global one_time_check
one_time_check=0
win=tk.Tk()
########################

"""
#=============================================================new
canvas = Canvas(win,  height=800, width=1350)
image = ImageTk.PhotoImage(Image.open("C:/Users/Krishna/Desktop/c1.png"))
image2 = ImageTk.PhotoImage(Image.open("C:/Users/Krishna/Desktop/pppp.png"))

canvas.create_image(5,0, anchor=NW, image=image)
canvas.create_image(800,150, anchor=NW, image=image2)
canvas.grid()    


#==========================================================new end
"""


#database=""
database=""
#########    ALL    VARIABLE    ##############################################
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
data_base=tk.StringVar()

cal_price=tk.DoubleVar()

cal_gst=tk.DoubleVar()

cal_amt=tk.DoubleVar()

cal_item=tk.StringVar()

cal_qut=tk.DoubleVar()

cal_id=tk.IntVar()

global datalist

global bill


global d

global bill_list

bill_list=[]

datalist=[]

Add_item=tk.StringVar()

price=tk.DoubleVar()

create_new_data=tk.StringVar()

getdatabase=""

d=""

yes=0

global l

l=[]
global total_bill_rate

total_bill_rate=0

customer=tk.StringVar()

phone=tk.StringVar()

new_item=tk.StringVar()

new_price=tk.DoubleVar()

new_gst=tk.DoubleVar()

new_qunt=tk.DoubleVar()

new_id=tk.IntVar()



update_item_new=tk.StringVar()
update_name=tk.StringVar()
update_id=tk.IntVar()
update_gst=tk.DoubleVar()
update_quantity=tk.DoubleVar()
update_price=tk.DoubleVar()


#delete variable are here
item_to_be_delete=tk.StringVar()
#max sales item variabnle
max_item_sales=tk.StringVar()
max_quantity_sales=tk.DoubleVar()








#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def removewin():
    global win
    for widget in win.winfo_children():
        widget.grid_remove()
        
def loginpage():

#================================================================================
    """
    F =Frame(canvas, highlightbackground="black", highlightcolor="black", highlightthickness=1,bd=20,bg="green")
    F.place(x=100, y=50, width=600,height=700)
    text1=tk.Label(F,text="Hello , Friends!",font=("Arial Bold", 30),bg="green",fg="white").place(x=160,y=150)
    text2=tk.Label(F,text="Fill up personal information and",font=("Arial Bold", 28),bg="green",fg="white").place(x=0,y=250)
    text3=tk.Label(F,text="Start journey with us.",font=("Arial Bold", 30),bg="green",fg="white").place(x=100,y=350)
    """
#==================================================================================================
    
    
    #top1=Toplevel()
    win.minsize(1350,2000)
    user=tk.StringVar()
    password=tk.StringVar()


    
    #border=tk.Canvas(win,width=1000,height=1000)
    admin=tk.Label(win,text="Admin_login",font=("Arial Bold", 38))
    admin.grid(row=0,column=0, columnspan=1,pady=(0,0),padx=(70,0))
    
    username=tk.Label(win,text="Username",font=("Arial Bold", 18))
    username.grid(row=1,column=0,pady=(100,0),padx=(30,0))
    enter_user=ttk.Entry(win,textvariable=user)
    enter_user.grid(row=1,column=1,pady=(100,0),padx=(30,0))
    
    pasword=tk.Label(win,text="Password",font=("Arial Bold", 18))
    pasword.grid(row=2,column=0,pady=(10,0),padx=(30,0))
    enter_pass=ttk.Entry(win,textvariable=password,show="*")
    enter_pass.grid(row=2,column=1,pady=(10,0),padx=(30,0))

    """
    enter_user=ttk.Entry(canvas,textvariable=user).place(x=710,y=500,width=490,height=30)
    enter_pass=ttk.Entry(canvas,textvariable=password,show="*").place(x=710,y=610,width=490,height=30)
    """
    
    def login():
        us=user.get()
        ps=password.get()
        if us=="admin" and ps =="admin":
            removewin()
            select_data_base_window()
        else:
            tk.messagebox.showerror("ERROR","invalid user or password")

            
    logbtn=ttk.Button(win,text="Login",command=login)
    logbtn.grid(row=3,column=0,pady=(10,0),padx=(60,0))
   

"""
#===============================================================new
    logbtn=ttk.Button(canvas,text="Login",command=login).place(x=710,y=691,width=490,height=63)
#=============================================================new end

"""
    
def dada_base_info():
    global d
    d=data_base.get()
    if d=="":
        tk.messagebox.showerror("warning","select database")
    else:
        #datalist.append(d)
        #database=data.get()
       ## conn=sqlite3.connect(database+ext)
       # cur=conn.cursor()
        #if d not in dalalist:
          #  pass
            
        main_task()
#-------------------------------------------------------------------------------------------------------------------------------------------------        
def take_items_from_database():
    global datalist
    global d
    datalist=[]
    ext=".db"
    conn=sqlite3.connect(d+ext)
    cur=conn.cursor()
    sql=""" SELECT itemname FROM item"""
    cur.execute(sql)
    find=cur.fetchall()
    for i in find:
        datalist.extend(i)

    return datalist



        
#---------------------------------------------------------------------------------------------------------------------------------------------------


        
def calculate_bill():
    global d
    global cal_item
    global cal_qut
    global cal_gst
    global l
    global bill
    global bill_list
    global show_sales
    ext=".db"
    conn=sqlite3.connect(d+ext)
    cur=conn.cursor()
    getitem=cal_item.get()
    q=float(cal_qut.get())
    #print(getitem,q)
    if getitem !=""and q!=0:
        
        
        
        cur.execute('SELECT id, price,gst FROM item WHERE itemname=?',(getitem,))
        
        acorrding_item=cur.fetchone()
        
        gst=float(acorrding_item[2])
        single_gst=gst
        #print(acorrding_item,gst)
        gst=gst*q
    
        amount=acorrding_item[1]
        amount=amount*q
        addgst=(amount*gst)/100
        amount=amount+addgst

    
        cal_price.set(amount)
        
        cal_id.set(acorrding_item[0])
        
        cal_gst.set(gst)
        
        l=[]
        
        a=cal_price.get()
        global total_bill_rate
        total_bill_rate=total_bill_rate+a
        
        b=cal_item.get()
        
        c=cal_gst.get()
        
        date=datetime.date.today()
        
        customer_name=customer.get()
        
        pho=phone.get()
        
        bill_list=cal_item.get(),cal_gst.get(),cal_price.get()
        #=========
        detail=[customer_name,pho]
        
        cur.execute('INSERT INTO daleysales(date,customername,itemname,totalquantity,totalprice,totalgst)VALUES(?,?,?,?,?,?)',(date,customer_name,b,q,a,c))
        
        conn.commit()
        global one_time_check
        
        if one_time_check==0:
            one_time_check_coutomer_details(customer_name,pho)
            one_time_check=1
            
        
        if yes==0:
            
            #bill.insert(END,detail,'\n')
            bill.insert(END,f"\n{ cal_item.get()},\t{q},\t\t{single_gst},\t{cal_gst.get()},\t{cal_price.get()}")
        
        
        
    
    else:
        tk.messagebox.showerror('Warning','fill qty or itm')
    

def description():
    global d
    ext=".db"
    conn=sqlite3.connect(d+ext)
    cur=conn.cursor()
    getdata=cal_item
    if getdata!="":
        pass
        
#===================================================================================================================================================
    

def select_data_base_window():
    win.minsize(1350,2000)
    newbutton=tk.Button(win,text="New",font=("Arial Bold", 18),height=2,width=4,command=new_database)
    newbutton.grid(row=0,column=0,padx=1200,pady=10)
    frame1=tk.Label(win,bd=10,bg="goldenrod")
    frame1.place(x=400,y=60,height=500,width=500)
    datainfo=tk.Label(frame1,text="SELECT  YOUR  DATA_BASE", bg='DarkSeaGreen4', font=("Arial Bold", 24))
    datainfo.grid(row=0,column=0,padx=10,pady=3)
    data=ttk.Combobox(frame1,width=20,textvariable=data_base,font=("Arial Bold", 18))
    data["values"]=datalist
    data.grid(row=1,column=0,padx=20,pady=40)
    button=tk.Button(frame1,text="process",font=("Arial Bold", 18),command=dada_base_info)
    button.grid(row=2,column=0,padx=10,pady=10)
    info=tk.Label(frame1,text="Welcome Users", bg='DarkSeaGreen4', font=("Arial Bold", 24), width=15,height=5)
    info.grid(row=3,column=0,padx=10,pady=10)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
def new_database():
    call_new()
    
def call_new():
    top=Toplevel(win,bg="medium spring green")
    top.minsize(1350,2000)
    frame2=Frame(top,bd=20,bg="lemon chiffon")
    frame2.place(x=200,y=100,width=1000,height=1000)
    name=tk.Label(frame2,text="Create your NewDataBase",font=("Arial Bold",28),width=25,height=3,bg="steel blue")
    name.grid(row=0,column=0,padx=230,pady=10)
    data_enter=ttk.Entry(frame2,width=25,textvariable=data_base,font=("Arial Bold", 18))
    data_enter.grid(row=1,column=0,pady=10)
    databas=tk.Button(frame2,text="create DataBase",font=("Arial Bold", 24),command=create)
    databas.grid(row=2,column=0,columnspan=1)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------    
    
    
def one_time_check_coutomer_details(customer_name,pho):
    bill.delete('1.0',END)
    bill.insert(END,"\t Welcome My Shop")
    #bill.insert(END,f"\n Bill number: {bill_no.get()}")
    bill.insert(END,f"\n Customer name: {customer_name}")
    bill.insert(END,f"\n Phone number: {pho}")
    bill.insert(END,f"\n==================================================")
    bill.insert(END,f"\n Products|\tQty|\tGST/kg(item)|\tTotal %GST|\tPrice")
    bill.insert(END,f"\n==================================================")
















    
    
def mainwindow():
    
    #win=tk.Tk()
    top=Toplevel(win)
    top.minsize(1350,2000)
    border=tk.Canvas(top,width=1000,height=1000)
    border.pack()
    frame1=tk.Frame(top,bd=10,bg="crimson")
    frame1.place(x=0,y=0,width=1000,height=100)
    frame2=tk.Frame(top,bd=10,bg="")
    frame2.place(x=0,y=100,width=500,height=1000)

    data=tk.StringVar()
    data_enter=ttk.Entry(frame1,width=25,textvariable=data,font=("Arial Bold", 18))
    data_enter.grid(row=1,column=2)
    
#'''def ck():
    
   # database=data.get()
    #ext=".db"
    #conn=sqlite3.connect(database+ext)
    #cur=conn.cursor()
    #print(database)'''
    item=tkinter.Label(frame2,text='Item name',font=("Arial Bold", 18))
    item.grid(row=0,column=0)
    tmenter=tk.StringVar()

    item_enter=tk.Entry(frame2,textvariable=tmenter,bd=10)
    item_enter.grid(row=0,column=5)

    line=tkinter.Label(frame2)
    line.grid(row=2,column=0)

    price=tkinter.Label(frame2,text='Price         ',font=("Arial Bold", 18))
    price.grid(row=3,column=0)

    penter=tk.StringVar()

    price_enter=tk.Entry(frame2,textvariable=penter,bd=10)
    price_enter.grid(row=3,column=5)

    line=tkinter.Label(frame2)
    line.grid(row=4,column=0)


    brand=tkinter.Label(frame2,text='brand          ',font=("Arial Bold", 18))
    brand.grid(row=5,column=0)

    benter=tk.StringVar()
    i=data_base.get()

    

    benter.set(i)

    brand_enter=tk.Entry(frame2,text=benter,bd=10)
    brand_enter.grid(row=5,column=5)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
def create():
    global d
    d=data_base.get()
    if d!="":
        try:
            
            ext=".db"
            conn=sqlite3.connect(d+ext)
            cur=conn.cursor()
            table1="""CREATE TABLE item(id int PRIMARY KEY ,itemname char UNIQUE ,price float, gst float,quantity float,date )"""
            cur.execute(table1)
            #if checkl!=True:
                
            #ans=tk.messagebox.showerror('warning','SOMETHING WRONG')

                
            table2="""CREATE TABLE daleysales(date,customername char,itemname,totalquantity,totalprice float,totalgst float)"""
            check2=cur.execute(table2)
            #if check2!=True:
                
            ##ans=tk.messagebox.showerror('warning','SOMETHING WRONG')
            main_task()        
        except Exception as e:
             
             tk.messagebox.showerror("Warning","database already exist")

    else:
        ans=tk.messagebox.showerror('warning','YOU have fill the option')
            
    #take_items_from_database()
   # databas=tk.Button(frame1,text="create DataBase",font=("Arial Bold", 24),command=create)
    #databas.grid(row=1,column=0,columnspan=1)
     #

     #database2=tk.Button(frame1,text="create DataBase",font=("Arial Bold", 24),command=ck)
     #database2.grid(row=1,column=3,columnspan=3)
    
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++






def main_task():
    global bill
    wi=Toplevel(win)
    wi.geometry('1360x1500')
    Frame3 =Frame(wi, bd=10,relief=GROOVE, bg="#074463")
    Frame3.place(x=0, y=0, width=1600,height=80)
    but_1=Button(Frame3, text='Add item', width=12, bg='brown', fg='white', command=open_win).grid(row=0, column=0, padx=10,pady=10)
    but_2=Button(Frame3, text='Update item', width=12, bg='brown', fg='white', command=open_win2).grid(row=0, column=1, padx=10,pady=10)
    but_3=Button(Frame3, text='Delete item', width=20, bg='brown', fg='white', command=open_win3).grid(row=0, column=2, padx=10,pady=10)
    but_4=Button(Frame3, text='Sales as per day', width=20, bg='brown', fg='white', command=open_win4).grid(row=0, column=3, padx=10,pady=10)
    but_5=Button(Frame3, text='Maximum Sales', width=20, bg='brown', fg='white', command=open_win5).grid(row=0, column=4, padx=10,pady=10)

    try:
        
        take_items_from_database()
    except :
        tk.messagebox.showerror("error","something wrong")

    Frame4 =Frame(wi, bd=10,relief=GROOVE, bg="#074463")
    Frame4.place(x=0, y=60, width=1600,height=80)
    lbl = Label(Frame4, font=( 'aria' ,28, 'bold' ),text="BILLING SYSTEM",bd=5,fg="white",bg="#074463")
    lbl.grid(row=0,column=0,padx=500)


    Frame1 = LabelFrame(wi,bd=10,relief=GROOVE,text="Customer Details", font=("times new roman",15,"bold"),fg="yellow", bg="#074463")
    Frame1.place(x=0, y=140, width=900,height=500)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #new
    lbl = Label(Frame1, font=( "times new roman",18,"bold" ),text="Customer Name",fg="white",bg="#074463")
    lbl.grid(row=0,column=0,padx=20, pady=5,sticky="w")
    txt = Entry(Frame1,font="arial",bd=7,relief=SUNKEN,textvariable=customer,width=15)
    txt.grid(row=0,column=1,padx=0,pady=5, sticky="w")
    global l
    l=[9,9,9,9,]

    lbl=Label(Frame1,text='Phone no.',font=("times new roman",18,"bold"),fg="white",bg="#074463")
    lbl.grid(row=0,column=2,padx=0, pady=5,sticky="w")
    txt = Entry(Frame1,font="arial",bd=7,relief=SUNKEN,textvariable=phone,width=15)
    txt.grid(row=0,column=3,padx=10,pady=5)
    
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


    lbl= Label(Frame1, font=("times new roman",18,"bold"),text="Item name",fg="white",bg="#074463")
    lbl.grid(row=1,column=0,padx=20, pady=50,sticky="w")
    combobox = ttk.Combobox(Frame1, values=datalist,textvariable=cal_item ,width=12,state="readonly",font=( 'aria' ,14, 'bold' ))
    combobox.grid(row=1,column=1,padx=0,pady=50,sticky="w")

    lbl = Label(Frame1, font=("times new roman",18,"bold"),text="Quantity",fg="white",bg="#074463")
    lbl.grid(row=1,column=2,padx=0,pady=50,sticky="w")
    combobox = tk.Entry(Frame1, textvariable=cal_qut,width=15,font="arial",bd=7,relief=SUNKEN)
    combobox.grid(row=1,column=3,padx=10,pady=50)


    lbl = Label(Frame1, font=("times new roman",18,"bold"),text="Gst",fg="white",bg="#074463")
    lbl.grid(row=2,column=0,padx=20, pady=40,sticky="w")
    txt = Entry(Frame1,font="arial",bd=7,relief=SUNKEN,textvariable=cal_gst,width=15,state="readonly")
    txt.grid(row=2,column=1,padx=0,pady=40,sticky="w")

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#new
    lbl=Label(Frame1,text='Price',font=("times new roman",18,"bold"),fg="white",bg="#074463")
    lbl.grid(row=2,column=2,padx=0, pady=40,sticky="w")
    txt = Entry(Frame1,font="arial",bd=7,relief=SUNKEN,textvariable=cal_price,state="readonly",width=15)
    txt.grid(row=2,column=3,padx=10,pady=40)

    but_1=Button(Frame1, text='Enter',command=calculate_bill, width=14,font=( 'aria' ,16, 'bold' ), bg='brown', fg='white').grid(row=50, column=1, padx=(150,0),pady=20, sticky="w")
    #box = Listbox(Frame1, width=146, height=5).place(x=0,y=380)
    

    
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++    
    #but_1=Button(Frame1, text='Enter', width=14,font=( 'aria' ,16, 'bold' ), bg='brown', fg='white',command=calculate_bill).grid(row=60, column=3, padx=1, pady=50)


    Frame2 = Frame(wi, bd=10,relief=GROOVE, bg="#074463")
    Frame2.place(x=927, y=140, height=500, width=430)

   # recipts = Listbox(Frame2, width=60, height=20)
    
    #recipts.grid(row=0, column=0, padx=10)#.place(x=40, y=50)

    #recipts.insert('end',l)
    bill=Text(Frame2,width=50, height=20)
    bill.grid(row=0, column=0, padx=2)
    
    #but_1=Button(Frame2, text='Enter',command=calculate_bill, width=14,font=( 'aria' ,16, 'bold' ), bg='brown', fg='white').grid(row=50, column=0, padx=10,pady=20)
    but_1=Button(Frame2, text='Print',command=iPrint, width=14,font=( 'aria' ,16, 'bold' ), bg='brown', fg='white').grid(row=60, column=0, padx=10,pady=20)
    


    Frame5 = Frame(wi, bd=10,relief=GROOVE, bg="#074463")
    Frame5.place(x=0, y=640, width=1600,height=80)
    lbl = Label(Frame5, font=( 'Monotype Corsiva' ,14, 'bold' ),text='designed by UNICO Team',fg="white",bg="#074463")
    lbl.grid(row=0,column=0,padx=550,pady=15)

    











    
   
#=================================================================================================================================================================    

def open_win():
    wi=Toplevel(win)
    wi.geometry('1600x1500')
    frame2=LabelFrame(wi, bd=10,text='Add Product Details',relief=GROOVE, bg="#074463",font=("times new roman",15,"bold"),fg="yellow")
    frame2.place(x=200, y=100, width=1000, height=500)
    wi.title("Add Product Details")
    l2=Label(frame2,text='Product ID',font=("times new roman",18,"bold"),fg="white",bg="#074463").grid(row=1, column=10, padx=150, pady=25)#.place(x=600,y=200)
    e2=Entry(frame2,textvariable=new_id, bd=5,width=35).grid(row=1, column=50, padx=0, pady=0)#.place(x=750,y=200)
    
    l3=Label(frame2,text='Product Name',font=("times new roman",18,"bold"),fg="white",bg="#074463").grid(row=2, column=10, padx=0, pady=25)#.place(x=600,y=225)
    e3=Entry(frame2, textvariable=new_item,bd=5,width=35).grid(row=2, column=50, padx=0, pady=0)#.place(x=750,y=225)
    
    l4=Label(frame2,text='Quantity',font=("times new roman",18,"bold"),fg="white",bg="#074463").grid(row=3, column=10, padx=0, pady=25)#.place(x=600,y=250)
    e4=Entry(frame2,textvariable=new_qunt ,bd=5,width=35).grid(row=3, column=50, padx=0, pady=0)#.place(x=750,y=250)
 
    l5=Label(frame2,text='Price',font=("times new roman",18,"bold"),fg="white",bg="#074463").grid(row=4, column=10, padx=0, pady=25)#.place(x=600,y=275)
    e5=Entry(frame2,textvariable=new_price, bd=5,width=35).grid(row=4, column=50, padx=0, pady=0)#.place(x=750,y=275)
   
    l6=Label(frame2,text='GST',font=("times new roman",18,"bold"),fg="white",bg="#074463").grid(row=5, column=10, padx=0, pady=25)#.place(x=600,y=300)
    e6=Entry(frame2,textvariable=new_gst, bd=5,width=35).grid(row=5, column=50, padx=0, pady=0)#.place(x=750,y=300)
    but_1=Button(frame2, text='Submit', width=12, bg='brown', fg='white',command=add_item).grid(row=6, column=15, padx=0, pady=10)#.place(x=700, y=500)







    
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

 
    
def open_win2():
    wi=Toplevel(win)
    wi.geometry('1600x1500')
    wi.title("Update Item")
    frame2=LabelFrame(wi, bd=10,text='Update Item',relief=GROOVE, bg="#074463",font=("times new roman",15,"bold"),fg="yellow")
    frame2.place(x=200, y=100, width=1000, height=500)
    #label_1=Label(frame2,text='Update item', relief="solid", font=('arial',12,'bold')).grid(row=0, column=0, padx=400, pady=10,columnspan=25)#.place(x=725,y=100)

    data=take_items_from_database()
    l2=Label(frame2,text='Product ID',font=("times new roman",18,"bold"),fg="white",bg="#074463").grid(row=1, column=0, padx=(260,0), pady=25,sticky="w")#.place(x=600,y=200)
    e2=Entry(frame2, bd=5,width=35,state='readonly',textvariable=update_id).grid(row=1, column=1, padx=20, pady=0)#.place(x=780,y=200)
    
    l3=Label(frame2,text='Product Name',font=("times new roman",18,"bold"),fg="white",bg="#074463").grid(row=2, column=0, padx=(260,0), pady=25,sticky="w")#.place(x=600,y=225)
    #e3=Entry(frame2, bd=5,width=35).grid(row=2, column=1, padx=0, pady=0)#.place(x=780,y=225)
    combobox = ttk.Combobox(frame2, values=data,textvariable=update_item_new,width=18,font=( 'aria' ,14, 'bold' ))
    combobox.grid(row=2, column=1, padx=0, pady=0)
    
    l4=Label(frame2,text='Gst',font=("times new roman",18,"bold"),fg="white",bg="#074463").grid(row=3, column=0, padx=(260,0), pady=25,sticky="w")#.place(x=600,y=250)
    e4=Entry(frame2, bd=5,width=35,textvariable=update_gst).grid(row=3, column=1, padx=0, pady=0)#.place(x=780,y=250)
 
    l5=Label(frame2,text='Rate',font=("times new roman",18,"bold"),fg="white",bg="#074463").grid(row=4, column=0, padx=(260,0), pady=25,sticky="w")#.place(x=600,y=275)
    e5=Entry(frame2, bd=5,width=35,textvariable=update_price).grid(row=4, column=1, padx=0, pady=0)#.place(x=780,y=275)

    but_1=Button(frame2, text='Update', width=12, bg='brown', fg='white',command=now_final_update).grid(row=5, column=0, padx=(300,0), pady=25)#.place(x=150, y=400)
    but_2=Button(frame2, text='Search', width=12, bg='brown',command=search_update, fg='white').grid(row=5, column=1, padx=0, pady=25)#.place(x=800, y=500)






"""
#=============================================================new
canvas = Canvas(win,  height=800, width=1350)
image = ImageTk.PhotoImage(Image.open("C:/Users/Krishna/Desktop/c1.png"))
image2 = ImageTk.PhotoImage(Image.open("C:/Users/Krishna/Desktop/pppp.png"))

canvas.create_image(5,0, anchor=NW, image=image)
canvas.create_image(800,150, anchor=NW, image=image2)
canvas.grid()    


#==========================================================new end
"""


#database=""
database=""
#########    ALL    VARIABLE    ##############################################
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
data_base=tk.StringVar()

cal_price=tk.DoubleVar()

cal_gst=tk.DoubleVar()

cal_amt=tk.DoubleVar()

cal_item=tk.StringVar()

cal_qut=tk.DoubleVar()

cal_id=tk.IntVar()

global datalist

global bill


global d

global bill_list

bill_list=[]

datalist=[]

Add_item=tk.StringVar()

price=tk.DoubleVar()

create_new_data=tk.StringVar()

getdatabase=""

d=""

yes=0

global l

l=[]
global total_bill_rate

total_bill_rate=0

customer=tk.StringVar()

phone=tk.StringVar()

new_item=tk.StringVar()

new_price=tk.DoubleVar()

new_gst=tk.DoubleVar()

new_qunt=tk.DoubleVar()

new_id=tk.IntVar()



update_item_new=tk.StringVar()
update_name=tk.StringVar()
update_id=tk.IntVar()
update_gst=tk.DoubleVar()
update_quantity=tk.DoubleVar()
update_price=tk.DoubleVar()


#delete variable are here
item_to_be_delete=tk.StringVar()
#max sales item variabnle
max_item_sales=tk.StringVar()
max_quantity_sales=tk.DoubleVar()








#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def removewin():
    global win
    for widget in win.winfo_children():
        widget.grid_remove()
        
def loginpage():

#================================================================================
    """
    F =Frame(canvas, highlightbackground="black", highlightcolor="black", highlightthickness=1,bd=20,bg="green")
    F.place(x=100, y=50, width=600,height=700)
    text1=tk.Label(F,text="Hello , Friends!",font=("Arial Bold", 30),bg="green",fg="white").place(x=160,y=150)
    text2=tk.Label(F,text="Fill up personal information and",font=("Arial Bold", 28),bg="green",fg="white").place(x=0,y=250)
    text3=tk.Label(F,text="Start journey with us.",font=("Arial Bold", 30),bg="green",fg="white").place(x=100,y=350)
    """
#==================================================================================================
    
    
    #top1=Toplevel()
    win.minsize(1350,2000)
    user=tk.StringVar()
    password=tk.StringVar()


    
    #border=tk.Canvas(win,width=1000,height=1000)
    admin=tk.Label(win,text="Admin_login",font=("Arial Bold", 38))
    admin.grid(row=0,column=0, columnspan=1,pady=(0,0),padx=(70,0))
    
    username=tk.Label(win,text="Username",font=("Arial Bold", 18))
    username.grid(row=1,column=0,pady=(100,0),padx=(30,0))
    enter_user=ttk.Entry(win,textvariable=user)
    enter_user.grid(row=1,column=1,pady=(100,0),padx=(30,0))
    
    pasword=tk.Label(win,text="Password",font=("Arial Bold", 18))
    pasword.grid(row=2,column=0,pady=(10,0),padx=(30,0))
    enter_pass=ttk.Entry(win,textvariable=password,show="*")
    enter_pass.grid(row=2,column=1,pady=(10,0),padx=(30,0))

    """
    enter_user=ttk.Entry(canvas,textvariable=user).place(x=710,y=500,width=490,height=30)
    enter_pass=ttk.Entry(canvas,textvariable=password,show="*").place(x=710,y=610,width=490,height=30)
    """
    
    def login():
        us=user.get()
        ps=password.get()
        if us=="admin" and ps =="admin":
            removewin()
            select_data_base_window()
        else:
            tk.messagebox.showerror("ERROR","invalid user or password")

            
    logbtn=ttk.Button(win,text="Login",command=login)
    logbtn.grid(row=3,column=0,pady=(10,0),padx=(60,0))
   

"""
#===============================================================new
    logbtn=ttk.Button(canvas,text="Login",command=login).place(x=710,y=691,width=490,height=63)
#=============================================================new end

"""
    
def dada_base_info():
    global d
    d=data_base.get()
    if d=="":
        tk.messagebox.showerror("warning","select database")
    else:
        #datalist.append(d)
        #database=data.get()
       ## conn=sqlite3.connect(database+ext)
       # cur=conn.cursor()
        #if d not in dalalist:
          #  pass
            
        main_task()
#-------------------------------------------------------------------------------------------------------------------------------------------------        
def take_items_from_database():
    global datalist
    global d
    datalist=[]
    ext=".db"
    conn=sqlite3.connect(d+ext)
    cur=conn.cursor()
    sql=""" SELECT itemname FROM item"""
    cur.execute(sql)
    find=cur.fetchall()
    for i in find:
        datalist.extend(i)

    return datalist



        
#---------------------------------------------------------------------------------------------------------------------------------------------------


        
def calculate_bill():
    global d
    global cal_item
    global cal_qut
    global cal_gst
    global l
    global bill
    global bill_list
    global show_sales
    ext=".db"
    conn=sqlite3.connect(d+ext)
    cur=conn.cursor()
    getitem=cal_item.get()
    q=float(cal_qut.get())
    #print(getitem,q)
    if getitem !=""and q!=0:
        
        
        
        cur.execute('SELECT id, price,gst FROM item WHERE itemname=?',(getitem,))
        
        acorrding_item=cur.fetchone()
        
        gst=float(acorrding_item[2])
        single_gst=gst
        #print(acorrding_item,gst)
        gst=gst*q
    
        amount=acorrding_item[1]
        amount=amount*q
        addgst=(amount*gst)/100
        amount=amount+addgst

    
        cal_price.set(amount)
        
        cal_id.set(acorrding_item[0])
        
        cal_gst.set(gst)
        
        l=[]
        
        a=cal_price.get()
        global total_bill_rate
        total_bill_rate=total_bill_rate+a
        
        b=cal_item.get()
        
        c=cal_gst.get()
        
        date=datetime.date.today()
        
        customer_name=customer.get()
        
        pho=phone.get()
        
        bill_list=cal_item.get(),cal_gst.get(),cal_price.get()
        #=========
        detail=[customer_name,pho]
        
        cur.execute('INSERT INTO daleysales(date,customername,itemname,totalquantity,totalprice,totalgst)VALUES(?,?,?,?,?,?)',(date,customer_name,b,q,a,c))
        
        conn.commit()
        global one_time_check
        
        if one_time_check==0:
            one_time_check_coutomer_details(customer_name,pho)
            one_time_check=1
            
        
        if yes==0:
            
            #bill.insert(END,detail,'\n')
            bill.insert(END,f"\n{ cal_item.get()},\t{q},\t\t{single_gst},\t{cal_gst.get()},\t{cal_price.get()}")
        
        
        
    
    else:
        tk.messagebox.showerror('Warning','fill qty or itm')
    

def description():
    global d
    ext=".db"
    conn=sqlite3.connect(d+ext)
    cur=conn.cursor()
    getdata=cal_item
    if getdata!="":
        pass
        
#===================================================================================================================================================
    

def select_data_base_window():
    win.minsize(1350,2000)
    newbutton=tk.Button(win,text="New",font=("Arial Bold", 18),height=2,width=4,command=new_database)
    newbutton.grid(row=0,column=0,padx=1200,pady=10)
    frame1=tk.Label(win,bd=10,bg="goldenrod")
    frame1.place(x=400,y=60,height=500,width=500)
    datainfo=tk.Label(frame1,text="SELECT  YOUR  DATA_BASE", bg='DarkSeaGreen4', font=("Arial Bold", 24))
    datainfo.grid(row=0,column=0,padx=10,pady=3)
    data=ttk.Combobox(frame1,width=20,textvariable=data_base,font=("Arial Bold", 18))
    data["values"]=datalist
    data.grid(row=1,column=0,padx=20,pady=40)
    button=tk.Button(frame1,text="process",font=("Arial Bold", 18),command=dada_base_info)
    button.grid(row=2,column=0,padx=10,pady=10)
    info=tk.Label(frame1,text="Welcome Users", bg='DarkSeaGreen4', font=("Arial Bold", 24), width=15,height=5)
    info.grid(row=3,column=0,padx=10,pady=10)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
def new_database():
    call_new()
    
def call_new():
    top=Toplevel(win,bg="medium spring green")
    top.minsize(1350,2000)
    frame2=Frame(top,bd=20,bg="lemon chiffon")
    frame2.place(x=200,y=100,width=1000,height=1000)
    name=tk.Label(frame2,text="Create your NewDataBase",font=("Arial Bold",28),width=25,height=3,bg="steel blue")
    name.grid(row=0,column=0,padx=230,pady=10)
    data_enter=ttk.Entry(frame2,width=25,textvariable=data_base,font=("Arial Bold", 18))
    data_enter.grid(row=1,column=0,pady=10)
    databas=tk.Button(frame2,text="create DataBase",font=("Arial Bold", 24),command=create)
    databas.grid(row=2,column=0,columnspan=1)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------    
    
    
def one_time_check_coutomer_details(customer_name,pho):
    bill.delete('1.0',END)
    bill.insert(END,"\t Welcome My Shop")
    #bill.insert(END,f"\n Bill number: {bill_no.get()}")
    bill.insert(END,f"\n Customer name: {customer_name}")
    bill.insert(END,f"\n Phone number: {pho}")
    bill.insert(END,f"\n==================================================")
    bill.insert(END,f"\n Products|\tQty|\tGST/kg(item)|\tTotal %GST|\tPrice")
    bill.insert(END,f"\n==================================================")
















    
    
def mainwindow():
    
    #win=tk.Tk()
    top=Toplevel(win)
    top.minsize(1350,2000)
    border=tk.Canvas(top,width=1000,height=1000)
    border.pack()
    frame1=tk.Frame(top,bd=10,bg="crimson")
    frame1.place(x=0,y=0,width=1000,height=100)
    frame2=tk.Frame(top,bd=10,bg="")
    frame2.place(x=0,y=100,width=500,height=1000)

    data=tk.StringVar()
    data_enter=ttk.Entry(frame1,width=25,textvariable=data,font=("Arial Bold", 18))
    data_enter.grid(row=1,column=2)
    
#'''def ck():
    
   # database=data.get()
    #ext=".db"
    #conn=sqlite3.connect(database+ext)
    #cur=conn.cursor()
    #print(database)'''
    item=tkinter.Label(frame2,text='Item name',font=("Arial Bold", 18))
    item.grid(row=0,column=0)
    tmenter=tk.StringVar()

    item_enter=tk.Entry(frame2,textvariable=tmenter,bd=10)
    item_enter.grid(row=0,column=5)

    line=tkinter.Label(frame2)
    line.grid(row=2,column=0)

    price=tkinter.Label(frame2,text='Price         ',font=("Arial Bold", 18))
    price.grid(row=3,column=0)

    penter=tk.StringVar()

    price_enter=tk.Entry(frame2,textvariable=penter,bd=10)
    price_enter.grid(row=3,column=5)

    line=tkinter.Label(frame2)
    line.grid(row=4,column=0)


    brand=tkinter.Label(frame2,text='brand          ',font=("Arial Bold", 18))
    brand.grid(row=5,column=0)

    benter=tk.StringVar()
    i=data_base.get()

    

    benter.set(i)

    brand_enter=tk.Entry(frame2,text=benter,bd=10)
    brand_enter.grid(row=5,column=5)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
def create():
    global d
    d=data_base.get()
    if d!="":
        try:
            
            ext=".db"
            conn=sqlite3.connect(d+ext)
            cur=conn.cursor()
            table1="""CREATE TABLE item(id int PRIMARY KEY ,itemname char UNIQUE ,price float, gst float,quantity float,date )"""
            cur.execute(table1)
            #if checkl!=True:
                
            #ans=tk.messagebox.showerror('warning','SOMETHING WRONG')

                
            table2="""CREATE TABLE daleysales(date,customername char,itemname,totalquantity,totalprice float,totalgst float)"""
            check2=cur.execute(table2)
            #if check2!=True:
                
            ##ans=tk.messagebox.showerror('warning','SOMETHING WRONG')
            main_task()        
        except Exception as e:
             
             tk.messagebox.showerror("Warning","database already exist")

    else:
        ans=tk.messagebox.showerror('warning','YOU have fill the option')
            
    #take_items_from_database()
   # databas=tk.Button(frame1,text="create DataBase",font=("Arial Bold", 24),command=create)
    #databas.grid(row=1,column=0,columnspan=1)
     #

     #database2=tk.Button(frame1,text="create DataBase",font=("Arial Bold", 24),command=ck)
     #database2.grid(row=1,column=3,columnspan=3)
    
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++






def main_task():
    global bill
    wi=Toplevel(win)
    wi.geometry('1360x1500')
    Frame3 =Frame(wi, bd=10,relief=GROOVE, bg="#074463")
    Frame3.place(x=0, y=0, width=1600,height=80)
    but_1=Button(Frame3, text='Add item', width=12, bg='brown', fg='white', command=open_win).grid(row=0, column=0, padx=10,pady=10)
    but_2=Button(Frame3, text='Update item', width=12, bg='brown', fg='white', command=open_win2).grid(row=0, column=1, padx=10,pady=10)
    but_3=Button(Frame3, text='Delete item', width=20, bg='brown', fg='white', command=open_win3).grid(row=0, column=2, padx=10,pady=10)
    but_4=Button(Frame3, text='Sales as per day', width=20, bg='brown', fg='white', command=open_win4).grid(row=0, column=3, padx=10,pady=10)
    but_5=Button(Frame3, text='Maximum Sales', width=20, bg='brown', fg='white', command=open_win5).grid(row=0, column=4, padx=10,pady=10)

    try:
        
        take_items_from_database()
    except :
        tk.messagebox.showerror("error","something wrong")

    Frame4 =Frame(wi, bd=10,relief=GROOVE, bg="#074463")
    Frame4.place(x=0, y=60, width=1600,height=80)
    lbl = Label(Frame4, font=( 'aria' ,28, 'bold' ),text="BILLING SYSTEM",bd=5,fg="white",bg="#074463")
    lbl.grid(row=0,column=0,padx=500)


    Frame1 = LabelFrame(wi,bd=10,relief=GROOVE,text="Customer Details", font=("times new roman",15,"bold"),fg="yellow", bg="#074463")
    Frame1.place(x=0, y=140, width=900,height=500)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #new
    lbl = Label(Frame1, font=( "times new roman",18,"bold" ),text="Customer Name",fg="white",bg="#074463")
    lbl.grid(row=0,column=0,padx=20, pady=5,sticky="w")
    txt = Entry(Frame1,font="arial",bd=7,relief=SUNKEN,textvariable=customer,width=15)
    txt.grid(row=0,column=1,padx=0,pady=5, sticky="w")
    global l
    l=[9,9,9,9,]

    lbl=Label(Frame1,text='Phone no.',font=("times new roman",18,"bold"),fg="white",bg="#074463")
    lbl.grid(row=0,column=2,padx=0, pady=5,sticky="w")
    txt = Entry(Frame1,font="arial",bd=7,relief=SUNKEN,textvariable=phone,width=15)
    txt.grid(row=0,column=3,padx=10,pady=5)
    
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


    lbl= Label(Frame1, font=("times new roman",18,"bold"),text="Item name",fg="white",bg="#074463")
    lbl.grid(row=1,column=0,padx=20, pady=50,sticky="w")
    combobox = ttk.Combobox(Frame1, values=datalist,textvariable=cal_item ,width=12,state="readonly",font=( 'aria' ,14, 'bold' ))
    combobox.grid(row=1,column=1,padx=0,pady=50,sticky="w")

    lbl = Label(Frame1, font=("times new roman",18,"bold"),text="Quantity",fg="white",bg="#074463")
    lbl.grid(row=1,column=2,padx=0,pady=50,sticky="w")
    combobox = tk.Entry(Frame1, textvariable=cal_qut,width=15,font="arial",bd=7,relief=SUNKEN)
    combobox.grid(row=1,column=3,padx=10,pady=50)


    lbl = Label(Frame1, font=("times new roman",18,"bold"),text="Gst",fg="white",bg="#074463")
    lbl.grid(row=2,column=0,padx=20, pady=40,sticky="w")
    txt = Entry(Frame1,font="arial",bd=7,relief=SUNKEN,textvariable=cal_gst,width=15,state="readonly")
    txt.grid(row=2,column=1,padx=0,pady=40,sticky="w")

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#new
    lbl=Label(Frame1,text='Price',font=("times new roman",18,"bold"),fg="white",bg="#074463")
    lbl.grid(row=2,column=2,padx=0, pady=40,sticky="w")
    txt = Entry(Frame1,font="arial",bd=7,relief=SUNKEN,textvariable=cal_price,state="readonly",width=15)
    txt.grid(row=2,column=3,padx=10,pady=40)

    but_1=Button(Frame1, text='Enter',command=calculate_bill, width=14,font=( 'aria' ,16, 'bold' ), bg='brown', fg='white').grid(row=50, column=1, padx=(150,0),pady=20, sticky="w")
    #box = Listbox(Frame1, width=146, height=5).place(x=0,y=380)
    

    
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++    
    #but_1=Button(Frame1, text='Enter', width=14,font=( 'aria' ,16, 'bold' ), bg='brown', fg='white',command=calculate_bill).grid(row=60, column=3, padx=1, pady=50)


    Frame2 = Frame(wi, bd=10,relief=GROOVE, bg="#074463")
    Frame2.place(x=927, y=140, height=500, width=430)

   # recipts = Listbox(Frame2, width=60, height=20)
    
    #recipts.grid(row=0, column=0, padx=10)#.place(x=40, y=50)

    #recipts.insert('end',l)
    bill=Text(Frame2,width=50, height=20)
    bill.grid(row=0, column=0, padx=2)
    
    #but_1=Button(Frame2, text='Enter',command=calculate_bill, width=14,font=( 'aria' ,16, 'bold' ), bg='brown', fg='white').grid(row=50, column=0, padx=10,pady=20)
    but_1=Button(Frame2, text='Print',command=iPrint, width=14,font=( 'aria' ,16, 'bold' ), bg='brown', fg='white').grid(row=60, column=0, padx=10,pady=20)
    


    Frame5 = Frame(wi, bd=10,relief=GROOVE, bg="#074463")
    Frame5.place(x=0, y=640, width=1600,height=80)
    lbl = Label(Frame5, font=( 'Monotype Corsiva' ,14, 'bold' ),text='designed by UNICO Team',fg="white",bg="#074463")
    lbl.grid(row=0,column=0,padx=550,pady=15)

    











    
   
#=================================================================================================================================================================    

def open_win():
    wi=Toplevel(win)
    wi.geometry('1600x1500')
    frame2=LabelFrame(wi, bd=10,text='Add Product Details',relief=GROOVE, bg="#074463",font=("times new roman",15,"bold"),fg="yellow")
    frame2.place(x=200, y=100, width=1000, height=500)
    wi.title("Add Product Details")
    l2=Label(frame2,text='Product ID',font=("times new roman",18,"bold"),fg="white",bg="#074463").grid(row=1, column=10, padx=150, pady=25)#.place(x=600,y=200)
    e2=Entry(frame2,textvariable=new_id, bd=5,width=35).grid(row=1, column=50, padx=0, pady=0)#.place(x=750,y=200)
    
    l3=Label(frame2,text='Product Name',font=("times new roman",18,"bold"),fg="white",bg="#074463").grid(row=2, column=10, padx=0, pady=25)#.place(x=600,y=225)
    e3=Entry(frame2, textvariable=new_item,bd=5,width=35).grid(row=2, column=50, padx=0, pady=0)#.place(x=750,y=225)
    
    l4=Label(frame2,text='Quantity',font=("times new roman",18,"bold"),fg="white",bg="#074463").grid(row=3, column=10, padx=0, pady=25)#.place(x=600,y=250)
    e4=Entry(frame2,textvariable=new_qunt ,bd=5,width=35).grid(row=3, column=50, padx=0, pady=0)#.place(x=750,y=250)
 
    l5=Label(frame2,text='Price',font=("times new roman",18,"bold"),fg="white",bg="#074463").grid(row=4, column=10, padx=0, pady=25)#.place(x=600,y=275)
    e5=Entry(frame2,textvariable=new_price, bd=5,width=35).grid(row=4, column=50, padx=0, pady=0)#.place(x=750,y=275)
   
    l6=Label(frame2,text='GST',font=("times new roman",18,"bold"),fg="white",bg="#074463").grid(row=5, column=10, padx=0, pady=25)#.place(x=600,y=300)
    e6=Entry(frame2,textvariable=new_gst, bd=5,width=35).grid(row=5, column=50, padx=0, pady=0)#.place(x=750,y=300)
    but_1=Button(frame2, text='Submit', width=12, bg='brown', fg='white',command=add_item).grid(row=6, column=15, padx=0, pady=10)#.place(x=700, y=500)







    
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

 
    
def open_win2():
    wi=Toplevel(win)
    wi.geometry('1600x1500')
    wi.title("Update Item")
    frame2=LabelFrame(wi, bd=10,text='Update Item',relief=GROOVE, bg="#074463",font=("times new roman",15,"bold"),fg="yellow")
    frame2.place(x=200, y=100, width=1000, height=500)
    #label_1=Label(frame2,text='Update item', relief="solid", font=('arial',12,'bold')).grid(row=0, column=0, padx=400, pady=10,columnspan=25)#.place(x=725,y=100)

    data=take_items_from_database()
    l2=Label(frame2,text='Product ID',font=("times new roman",18,"bold"),fg="white",bg="#074463").grid(row=1, column=0, padx=(260,0), pady=25,sticky="w")#.place(x=600,y=200)
    e2=Entry(frame2, bd=5,width=35,state='readonly',textvariable=update_id).grid(row=1, column=1, padx=20, pady=0)#.place(x=780,y=200)
    
    l3=Label(frame2,text='Product Name',font=("times new roman",18,"bold"),fg="white",bg="#074463").grid(row=2, column=0, padx=(260,0), pady=25,sticky="w")#.place(x=600,y=225)
    #e3=Entry(frame2, bd=5,width=35).grid(row=2, column=1, padx=0, pady=0)#.place(x=780,y=225)
    combobox = ttk.Combobox(frame2, values=data,textvariable=update_item_new,width=18,font=( 'aria' ,14, 'bold' ))
    combobox.grid(row=2, column=1, padx=0, pady=0)
    
    l4=Label(frame2,text='Gst',font=("times new roman",18,"bold"),fg="white",bg="#074463").grid(row=3, column=0, padx=(260,0), pady=25,sticky="w")#.place(x=600,y=250)
    e4=Entry(frame2, bd=5,width=35,textvariable=update_gst).grid(row=3, column=1, padx=0, pady=0)#.place(x=780,y=250)
 
    l5=Label(frame2,text='Rate',font=("times new roman",18,"bold"),fg="white",bg="#074463").grid(row=4, column=0, padx=(260,0), pady=25,sticky="w")#.place(x=600,y=275)
    e5=Entry(frame2, bd=5,width=35,textvariable=update_price).grid(row=4, column=1, padx=0, pady=0)#.place(x=780,y=275)

    but_1=Button(frame2, text='Update', width=12, bg='brown', fg='white',command=now_final_update).grid(row=5, column=0, padx=(300,0), pady=25)#.place(x=150, y=400)
    but_2=Button(frame2, text='Search', width=12, bg='brown',command=search_update, fg='white').grid(row=5, column=1, padx=0, pady=25)#.place(x=800, y=500)























    
#======================================================================================================================================================================
def open_win3():
    wi=Toplevel(win)
    wi.geometry('1600x1500')
    wi.title("Delete")
    frame2=LabelFrame(wi, bd=10,text='Delete Item',relief=GROOVE, bg="#074463",font=("times new roman",15,"bold"),fg="yellow")
    frame2.place(x=200, y=100, width=1000, height=500)
    #label_1=Label(frame2,text='Update item', relief="solid", font=('arial',12,'bold')).grid(row=0, column=0, padx=400, pady=10,columnspan=25)#.place(x=725,y=100)
    delete=take_items_from_database()
    
    l2=Label(frame2,text='Product ID',font=("times new roman",18,"bold"),fg="white",bg="#074463").grid(row=1, column=0, padx=(200,0), pady=25,sticky="w")#.place(x=600,y=200)
    e2=Entry(frame2, bd=5,width=35).grid(row=1, column=1, padx=0, pady=0)#.place(x=780,y=200)
    
    l3=Label(frame2,text='Product Name',font=("times new roman",18,"bold"),fg="white",bg="#074463").grid(row=2, column=0, padx=(200,0), pady=25,sticky="w")#.place(x=600,y=225)
    e3=ttk.Combobox(frame2,values=delete,textvariable=item_to_be_delete,width=34)
    e3.grid(row=2, column=1, padx=0, pady=0)#.place(x=780,y=225)
    
    l4=Label(frame2,text='Quantity Available',font=("times new roman",18,"bold"),fg="white",bg="#074463").grid(row=3, column=0, padx=(200,0), pady=25,sticky="w")#.place(x=600,y=250)
    e4=Entry(frame2, bd=5,width=35).grid(row=3, column=1, padx=0, pady=0)#.place(x=780,y=250)
 
    l5=Label(frame2,text='Quantity Purchased',font=("times new roman",18,"bold"),fg="white",bg="#074463").grid(row=4, column=0, padx=(200,0), pady=25,sticky="w")#.place(x=600,y=275)
    e5=Entry(frame2, bd=5,width=35).grid(row=4, column=1, padx=0, pady=0)#.place(x=780,y=275)

    but_1=Button(frame2, text='Delete', width=12, bg='brown', fg='white',command=delete_item).grid(row=6, column=0, padx=(390,0), pady=50)#.place(x=700, y=500)


def open_win5():
    wi=Toplevel(win)
    wi.geometry('1600x1500')
    
    frame2=LabelFrame(wi, bd=10,text='Maximum Sales ',relief=GROOVE, bg="#074463",font=("times new roman",15,"bold"),fg="yellow")
    frame2.place(x=200, y=100, width=1000, height=500)
    wi.title("Maximum Sales")
    
    l2=Label(frame2,text='Maximum Sale Items',font=("times new roman",18,"bold"),fg="white",bg="#074463").grid(row=1, column=0, padx=0, pady=(100,0))#.place(x=600,y=200)
    e2=Entry(frame2, bd=5,width=35,textvariable=max_item_sales).grid(row=1, column=50, padx=0, pady=(100,0))#.place(x=750,y=200)
    
    l3=Label(frame2,text='Maximum Sales Quantity',font=("times new roman",18,"bold"),fg="white",bg="#074463").grid(row=2, column=0, padx=0,pady=(100,0))#.place(x=600,y=225)
    e3=Entry(frame2,bd=5,width=35,textvariable=max_quantity_sales).grid(row=2, column=50, padx=0, pady=(100,0))#.place(x=750,y=225)
    maxitem_sales_current_date()
   # but_1=Button(frame2, text='Check', width=12, bg='brown', fg='white').grid(row=6, column=0, padx=(450,0), pady=100,sticky="w")#.place(x=700, y=500)

























    
#==================================================================================================================================================================
def open_win4():
    global show_sales
    wi=Toplevel(win)
    wi.geometry('1600x1500')
    wi.title("Sales as per day")
    frame2=LabelFrame(wi, bd=10,text='Sales as per day',relief=GROOVE, bg="#074463",font=("times new roman",15,"bold"),fg="yellow")
    frame2.place(x=200, y=100, width=1000, height=500)
    l3=Label(frame2,text='Date',font=("times new roman",18,"bold"),fg="white",bg="#074463").grid(row=0, column=0, padx=88, pady=30,sticky="w")#.place(x=400,y=200)
    combobox = ttk.Combobox(frame2, values=["", "", "",""]).grid(row=0, column=0, padx=150, pady=30,sticky="w")
    l4=Label(frame2,text='Month',font=("times new roman",18,"bold"),fg="white",bg="#074463").grid(row=0, column=0, padx=400, pady=30,sticky="w")#.place(x=800,y=200)
    combobox = ttk.Combobox(frame2, values=["", "", "",""]).grid(row=0, column=0, padx=(480,0), pady=30,sticky="w")
    l5=Label(frame2,text='Year',font=("times new roman",18,"bold"),fg="white",bg="#074463").grid(row=0, column=0, padx=(680,0), pady=30,sticky="w")#.place(x=800,y=200)
    combobox = ttk.Combobox(frame2, values=["", "", "",""]).grid(row=0, column=0, padx=(750,0), pady=30,sticky="w")

    f=Frame(frame2,bd=10, relief=GROOVE)
    f.place(x=50, y=100,width=900, height=280)
    scrol_y=Scrollbar(f,orient=VERTICAL)
    show_sales=Text(f,yscrollcommand=scrol_y.set)
    scrol_y.pack(side=RIGHT, fill=Y)
    scrol_y.config(command=show_sales.yview)
    show_sales.pack(fill=BOTH,expand=1)
                
    #show_sales = Text(frame2, width=120,height=15)
    #show_sales.grid(row=3, column=0, padx=5, pady=30)#.place(x=360, y=300)
    but_1=Button(frame2, text='Check', width=12, bg='brown', fg='white').grid(row=4, column=0, padx=0, pady=320)#.place(x=700, y=500)
    
    seles_daley()
    
  
    


def add_item():
    ext=".db"
    global d
    conn=sqlite3.connect(d+ext)
    cur=conn.cursor()
    price=new_price.get()
    Id=new_id.get()
    item=new_item.get()
    gst=new_gst.get()
    qunt=new_qunt.get()
    date="2020"
    if item!="" and Id!="" and price!="" and qunt!="" and gst!="":
        
        
        #print(d)
        try:
            
            
            cur.execute('INSERT INTO item(id,itemname,price,gst,quantity,date)VALUES(?,?,?,?,?,?)',(Id,item,price,gst,qunt,date))
            conn.commit()
            #conn.close()
            take_items_from_database()
        except Exception as  e:
            tk.messagebox.showinfo('Warning',e)

        else:
            tk.messagebox.showinfo('Information','your data insert successfully : thank you')
        finally:
            open_win()
        
            
        #tk.messagebox.showerror('Error','you have an Error  at time add new item')
            
    else:
        tk.messagebox.showerror('Warning','you have to fill all option')
        open_win()
            
          
    

def delete_item():
    global d
    ext=".db"
    conn=sqlite3.connect(d+ext)
    cur=conn.cursor()
    be_delete=item_to_be_delete.get()
    try:
        
        
        cur.execute('delete from item where itemname=?',(be_delete,))
        conn.commit()
        
    except Exception as e:
        tk.messagebox.showerror('Warning',e)
    else:
        tk.messagebox.showinfo('information','item deleted succusfully')
    finally:
        
        #take_items_from_database()
        open_win3()







def seles_daley():
    ext=".db"
    conn=sqlite3.connect(d+ext)
    cur=conn.cursor()
    date=datetime.date.today()
    res=cur.execute("SELECT *FROM daleysales WHERE date=?",(date,))
    show_sales.delete('1.0',END)
    show_sales.insert(END,"\t\t\t\t\t\t\t\t\t Welcome My Shop")
    #bill.insert(END,f"\n Bill number: {bill_no.get()}")
    #show_sales.insert(END,f"\n Customer name: {customer_name}")
    #show_sales.insert(END,f"\n Phone number: {pho}")
    show_sales.insert(END,f"\n================================================================================================================")
    show_sales.insert(END,f"\n DATE|\t\t Customer name|\t\tItem name|\t\t Quantity|\t\tPrice|\t\t total GST")
    show_sales.insert(END,f"\n=======================================================================================================================")
    for i in res:
        show_sales.insert(END,f"\n{i[0]}\t\t{i[1]}\t\t{i[2]}\t\t{i[3]}\t\t{i[4]}\t\t{i[5]}")
        #print(i)
    
        
def iPrint():
    
      global total_bill_rate
      
      total="\n\n\ntotal bill ammont is ==   "
      
      print(total_bill_rate)
      q=bill.get("1.0", "end-1c")
      q=q+total+str(total_bill_rate)
      
      filename=tempfile.mktemp(".txt")
      open (filename ,"w"). write(q)
      os.startfile(filename, "print")
      global one_time_check
      one_time_check=0
      
   
      total_bill_rate=0
      



def search_update():
        
        global d
        i=update_item_new.get()
        
            
        ext=".db"
        conn=sqlite3.connect(d+ext)
        cur=conn.cursor()
        cur.execute('SELECT id,itemname,price,gst FROM item WHERE itemname=?',(i,))
        res=cur.fetchone()
        #print(res)
        update_id.set(res[0])
        update_name.set(res[1])
        update_price.set(res[2])
        update_gst.set(res[3])
        #update_quantity=res[4]
        #update_date=res[5]

        #except Exception as e:
        #print(e)
               
    
def now_final_update():
      global d  
      ext=".db"
      conn=sqlite3.connect(d+ext)
      cur=conn.cursor()
      a=int(update_id.get())
      b=str(update_name.get())
      c=float(update_price.get())
      s=float(update_gst.get())
      try:
          
          cur.execute('UPDATE item set itemname=?,price=?,gst=? WHERE id=?',(b,c,s,a))
          conn.commit()
      
          
      except Exception as e:
      #print(e)
          tk.messagebox.showinfo('warning',e)
      else:
          tk.messagebox.showinfo('Information','updated is successful')

      finally:
         take_items_from_database()
         open_win2()



def maxitem_sales_current_date():
    
    date=datetime.date.today()
    global d  
    ext=".db"
    conn=sqlite3.connect(d+ext)
    cur=conn.cursor()
    query="""SELECT itemname from daleysales WHERE date=?"""
    cur.execute(query,(date,))
    result=cur.fetchall()
    second(result)
def second(result):
    temp=0
    maxquantit=0
    result=list(result)
    date=datetime.date.today()
    global d  
    ext=".db"
    conn=sqlite3.connect(d+ext)
    cur=conn.cursor()
    for i in result:
        i=list(i)
        for j in i:
            query="""SELECT SUM(totalquantity) FROM daleysales WHERE itemname=? AND date=?"""
            cur.execute(query,(j,date))
            maxquantity=cur.fetchone()
            maxq=maxquantity
            for k in range(0,len(maxq)):
                total=float(maxq[k])
                if temp<total:
                    temp=total
                    max_item_sales.set(i)
                    max_quantity_sales.set(total)
    



#######################################################################################################################################################################







#open_win5()     
#mainwindow()
loginpage()
#select_data_base_window()     
#call_new()
#main_task()

win.mainloop()








    
#======================================================================================================================================================================
def open_win3():
    wi=Toplevel(win)
    wi.geometry('1600x1500')
    wi.title("Delete")
    frame2=LabelFrame(wi, bd=10,text='Delete Item',relief=GROOVE, bg="#074463",font=("times new roman",15,"bold"),fg="yellow")
    frame2.place(x=200, y=100, width=1000, height=500)
    #label_1=Label(frame2,text='Update item', relief="solid", font=('arial',12,'bold')).grid(row=0, column=0, padx=400, pady=10,columnspan=25)#.place(x=725,y=100)
    delete=take_items_from_database()
    
    l2=Label(frame2,text='Product ID',font=("times new roman",18,"bold"),fg="white",bg="#074463").grid(row=1, column=0, padx=(200,0), pady=25,sticky="w")#.place(x=600,y=200)
    e2=Entry(frame2, bd=5,width=35).grid(row=1, column=1, padx=0, pady=0)#.place(x=780,y=200)
    
    l3=Label(frame2,text='Product Name',font=("times new roman",18,"bold"),fg="white",bg="#074463").grid(row=2, column=0, padx=(200,0), pady=25,sticky="w")#.place(x=600,y=225)
    e3=ttk.Combobox(frame2,values=delete,textvariable=item_to_be_delete,width=34)
    e3.grid(row=2, column=1, padx=0, pady=0)#.place(x=780,y=225)
    
    l4=Label(frame2,text='Quantity Available',font=("times new roman",18,"bold"),fg="white",bg="#074463").grid(row=3, column=0, padx=(200,0), pady=25,sticky="w")#.place(x=600,y=250)
    e4=Entry(frame2, bd=5,width=35).grid(row=3, column=1, padx=0, pady=0)#.place(x=780,y=250)
 
    l5=Label(frame2,text='Quantity Purchased',font=("times new roman",18,"bold"),fg="white",bg="#074463").grid(row=4, column=0, padx=(200,0), pady=25,sticky="w")#.place(x=600,y=275)
    e5=Entry(frame2, bd=5,width=35).grid(row=4, column=1, padx=0, pady=0)#.place(x=780,y=275)

    but_1=Button(frame2, text='Delete', width=12, bg='brown', fg='white',command=delete_item).grid(row=6, column=0, padx=(390,0), pady=50)#.place(x=700, y=500)


def open_win5():
    wi=Toplevel(win)
    wi.geometry('1600x1500')
    
    frame2=LabelFrame(wi, bd=10,text='Maximum Sales ',relief=GROOVE, bg="#074463",font=("times new roman",15,"bold"),fg="yellow")
    frame2.place(x=200, y=100, width=1000, height=500)
    wi.title("Maximum Sales")
    
    l2=Label(frame2,text='Maximum Sale Items',font=("times new roman",18,"bold"),fg="white",bg="#074463").grid(row=1, column=0, padx=0, pady=(100,0))#.place(x=600,y=200)
    e2=Entry(frame2, bd=5,width=35,textvariable=max_item_sales).grid(row=1, column=50, padx=0, pady=(100,0))#.place(x=750,y=200)
    
    l3=Label(frame2,text='Maximum Sales Quantity',font=("times new roman",18,"bold"),fg="white",bg="#074463").grid(row=2, column=0, padx=0,pady=(100,0))#.place(x=600,y=225)
    e3=Entry(frame2,bd=5,width=35,textvariable=max_quantity_sales).grid(row=2, column=50, padx=0, pady=(100,0))#.place(x=750,y=225)
    maxitem_sales_current_date()
   # but_1=Button(frame2, text='Check', width=12, bg='brown', fg='white').grid(row=6, column=0, padx=(450,0), pady=100,sticky="w")#.place(x=700, y=500)

























    
#==================================================================================================================================================================
def open_win4():
    global show_sales
    wi=Toplevel(win)
    wi.geometry('1600x1500')
    wi.title("Sales as per day")
    frame2=LabelFrame(wi, bd=10,text='Sales as per day',relief=GROOVE, bg="#074463",font=("times new roman",15,"bold"),fg="yellow")
    frame2.place(x=200, y=100, width=1000, height=500)
    l3=Label(frame2,text='Date',font=("times new roman",18,"bold"),fg="white",bg="#074463").grid(row=0, column=0, padx=88, pady=30,sticky="w")#.place(x=400,y=200)
    combobox = ttk.Combobox(frame2, values=["", "", "",""]).grid(row=0, column=0, padx=150, pady=30,sticky="w")
    l4=Label(frame2,text='Month',font=("times new roman",18,"bold"),fg="white",bg="#074463").grid(row=0, column=0, padx=400, pady=30,sticky="w")#.place(x=800,y=200)
    combobox = ttk.Combobox(frame2, values=["", "", "",""]).grid(row=0, column=0, padx=(480,0), pady=30,sticky="w")
    l5=Label(frame2,text='Year',font=("times new roman",18,"bold"),fg="white",bg="#074463").grid(row=0, column=0, padx=(680,0), pady=30,sticky="w")#.place(x=800,y=200)
    combobox = ttk.Combobox(frame2, values=["", "", "",""]).grid(row=0, column=0, padx=(750,0), pady=30,sticky="w")

    f=Frame(frame2,bd=10, relief=GROOVE)
    f.place(x=50, y=100,width=900, height=280)
    scrol_y=Scrollbar(f,orient=VERTICAL)
    show_sales=Text(f,yscrollcommand=scrol_y.set)
    scrol_y.pack(side=RIGHT, fill=Y)
    scrol_y.config(command=show_sales.yview)
    show_sales.pack(fill=BOTH,expand=1)
                
    #show_sales = Text(frame2, width=120,height=15)
    #show_sales.grid(row=3, column=0, padx=5, pady=30)#.place(x=360, y=300)
    but_1=Button(frame2, text='Check', width=12, bg='brown', fg='white').grid(row=4, column=0, padx=0, pady=320)#.place(x=700, y=500)
    
    seles_daley()
    
  
    


def add_item():
    ext=".db"
    global d
    conn=sqlite3.connect(d+ext)
    cur=conn.cursor()
    price=new_price.get()
    Id=new_id.get()
    item=new_item.get()
    gst=new_gst.get()
    qunt=new_qunt.get()
    date="2020"
    if item!="" and Id!="" and price!="" and qunt!="" and gst!="":
        
        
        #print(d)
        try:
            
            
            cur.execute('INSERT INTO item(id,itemname,price,gst,quantity,date)VALUES(?,?,?,?,?,?)',(Id,item,price,gst,qunt,date))
            conn.commit()
            #conn.close()
            take_items_from_database()
        except Exception as  e:
            tk.messagebox.showinfo('Warning',e)

        else:
            tk.messagebox.showinfo('Information','your data insert successfully : thank you')
        finally:
            open_win()
        
            
        #tk.messagebox.showerror('Error','you have an Error  at time add new item')
            
    else:
        tk.messagebox.showerror('Warning','you have to fill all option')
        open_win()
            
          
    

def delete_item():
    global d
    ext=".db"
    conn=sqlite3.connect(d+ext)
    cur=conn.cursor()
    be_delete=item_to_be_delete.get()
    try:
        
        
        cur.execute('delete from item where itemname=?',(be_delete,))
        conn.commit()
        
    except Exception as e:
        tk.messagebox.showerror('Warning',e)
    else:
        tk.messagebox.showinfo('information','item deleted succusfully')
    finally:
        
        #take_items_from_database()
        open_win3()







def seles_daley():
    ext=".db"
    conn=sqlite3.connect(d+ext)
    cur=conn.cursor()
    date=datetime.date.today()
    res=cur.execute("SELECT *FROM daleysales WHERE date=?",(date,))
    show_sales.delete('1.0',END)
    show_sales.insert(END,"\t\t\t\t\t\t\t\t\t Welcome My Shop")
    #bill.insert(END,f"\n Bill number: {bill_no.get()}")
    #show_sales.insert(END,f"\n Customer name: {customer_name}")
    #show_sales.insert(END,f"\n Phone number: {pho}")
    show_sales.insert(END,f"\n================================================================================================================")
    show_sales.insert(END,f"\n DATE|\t\t Customer name|\t\tItem name|\t\t Quantity|\t\tPrice|\t\t total GST")
    show_sales.insert(END,f"\n=======================================================================================================================")
    for i in res:
        show_sales.insert(END,f"\n{i[0]}\t\t{i[1]}\t\t{i[2]}\t\t{i[3]}\t\t{i[4]}\t\t{i[5]}")
        #print(i)
    
        
def iPrint():
    
      global total_bill_rate
      
      total="\n\n\ntotal bill ammont is ==   "
      
      print(total_bill_rate)
      q=bill.get("1.0", "end-1c")
      q=q+total+str(total_bill_rate)
      
      filename=tempfile.mktemp(".txt")
      open (filename ,"w"). write(q)
      os.startfile(filename, "print")
      global one_time_check
      one_time_check=0
      
   
      total_bill_rate=0
      



def search_update():
        
        global d
        i=update_item_new.get()
        
            
        ext=".db"
        conn=sqlite3.connect(d+ext)
        cur=conn.cursor()
        cur.execute('SELECT id,itemname,price,gst FROM item WHERE itemname=?',(i,))
        res=cur.fetchone()
        #print(res)
        update_id.set(res[0])
        update_name.set(res[1])
        update_price.set(res[2])
        update_gst.set(res[3])
        #update_quantity=res[4]
        #update_date=res[5]

        #except Exception as e:
        #print(e)
               
    
def now_final_update():
      global d  
      ext=".db"
      conn=sqlite3.connect(d+ext)
      cur=conn.cursor()
      a=int(update_id.get())
      b=str(update_name.get())
      c=float(update_price.get())
      s=float(update_gst.get())
      try:
          
          cur.execute('UPDATE item set itemname=?,price=?,gst=? WHERE id=?',(b,c,s,a))
          conn.commit()
      
          
      except Exception as e:
      #print(e)
          tk.messagebox.showinfo('warning',e)
      else:
          tk.messagebox.showinfo('Information','updated is successful')

      finally:
         take_items_from_database()
         open_win2()



def maxitem_sales_current_date():
    
    date=datetime.date.today()
    global d  
    ext=".db"
    conn=sqlite3.connect(d+ext)
    cur=conn.cursor()
    query="""SELECT itemname from daleysales WHERE date=?"""
    cur.execute(query,(date,))
    result=cur.fetchall()
    second(result)
def second(result):
    temp=0
    maxquantit=0
    result=list(result)
    date=datetime.date.today()
    global d  
    ext=".db"
    conn=sqlite3.connect(d+ext)
    cur=conn.cursor()
    for i in result:
        i=list(i)
        for j in i:
            query="""SELECT SUM(totalquantity) FROM daleysales WHERE itemname=? AND date=?"""
            cur.execute(query,(j,date))
            maxquantity=cur.fetchone()
            maxq=maxquantity
            for k in range(0,len(maxq)):
                total=float(maxq[k])
                if temp<total:
                    temp=total
                    max_item_sales.set(i)
                    max_quantity_sales.set(total)
    



#######################################################################################################################################################################







#open_win5()     
#mainwindow()
loginpage()
#select_data_base_window()     
#call_new()
#main_task()

win.mainloop()
