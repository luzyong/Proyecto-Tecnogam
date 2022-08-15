from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import Pmw
from PIL import Image, ImageTk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from threading import *
import time
from pylogixx import *

class ventanas():
    def __init__(self,master):
        self.plc=[]
        self.data1 = {'X': ['US','CA','GER','UK','FR'],
         'Temperaturas': [45000,42000,52000,49000,47000]
        }
        self.df1 = DataFrame(self.data1,columns=['X','Temperaturas'])
        self.on  = "#61DB82"
        self.off = "#FD0A2A"
        self.run = 0
        self.lights = 0
        self.oven1 = StringVar()
        self.oven2 = StringVar()
        self.chimney1 = StringVar()
        self.chimney2 = StringVar()
        self.extract = 0
        self.turb1 = 0
        self.turb2 = 0
        self.burn = 0
        self.bomb = 0
        self.limit = 0
        self.prueba=0
        self.measure1=StringVar()
        self.measure2=StringVar()
        self.measure3=StringVar()

        #************************** CONTENEDOR 3 PÁGINAS ******************************************************************
        self.notebook = ttk.Notebook(master, padding='0.1i')
        #___________________________ PÁGINA 1 ____________________________________________________________________________________________
        self.mainframe = Frame(self.notebook,bg='#232b2b')
        #**************************** SECCIÓN DE IMAGEN ***************
        self.frame1 = Frame(self.mainframe,bg='#232b2b')
        self.maquina = Canvas(self.frame1,bg='white',borderwidth=2,relief=GROOVE)
        self.maquina.pack(padx=3,pady=3)
        self.img = ImageTk.PhotoImage(Image.open("C:\\Users\\admin\\Documents\\madonna.png"))
        self.maquina.create_image(10,10,anchor=NW,image=self.img)
        self.frame1.pack(side=TOP,expand=YES,fill=BOTH,padx=3,pady=3)
        #***************************** SECCIÓN DE DISPLAYS *************
        self.frame2 = Pmw.Group(self.mainframe,tag_pyclass=None,tag_background='black')
        self.frame2.pack(side=TOP,expand=YES,fill=BOTH,padx=3,pady=2)

        self.paquete1=Frame(self.frame2.interior(),borderwidth=2,relief=RAISED,bg='#A8A9AD')
        self.subframe21 = Frame(self.paquete1,bg='#A8A9AD')
        self.horno1 = Label(self.subframe21, text= '° HORNO 1',background='#A8A9AD').pack(side=LEFT,expand=YES,fill=BOTH)
        self.horno2 = Label(self.subframe21, text='° HORNO 2',background='#A8A9AD').pack(side=LEFT,expand=YES,fill=BOTH)
        self.chimenea1 = Label(self.subframe21, text='° CHIMENEA 1',background='#A8A9AD').pack(side=LEFT,expand=YES,fill=BOTH)
        self.chimenea2 = Label(self.subframe21,text='° CHIMENEA 2',background='#A8A9AD').pack(side=LEFT,expand=YES,fill=BOTH)
        self.subframe21.pack(side=TOP,expand=YES,fill=BOTH)

        self.subframe22 = Frame(self.paquete1,bg='#3b444b',borderwidth=1.5,relief=SUNKEN)
        self.horno1 = Label(self.subframe22, textvariable= self.oven1,font=('Terminal',12),foreground='#c30d00',justify=CENTER,anchor=CENTER,background='black',borderwidth=2,relief=RAISED).pack(side=LEFT,expand=YES,ipadx=2,ipady=2,pady=2)
        self.horno2 = Label(self.subframe22, textvariable=self.oven2,font=('Terminal',12),foreground='#c30d00',justify=CENTER,anchor=CENTER,background='black',borderwidth=2,relief=RAISED).pack(side=LEFT,expand=YES,ipadx=2,ipady=2)
        self.chimenea1 = Label(self.subframe22, textvariable=self.chimney1,font=('Terminal',12),foreground='#c30d00',justify=CENTER,anchor=CENTER,background='black',borderwidth=2,relief=RAISED).pack(side=LEFT,expand=YES,ipadx=2,ipady=2)
        self.chimenea2 = Label(self.subframe22,textvariable=self.chimney2,font=('Terminal',12),foreground='#c30d00',justify=CENTER,anchor=CENTER,background='black',borderwidth=2,relief=RAISED).pack(side=LEFT,expand=YES,ipadx=2,ipady=2)
        self.subframe22.pack(side=TOP,expand=YES,fill=BOTH,padx=3,pady=3)
        self.paquete1.pack(side=TOP,expand=YES,fill=BOTH)
        #******************************* SECCIÓN DE INDICADORES LED ***********
        self.frame3 = Pmw.Group(self.mainframe,tag_pyclass=None)
        self.frame3.pack(side=TOP,expand=YES,fill=BOTH,padx=3)

        self.paquete2=Frame(self.frame3.interior(),borderwidth=2,relief=RAISED,bg='#A8A9AD')

        self.subframe31 = Frame(self.paquete2,bg='#3b444b',borderwidth=1.5,relief=SUNKEN)
        self.circulo1 = Canvas(self.subframe31, borderwidth=2,relief=RAISED,width=20, height=20,bg=self.on)
        self.circulo1.pack(side=LEFT,expand=YES,padx=2)
        self.circulo2 = Canvas(self.subframe31, borderwidth=2,relief=RAISED,width=20, height=20,bg=self.on)
        self.circulo2.pack(side=LEFT,expand=YES)
        self.circulo3 = Canvas(self.subframe31, borderwidth=2,relief=RAISED,width=20, height=20,bg=self.on)
        self.circulo3.pack(side=LEFT,expand=YES)
        self.circulo4 = Canvas(self.subframe31, borderwidth=2,relief=RAISED,width=20, height=20,bg=self.on)
        self.circulo4.pack(side=LEFT,expand=YES)
        self.circulo5 = Canvas(self.subframe31, borderwidth=2,relief=RAISED,width=20, height=20,bg=self.on)
        self.circulo5.pack(side=LEFT,expand=YES)
        self.circulo6 = Canvas(self.subframe31, borderwidth=2,relief=RAISED,width=20, height=20,bg=self.on)
        self.circulo6.pack(side=LEFT,expand=YES)
        self.circulo7 = Canvas(self.subframe31, borderwidth=2,relief=RAISED,width=20, height=20,bg=self.on)
        self.circulo7.pack(side=LEFT,expand=YES,pady=3)
        self.subframe31.pack(side=TOP,expand=YES,fill=X,padx=3,pady=3)

        self.subframe32 = Frame(self.paquete2,bg='#A8A9AD')
        self.extractor = Label(self.subframe32, text= 'EXTRACTOR',justify=CENTER,anchor=CENTER,background='#A8A9AD').pack(side=LEFT,expand=YES,ipadx=16)
        self.turbo1 = Label(self.subframe32, text='TURBO 1',justify=CENTER,anchor=CENTER,background='#A8A9AD').pack(side=LEFT,expand=YES,fill=X,ipadx=19)
        self.turbo2 = Label(self.subframe32, text='TURBO 2',justify=CENTER,anchor=CENTER,background='#A8A9AD').pack(side=LEFT,expand=YES,fill=X,ipadx=19)
        self.bomba = Label(self.subframe32,text='BOMBA',justify=CENTER,anchor=CENTER,background='#A8A9AD').pack(side=LEFT,expand=YES,fill=X,ipadx=22)
        self.limite = Label(self.subframe32, text='LIMITE',justify=CENTER,anchor=CENTER,background='#A8A9AD').pack(side=LEFT,expand=YES,fill=X,ipadx=23)
        self.quemadoron = Label(self.subframe32, text='QUEMADOR ON',justify=CENTER,anchor=CENTER,background='#A8A9AD').pack(side=LEFT,expand=YES,fill=X,ipadx=2.5)
        self.quemadoroff = Label(self.subframe32,text='QUEMADOR OFF',justify=CENTER,anchor=CENTER,background='#A8A9AD').pack(side=LEFT,expand=YES,fill=X)
        self.subframe32.pack(side=TOP,expand=YES,fill=BOTH,padx=3,pady=3)

        self.paquete2.pack(side=TOP,expand=YES,fill=BOTH)
        #******************************** SECCIÓN DE ENTRADAS *********
        self.frame4 = Pmw.Group(self.mainframe,tag_pyclass=None,tag_background='black')
        self.frame4.pack(side=TOP,expand=YES,fill=BOTH,padx=3,pady=2)

        self.paquete3=Frame(self.frame4.interior(),borderwidth=2,relief=RAISED,bg='#A8A9AD')

        self.subframe21 = Frame(self.paquete3,bg='#A8A9AD')
        self.lote = Label(self.subframe21, text= 'LOTE',background='#A8A9AD').pack(side=LEFT,expand=YES,fill=BOTH)
        self.material = Label(self.subframe21, text='MATERIAL',background='#A8A9AD').pack(side=LEFT,expand=YES,fill=BOTH)
        self.cantidad = Label(self.subframe21, text='CANTIDAD',background='#A8A9AD').pack(side=LEFT,expand=YES,fill=BOTH)
        
        self.subframe21.pack(side=TOP,expand=YES,fill=BOTH)

        self.subframe22 = Frame(self.paquete3,bg='#3b444b',borderwidth=1.5,relief=SUNKEN)
        self.lotein = Entry(self.subframe22,bg='#232b2b',fg='#A8A9AD').pack(side=LEFT,expand=YES,pady=2)
        self.materialin = Entry(self.subframe22,bg='#232b2b',fg='#A8A9AD').pack(side=LEFT,expand=YES,pady=2)
        self.cantidadin = Entry(self.subframe22,bg='#232b2b',fg='#A8A9AD').pack(side=LEFT,expand=YES,pady=2)
        self.subframe22.pack(side=TOP,expand=YES,fill=BOTH,padx=3,pady=3)

        self.paquete3.pack(side=TOP,expand=YES,fill=BOTH)
        #********************************* SECCIÓN DE BOTONES ********
        self.frame5 = Pmw.Group(self.mainframe,tag_pyclass=None,tag_background='black')
        self.frame5.pack(side=TOP,expand=YES,fill=BOTH,padx=3,pady=2)

        self.paquete4=Frame(self.frame5.interior(),borderwidth=2,relief=RAISED,bg='#A8A9AD')

        self.lucesON = Button(self.paquete4,text='TURN ON LIGTHS',bg='#3b444b',fg='white',relief=RAISED,command=self.light_on)
        self.lucesON.pack(side=LEFT, expand=YES, pady=6)
        self.lucesOFF = Button(self.paquete4,text='TURN OFF LIGTHS',bg='#3b444b',fg='white',relief=RAISED,command=self.light_off)
        self.lucesOFF.pack(side=LEFT, expand=YES, pady=6)
        self.botonesON= Button(self.paquete4,text='POWER ON',bg='#3b444b',fg='white',relief=RAISED,command=self.threading)
        self.botonesON.pack(side=LEFT, expand=YES, pady=6)
        self.botonesOFF= Button(self.paquete4,text='POWER OFF',bg='#3b444b',fg='white',relief=RAISED,command=self.of)
        self.botonesOFF.pack(side=LEFT, expand=YES, pady=6)
        
        self.paquete4.pack(side=TOP,expand=YES,fill=BOTH)
        #******************************** TERMINA PÁGINA 1 ***********
        self.mainframe.pack(expand=YES,fill=BOTH)
        #_________________________________ PÁGINA 2 ___________________________________________________________________________________________________________________________
        self.tendencias = Frame(self.notebook,bg='white')
        self.figure1 = plt.Figure(figsize=(6,5), dpi=100)
        self.ax1 = self.figure1.add_subplot(111)
        self.bar1 = FigureCanvasTkAgg(self.figure1, self.tendencias)
        self.bar1.get_tk_widget().pack(side=LEFT, fill=BOTH,padx=30)
        #df1 = df1[['Country','GDP_Per_Capita']].groupby('Country').sum()
        self.df1.plot(kind='line', legend=True, ax=self.ax1)
        self.ax1.set_title('X Vs. Temperaturas')
        self.tendencias.pack(expand=YES,fill=BOTH)
        #_________________________________ PÁGINA 3 _________________________________________________________________________________-
        self.alerts = Frame(self.notebook,bg='#232b2b')
        self.alerts.pack(expand=YES,fill=BOTH)
        #_____________________________ AGREGANDO PÁGINAS AL CUADERNO _____________________________________________________________________________________-
        self.notebook.pack(expand=YES, fill=BOTH)
        self.notebook.add(self.mainframe, text="General")
        self.notebook.add(self.tendencias, text="Tendencias")
        self.notebook.add(self.alerts, text="Alertas")

    def threading(self):
        self.run = 1
        #print(str(self.measure1.get()),str(self.measure2.get()),str(self.measure3.get()))
        t1=Thread(target=self.work)
        t1.start()

    def of(self):
        self.run=0
        #print(self.measure1.get(),self.measure2.get(),self.measure3.get())
    
    def light_on(self):
        self.lights=1
        print(write(self.lights))
    
    def light_off(self):
        self.lights=0
        print(write(self.lights))


            
        
    def work(self):
        while self.run == 1:
            '''valores = read()
            for valor in valores:
                data={
                    'valor':valor,
                    'typo':Type(valor)
                }
                self.plc.append(data)
            archivo = f'./plc.json'         
            with open(archivo, 'w') as fp:
                json.dump(rules, fp,  indent=4)
            fp.close()
            print(valores)'''
            if self.prueba%2==0:
                self.circulo1.configure(bg=self.on)
                self.circulo2.configure(bg=self.off)
                self.circulo3.configure(bg=self.on)
                self.circulo4.configure(bg=self.off)
                self.circulo5.configure(bg=self.on)
                self.circulo6.configure(bg=self.off)
                self.circulo7.configure(bg=self.on)
                self.oven1.set(f'{self.prueba}')
                self.oven2.set(f'{self.prueba}')
                self.chimney1.set(f'{self.prueba}')
                self.chimney2.set(f'{self.prueba}')
            else:
                self.circulo1.configure(bg=self.off)
                self.circulo2.configure(bg=self.on)
                self.circulo3.configure(bg=self.off)
                self.circulo4.configure(bg=self.on)
                self.circulo5.configure(bg=self.off)
                self.circulo6.configure(bg=self.on)
                self.circulo7.configure(bg=self.off)
                self.oven1.set('a')
                self.oven2.set('b')
                self.chimney1.set('c')
                self.chimney2.set('d')
            self.prueba+=1
            time.sleep(1)
            
class about():
    def __init__(self,master):
        Pmw.initialise()
        Pmw.aboutversion('1.5')
        Pmw.aboutcopyright('Copyright Tecnogam 2022\nAll rights reserved')
        Pmw.aboutcontact(
        'For information about this application contact:\n' +
        ' Luz Yong\n' +
        ' Phone: (401) 555-1212\n' +
        ' email: info@company_name.com'
        )
        about = Pmw.AboutDialog(master, applicationname='Tecnogam')
        
root = Tk()
root['background']='#474747'
horno = ventanas(root)
#abaout = about(root)
root.mainloop()