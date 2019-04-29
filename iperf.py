
    # /$$$$$                                     /$$$$$$$             /$$$$$$                      /$$       /$$$$$$$                               
   # |__  $$                                    | $$__  $$           /$$__  $$                    | $$      | $$__  $$                              
      # | $$  /$$$$$$   /$$$$$$   /$$$$$$       | $$  \ $$  /$$$$$$ | $$  \__/  /$$$$$$   /$$$$$$ | $$      | $$  \ $$  /$$$$$$   /$$$$$$   /$$$$$$$
      # | $$ /$$__  $$ |____  $$ /$$__  $$      | $$$$$$$/ |____  $$| $$$$     |____  $$ /$$__  $$| $$      | $$$$$$$  /$$__  $$ |____  $$ /$$_____/
 # /$$  | $$| $$  \ $$  /$$$$$$$| $$  \ $$      | $$__  $$  /$$$$$$$| $$_/      /$$$$$$$| $$$$$$$$| $$      | $$__  $$| $$  \__/  /$$$$$$$|  $$$$$$ 
# | $$  | $$| $$  | $$ /$$__  $$| $$  | $$      | $$  \ $$ /$$__  $$| $$       /$$__  $$| $$_____/| $$      | $$  \ $$| $$       /$$__  $$ \____  $$
# |  $$$$$$/|  $$$$$$/|  $$$$$$$|  $$$$$$/      | $$  | $$|  $$$$$$$| $$      |  $$$$$$$|  $$$$$$$| $$      | $$$$$$$/| $$      |  $$$$$$$ /$$$$$$$/
 # \______/  \______/  \_______/ \______/       |__/  |__/ \_______/|__/       \_______/ \_______/|__/      |_______/ |__/       \_______/|_______/ 


# -*-coding:Latin-1 -*
import os
import re 
from plot2d_iperf import * 

def change_dir():
    """Change le repertoire de travaille"""
    dir=input("Indiquez le repoertoire de travail\n")
    string=string_input_test(dir)
    os.chdir(string)

def string_input_test (chaine):

        """tester si les informations sont bien une chaine de caracteres
    renvoye une chaine de caracteres avec le nom du fichier"""
        flag=True
        while flag:
                try:
                    chaine = str(chaine)
                    flag = False
                except:
                    flag=True
        return chaine

def file_open_test (file):
    """test l'ouverture d'ub fichier"""
    try:
        #ouvre et ferme en suite le fichier pour confirmer son existence
        fichier=open(file,"r")
        fichier.close()
    except FileNotFoundError:
        change_dir()
        fichier=input("Indique le nom du fichier\n")
        fichier=string_input_test(fichier)
        file_open_test(fichier)
        
def iperf_log (file,mode,title):
    """ouvrir le fichier et effectuer la lecture et crée listes par paragraphe
    La valeur par defaut est de lire le fichier
    renvoye une liste avec les paragraphes"""
    i=0
    k=0
    temp="q"
    #expressions a cherhcer et a modifier sur les paragraphes
    search_exp=r'[ ,-]+'
    rep_exp=r' '
    lines=[]#creation d'une liste vide
    with open(file,mode) as fichier:#ouverture d'un fichier avec fermeture automatique à la fin
        while(temp!=""):
            temp=fichier.readline()#stockage de la chaine dans une variable temporaire
            temp=string_input_test(temp)#test de la chaine de caracteres
            temp=re.sub(search_exp,rep_exp,temp)#remplace tous les espaces ou plus d'un espace par un seul
            lines.insert(i,temp)#ajoute le paragraphe a la liste
            i+=1#incremente le nb de paragraphes du texte
        lines=lines[3:i-2]
        i=i-5
        j=0
        xmax=0
        ymax=0
        somme=0
        liste=[]
        temps=[]
        debit=[]
        unit=[]
        debitmoy=0
        debitmin=900
        average=[]
        while(j<=i-1):#traitement de fichier text
                liste=lines[j]
                liste=liste.split(" ")#les mots sont separes par des espaces
                #os.system('pause')
                if (liste[0]==''):
                    k=j
                    break
                temps.append(liste[3])#informations sur la debit
                debit.append(liste[7])#informations sur la temps
                unit.append(liste[8])#informations unité
                debit[j]=float(debit[j])
                temps[j]=float(temps[j])-0.01
                if unit[j]=="Mbits/sec":
                    debit[j]=debit[j]/1000
                elif unit[j]=="Kbits/sec":
                    debit[j]=debit[j]/1000000
                if debit[j]<debitmin :
                    debitmin=debit[j]
                j+=1
        #traitement valeur moyenne
        average=lines[k+2]
        average=average.split(" ")
        debitmoy=float(average[7])
        if average[8]=="Mbits/sec":
            debitmoy=debitmoy/1000
        elif average[8]=="Kbits/sec":
            debitmoy=debitmoy/1000000
        unitdebitmoy=average[8]
        chaine="Average throughput"+" "+average[7]+" "+unitdebitmoy
    plot(temps,debit,chaine,debitmoy,title)
        

if __name__=="__main__":
    import plot2d_iperf
    change_dir()
    file=input("Indiquez le fichier a ouvrir\n")
    file_open_test(file)
    iperf_log(file)
    os.system("Pause")
    
