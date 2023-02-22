from tkinter import *
from tkinter import messagebox
from sqlite3 import *

def tiklandi():
    kayitSorusu = messagebox.askyesno('Kaydet','AD: {}\tSOYAD: {}\nNOT1: {}\tNOT2: {}\n\nKaydetmek istediğinizden emin misiniz?'
                                      .format(adEnt.get(),soyadEnt.get(),not1Ent.get(),not2Ent.get()))
    if kayitSorusu == True:
        merhaba = connect('Sınıf.db')
        imlec = merhaba.cursor()
        imlec.execute('CREATE TABLE IF NOT EXISTS sınıf(ad TEXT,soyad TEXT,not1 TEXT,not2 TEXT)')
        imlec.execute(f"INSERT INTO sınıf VALUES('{adEnt.get()}','{soyadEnt.get()}','{not1Ent.get()}','{not2Ent.get()}')")
        merhaba.commit()
    else: 
        pass

pencere=Tk()

pencere.resizable(height=False,width=False)

Canvas(pencere,height=450, width=750).pack()

freymYazi = Frame(pencere)
freymYazi.place(relx= 0.1, rely=0.1, relwidth=0.30, relheight=0.55)

freymEnt = Frame(pencere)
freymEnt.place(relx=0.4, rely=0.1, relwidth=0.27, relheight=0.55)

freymButon = Frame(pencere)
freymButon.place(relx=0.2,rely=0.85, relwidth=0.5, relheight=0.10)

# rely=10

ad = Label(freymYazi,text='Ad\t:',font=('arial 25 bold'))
ad.pack(padx=10,pady=10,side=TOP)

soyad = Label(freymYazi,text='Soyad\t:',font=('arial 25 bold'))
soyad.pack(padx=10,pady=10,side=TOP)

not1 = Label(freymYazi,text='1.Notu\t:',font=('arial 25 bold'))
not1.pack(padx=10,pady=10,side=TOP)

not2 = Label(freymYazi,text='2.Notu\t:',font=('arial 25 bold'))
not2.pack(padx=10,pady=10,side=TOP)

adEnt = Entry(freymEnt,width=50,font=('arial 25 bold'))
adEnt.pack(padx=0,pady=10)

soyadEnt = Entry(freymEnt,width=50,font=('arial 25 bold'))
soyadEnt.pack(padx=0,pady=10)

not1Ent = Entry(freymEnt,width=50,font=('arial 25 bold'))
not1Ent.pack(padx=0,pady=10)

not2Ent = Entry(freymEnt,width=50,font=('arial 25 bold'))
not2Ent.pack(padx=0,pady=10)

kaydet = Button(freymButon,text='Kaydet',font=('arial 20 bold italic'),bg='blue',fg='LIGHT BLUE',
                activebackground='LIGHT BLUE',activeforeground='blue',command=tiklandi)
kaydet.pack()

pencere.mainloop()
