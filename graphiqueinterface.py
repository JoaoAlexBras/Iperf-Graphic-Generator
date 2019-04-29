
    # /$$$$$                                     /$$$$$$$             /$$$$$$                      /$$       /$$$$$$$                               
   # |__  $$                                    | $$__  $$           /$$__  $$                    | $$      | $$__  $$                              
      # | $$  /$$$$$$   /$$$$$$   /$$$$$$       | $$  \ $$  /$$$$$$ | $$  \__/  /$$$$$$   /$$$$$$ | $$      | $$  \ $$  /$$$$$$   /$$$$$$   /$$$$$$$
      # | $$ /$$__  $$ |____  $$ /$$__  $$      | $$$$$$$/ |____  $$| $$$$     |____  $$ /$$__  $$| $$      | $$$$$$$  /$$__  $$ |____  $$ /$$_____/
 # /$$  | $$| $$  \ $$  /$$$$$$$| $$  \ $$      | $$__  $$  /$$$$$$$| $$_/      /$$$$$$$| $$$$$$$$| $$      | $$__  $$| $$  \__/  /$$$$$$$|  $$$$$$ 
# | $$  | $$| $$  | $$ /$$__  $$| $$  | $$      | $$  \ $$ /$$__  $$| $$       /$$__  $$| $$_____/| $$      | $$  \ $$| $$       /$$__  $$ \____  $$
# |  $$$$$$/|  $$$$$$/|  $$$$$$$|  $$$$$$/      | $$  | $$|  $$$$$$$| $$      |  $$$$$$$|  $$$$$$$| $$      | $$$$$$$/| $$      |  $$$$$$$ /$$$$$$$/
 # \______/  \______/  \_______/ \______/       |__/  |__/ \_______/|__/       \_______/ \_______/|__/      |_______/ |__/       \_______/|_______/ 


from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from iperf import *
from sys import *

class Interface(Frame):
    Flag=10
    filepath=""
    content=""
    title=""
    def __init__(self,fenetre,**kwargs):
        #creer une fenetre
        #barre du haut
        Frame.__init__(self,fenetre,width=800,height=300,**kwargs)
        self.pack(fill=BOTH)
        
        #parametre des affichages
        fenetre.iconbitmap("test.ico")#avant convertir en exe enlever cette ligne
        fenetre.title("Iperf Graphics Generator")
        
        menubar = Menu(fenetre)

        menu1 = Menu(menubar, tearoff=0)
        menu1.add_command(label="File", command=self.openfile)
        menu1.add_separator()
        menu1.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=menu1)

        menu3 = Menu(menubar, tearoff=0)
        menu3.add_command(label="Help", command=self.aide)
        menubar.add_cascade(label="Help", menu=menu3)

        fenetre.config(menu=menubar)
        
        #gerer les widgets
        self.label("Set graphic's title")
        self.txtzone()
        self.exitBoutton("Exit","left")
        self.open("OK","right")

        #creer des widgets
    def label(self,txt="",zone=None):
        """cree du text en parametre on indique le txte et la zonne ou on le veut
            le placer au milleur par defaut"""
        self.message=Label(self,text=txt)
        self.message.pack(side=zone)
        
    def exitBoutton(self,txt="",zone=None):
        """cree un boutton pour arreter le programme en parametre on indique le txte et la zonne ou on le veut
            le placer au milleur par defaut"""    
        self.exit=Button(self,text=txt,command=self.quit)
        self.exit.pack(side=zone)

    def button(self,txt="",zone=None,cmd=None):
        """cree un boutton pour arreter le programme en parametre on indique le txte et la zonne ou on le veut
            le placer au milleur par defaut"""    
        self.button=Button(self,text=txt,command=cmd)
        self.button.pack(side=zone)
        
        
        
    def open(self,txt="",zone=None):    
        """cree boutton qui permet d'ouvrir un fichier un fichier en parametre on indique le txte et la zonne ou on le veut
            le placer au milleur par defaut"""    
        self.choisir=Button(self,text=txt,command=self.openfile)
        Flag=1
        self.choisir.pack(side=zone)
        
    def ok_checkb(self,txt="",zone=None):    
        """cree un chekbutton en parametre on indique le txte et la zonne ou on le veut
            le placer au milleur par defaut"""    
        var_case=IntVar()
        self.ok=Checkbutton(self,text=txt,variable=var_case)
        self.ok.pack(side=zone)
        Flag=var_case.get()
       
    def send(self,event):
        self.title=self.txt.get()
        self.title=str(self.title) 
        filepath=askopenfilename(title="Chose file ",filetypes=[('txt files','.txt'),('iperf files','.iperf'),('all files','.*')])
        iperf_log(filepath,"r",self.title)
        
    def txtzone (self,zone=None):
        var=StringVar()
        self.txt=Entry(self,textvariable=var,width=30)
        self.txt.bind("<Return>",self.send)#quand appuye sur entree
        self.txt.pack(side=zone)
        
        
   
    #creation dactions
    def openfile(self):
        """Renvoye le chemain du fichier"""
        self.title=self.txt.get()
        self.title=str(self.title) 
        filepath=askopenfilename(title="Chose file ",filetypes=[('txt files','.txt'),('iperf files','.iperf'),('all files','.*')])
        iperf_log(filepath,"r",self.title)
        
    def aide (self):
        """affiche le menu aide"""
        showinfo("Help",
            """This software is made to create graphs from iperf logs\n
            You must sva the iperf logs in .txt or .iperf files\n
            Then the graph is generated\n
            Simple no ;)\n""")
            

        

     

 
        
#declaration de Frames        
class cadre (Interface):
    def __init__ (self,interface,w=150,h=300,zone=None,**kwargs):
        Frame.__init__(self,interface,width=w,height=h,**kwargs)
        self.pack(side=zone)

        
if __name__=="__main__":
    fenetre=Tk()
    interface=Interface(fenetre)
    interface.mainloop()
