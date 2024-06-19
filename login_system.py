from tkinter import *
from tkinter import messagebox


root=Tk()
root.title('Login System')
root.geometry('500x500')
root.resizable(False,False)
root.config(bg='#D5DBDB')
root.iconbitmap()#icon file.ico

#==========Define==========
show_photo=PhotoImage(file='show.png')
hide_photo=PhotoImage(file='hide.png')


def toggle_password():
    if entrypas.cget('show') == '':
        entrypas.config(show='*')
        
        toggle_btn.config(image=show_photo)
    else:
        entrypas.config(show='')
        
        toggle_btn.config(image=hide_photo)

def login():
    global username,password
    
    username='user'
    password='0000'
    
    
    if entryuser.get()==username and entrypas.get()==password:
        root.destroy()
        root1=Tk()
        root1.configure(bg='black')
        btnart=Button(text='START',fg='white',bg='#1976D2',width=20,height=5,bd=8).pack()
        root1.mainloop()
    elif entryuser.get()!=username and entrypas.get() == password:
        messagebox.showerror('Error','Username is incorrect')
    elif entrypas.get()!=password and entryuser.get()==username:
        messagebox.showerror('Error','Password is incorrect')
    
    else:
        messagebox.showerror("Error","Username and password is incorrect")
        entryuser.config(fg='red')
        entrypas.config(fg='red')
        #root.destroy()       

def login2():
    global phonenumber,username
    phonenumber='010'
    if entryuser.get()==username and entrypas.get()==phonenumber:
        messagebox.showinfo('Username & Password','username : '+username+'\n password : '+password )
        lblpas.config(text='Password')
        btnlog.config(command=lambda:login())
    else:
        messagebox.showerror('Error','The Number is Incorrect')

                                                

def forget():
    lblpas.config(text='Phone number')
    btnlog.config(command=lambda:login2())
    
#====================
username=StringVar()
password=StringVar()

#=====Title=====
title=Label(root,text='Login System',font=('Courier',15),bg='black',fg='white')
title.pack(fill=X)

#=====Frame=====
frame1=Frame(root,width=900,height=1050,bg='whitesmoke')
frame1.pack(pady=30)

myname=Label(frame1,text='BY : Haitham.N.Sharlie',bg='whitesmoke')
myname.place(x=320,y=1000)
#=====Logo panel=====
photo=PhotoImage(file='Secure data-bro.png')

panel=Label(root,image=photo,bg='whitesmoke')
panel.place(x=350,y=60)
#=====Labels And Entys=====
lblusr=Label(frame1,text='Username :',font=('Courier',15),bg='whitesmoke')
lblusr.place(x=10,y=500)

entryuser=Entry(frame1,textvariable=username)
entryuser.place(x=350,y=500,width=400,height=70)


lblpas=Label(frame1,text='Password :',font=('Courier',15),bg='whitesmoke')
lblpas.place(x=10,y=650)

entrypas=Entry(frame1,show='*',textvariable=password)
entrypas.place(x=350,y=650,width=400,height=70)
#Show And Hide Button
toggle_btn = Button(frame1,image=show_photo,bg='white', command=toggle_password)
toggle_btn.place(x=700,y=650,width=70,height=70)
#====Buttons======
cb=Checkbutton(frame1,text='Forget Password',font=('Courier',12),bg='whitesmoke',command=lambda:forget())
cb.place(x=350,y=750)

btnlog=Button(frame1,text='LOGIN',font=('Courier',15),bg='whitesmoke',width=12,bd=2,command=lambda:login())
btnlog.place(x=45,y=850)


btnsign=Button(frame1,text='SIGNIN',font=('Courier',15),bg='whitesmoke',width=12,bd=2)
btnsign.place(x=455,y=850)

btnexit=Button(frame1,text='Exit',bg='whitesmoke',bd=3,font=('celibri',10,'bold'),command=lambda:root.destroy()).place(x=710,y=10,width=180,height=80)

root.mainloop()