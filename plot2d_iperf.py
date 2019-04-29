    # /$$$$$                                     /$$$$$$$             /$$$$$$                      /$$       /$$$$$$$                               
   # |__  $$                                    | $$__  $$           /$$__  $$                    | $$      | $$__  $$                              
      # | $$  /$$$$$$   /$$$$$$   /$$$$$$       | $$  \ $$  /$$$$$$ | $$  \__/  /$$$$$$   /$$$$$$ | $$      | $$  \ $$  /$$$$$$   /$$$$$$   /$$$$$$$
      # | $$ /$$__  $$ |____  $$ /$$__  $$      | $$$$$$$/ |____  $$| $$$$     |____  $$ /$$__  $$| $$      | $$$$$$$  /$$__  $$ |____  $$ /$$_____/
 # /$$  | $$| $$  \ $$  /$$$$$$$| $$  \ $$      | $$__  $$  /$$$$$$$| $$_/      /$$$$$$$| $$$$$$$$| $$      | $$__  $$| $$  \__/  /$$$$$$$|  $$$$$$ 
# | $$  | $$| $$  | $$ /$$__  $$| $$  | $$      | $$  \ $$ /$$__  $$| $$       /$$__  $$| $$_____/| $$      | $$  \ $$| $$       /$$__  $$ \____  $$
# |  $$$$$$/|  $$$$$$/|  $$$$$$$|  $$$$$$/      | $$  | $$|  $$$$$$$| $$      |  $$$$$$$|  $$$$$$$| $$      | $$$$$$$/| $$      |  $$$$$$$ /$$$$$$$/
 # \______/  \______/  \_______/ \______/       |__/  |__/ \_______/|__/       \_______/ \_______/|__/      |_______/ |__/       \_______/|_______/ 


import matplotlib.pyplot as plt
import os
from tkinter import *
from math import ceil
from numpy import linspace


#fonction de test des chaines de caracteres
def string_test(string):
	flag=True
	while(flag):
		try:
			title=str(title)
			flag=False
		except:
			title=("La chaine de caracteres est fausse veuillez en introduire une autre \n")
			
def plot(xtemp,y,chaine,unitdebitmoy,title):
        """affiche les points sur un repére cathesien
                Cette fonction prends comme arguments les valeurs des points en
                abcisse(x) et ordonnée(y) sous forme de liste, elle a aussi comme arguments
                optionnels la taille de la fenetre si on passe en paramettre que les points x,y 
                la fenetre du graphique est de 100"""
        moy=[]
        somme=0
        avg=0
        i=1
        x=[]
        Y=[]
        #arrondir à des valeurs entiéres l'axe des x
        for i,info in enumerate(xtemp):
            x.append(ceil(xtemp[i]))
        #si l'arrondi à creé 2 valeurs egales on force
        #un "deuxiéme arrondi" mais cette fois à a valeur inferieur
        for i,info in enumerate(x):    
            if (x[i]==x[i-1]):
                x[i-1]=x[i-1]-1
        #ajouter la valeur 0 au graphique
        x.insert(0,0)
        y.insert(0,0)
        #creation d'une liste qui contiens la meme valeur dans toutes les cases por
        #faire notre constante
        for i,info in enumerate(x):
            moy.append(unitdebitmoy)
        #tester le titre de notre graphique
        string_test(title)
        plt.title(title)
        #gerer les echelles
        plt.axis([x[0],x[-1],0,2])#limite les axes 
        #discretiser les axes des graphiques
        plt.yticks(linspace(0,2,20))
        plt.xticks(range(x[-1]))###################range(x[-1]+1)
        plt.xlabel("Minutes")
        plt.ylabel("Gbits/sec")
        #preparation de la courbe
        plt.plot(x,y,label="Troughput's Evolution")
        plt.plot(x,moy,label=chaine)
        plt.legend()
        #plt.text(30,1,chaine)
        #affichr un grille
        plt.grid(True)
        plt.show()

if __name__=="__main__":
	plot([1,2,3,4],[10,5,50,40],"test")
	os.system("Pause")
	
	
