import os
import json
import pprint
import nmap
import shutil
import glob
from colorama import Fore, Back, Style, init

init()

dir_path = '.' #variable pour stocker le repertoire où la ligne suivante va chercher les fichier .json
json_files = [f for f in os.listdir(dir_path) if f.endswith('.json')] #la function os.listdir(dir_path) retourne les fichier et repertoires qui sont dans le repertoire (dir_path)...."f for f in..." est un boucle qui va itérer dans la liste doné par os.listdir(dir_path)....if f.endswith('.json') c'est un conditional qui filtre la liste avec les fichier qui se terminent par .json


titre_server_config = """

░█▀▀░█▀▀░█▀▄░█░█░█▀▀░█▀▄░░░█▀▀░█▀█░█▀█░█▀▀░▀█▀░█▀▀
░▀▀█░█▀▀░█▀▄░▀▄▀░█▀▀░█▀▄░░░█░░░█░█░█░█░█▀▀░░█░░█░█
░▀▀▀░▀▀▀░▀░▀░░▀░░▀▀▀░▀░▀░░░▀▀▀░▀▀▀░▀░▀░▀░░░▀▀▀░▀▀▀
"""
Selection = """
          ╔╦╗┌─┐┌┐┌┬ ┬            
--------  ║║║├┤ ││││ │  --------- 
          ╩ ╩└─┘┘└┘└─┘            
1. Ajouter une configuration      
2. Modifier une configuration     
3. Lister les configurations      
4. Supprimer une configuration    
5. Sauvegarder les configurations 
6. Restaurer les configurations   
7. Scanner les serveurs (NMAP)    
--------------------------------- 
"""
fichier_conf = """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
╔╗╔┌─┐┬ ┬┬  ┬┌─┐┌─┐┬ ┬  ╔═╗┬┌─┐┬ ┬┬┌─┐┬─┐  ╔═╗╔═╗╔╗╔╔═╗
║║║│ ││ │└┐┌┘├┤ ├─┤│ │  ╠╣ ││  ├─┤│├┤ ├┬┘  ║  ║ ║║║║╠╣ 
╝╚╝└─┘└─┘ └┘ └─┘┴ ┴└─┘  ╚  ┴└─┘┴ ┴┴└─┘┴└─  ╚═╝╚═╝╝╚╝╚      
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

modifier_une_conf = """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
╔╦╗┌─┐┌┬┐┬┌─┐┬┌─┐┬─┐  ┬ ┬┌┐┌  ╔═╗┬┌─┐┬ ┬┬┌─┐┬─┐  ╔═╗╔═╗╔╗╔╔═╗
║║║│ │ │││├┤ │├┤ ├┬┘  │ ││││  ╠╣ ││  ├─┤│├┤ ├┬┘  ║  ║ ║║║║╠╣ 
╩ ╩└─┘─┴┘┴└  ┴└─┘┴└─  └─┘┘└┘  ╚  ┴└─┘┴ ┴┴└─┘┴└─  ╚═╝╚═╝╝╚╝╚    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

fichier_conf_liste = """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
╦  ┬┌─┐┌┬┐┌─┐  ┌┬┐┌─┐┌─┐  ╔═╗┬┌─┐┬ ┬┬┌─┐┬─┐┌─┐  ╔═╗╔═╗╔╗╔╔═╗
║  │└─┐ │ ├┤    ││├┤ └─┐  ╠╣ ││  ├─┤│├┤ ├┬┘└─┐  ║  ║ ║║║║╠╣ 
╩═╝┴└─┘ ┴ └─┘  ─┴┘└─┘└─┘  ╚  ┴└─┘┴ ┴┴└─┘┴└─└─┘  ╚═╝╚═╝╝╚╝╚      
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

supprimer_conf = """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
╔═╗┬ ┬┌─┐┌─┐┬─┐┬┌┬┐┌─┐┬─┐  ┬ ┬┌┐┌  ╔═╗┬┌─┐┬ ┬┬┌─┐┬─┐  ╔═╗╔═╗╔╗╔╔═╗
╚═╗│ │├─┘├─┘├┬┘││││├┤ ├┬┘  │ ││││  ╠╣ ││  ├─┤│├┤ ├┬┘  ║  ║ ║║║║╠╣ 
╚═╝└─┘┴  ┴  ┴└─┴┴ ┴└─┘┴└─  └─┘┘└┘  ╚  ┴└─┘┴ ┴┴└─┘┴└─  ╚═╝╚═╝╝╚╝╚   
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
sauvegarde_conf = """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
╔═╗┌─┐┬ ┬┬  ┬┌─┐┌─┐┌─┐┬─┐┌┬┐┌─┐┬─┐  ┬ ┬┌┐┌  ╔═╗┬┌─┐┬ ┬┬┌─┐┬─┐  ╔═╗╔═╗╔╗╔╔═╗
╚═╗├─┤│ │└┐┌┘├┤ │ ┬├─┤├┬┘ ││├┤ ├┬┘  │ ││││  ╠╣ ││  ├─┤│├┤ ├┬┘  ║  ║ ║║║║╠╣ 
╚═╝┴ ┴└─┘ └┘ └─┘└─┘┴ ┴┴└──┴┘└─┘┴└─  └─┘┘└┘  ╚  ┴└─┘┴ ┴┴└─┘┴└─  ╚═╝╚═╝╝╚╝╚  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

scan_conf = """  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   
╔═╗┌─┐┌─┐┌┐┌  ┌┬┐┌─┐┌─┐  ╔═╗┬┌─┐┬ ┬┬┌─┐┬─┐┌─┐  ╔═╗╔═╗╔╗╔╔═╗ 
╚═╗│  ├─┤│││   ││├┤ └─┐  ╠╣ ││  ├─┤│├┤ ├┬┘└─┐  ║  ║ ║║║║╠╣  
╚═╝└─┘┴ ┴┘└┘  ─┴┘└─┘└─┘  ╚  ┴└─┘┴ ┴┴└─┘┴└─└─┘  ╚═╝╚═╝╝╚╝╚ooo 

 /$$   /$$                                  
| $$$ | $$                                  
| $$$$| $$ /$$$$$$/$$$$   /$$$$$$   /$$$$$$ 
| $$ $$ $$| $$_  $$_  $$ |____  $$ /$$__  $$    
| $$  $$$$| $$ \ $$ \ $$  /$$$$$$$| $$  \ $$
| $$\  $$$| $$ | $$ | $$ /$$__  $$| $$  | $$
| $$ \  $$| $$ | $$ | $$|  $$$$$$$| $$$$$$$/
|__/  \__/|__/ |__/ |__/ \_______/| $$____/ 
                                  | $$      
                                  | $$      
                                  |__/      
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
"""

restaurer_conf = """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
╦═╗┌─┐┌─┐┌┬┐┌─┐┬─┐┌─┐┌┬┐┬┌─┐┌┐┌  ╔═╗┬┌─┐┬ ┬┬┌─┐┬─┐┌─┐  ╔═╗╔═╗╔╗╔╔═╗
╠╦╝├┤ └─┐ │ │ │├┬┘├─┤ │ ││ ││││  ╠╣ ││  ├─┤│├┤ ├┬┘└─┐  ║  ║ ║║║║╠╣ 
╩╚═└─┘└─┘ ┴ └─┘┴└─┴ ┴ ┴ ┴└─┘┘└┘  ╚  ┴└─┘┴ ┴┴└─┘┴└─└─┘  ╚═╝╚═╝╝╚╝╚   
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
"""


selection_5 = """
-------Options-De-Sauvegarde--------------------------
1. Sauvegarder le nouveau Serveur
2. Sauvegarder les modifications du serveur existant
3. Revenir au Menu 
-----------------------------------------------------
"""

selection_6 = """
-------Options-De-Restoration--------------------------
1. Nouveau point de restauration
2. Restaurer depuis un point de restauration
3. Supprimer un point de sauvegarde
4. Revenir au Menu
-----------------------------------------------------
"""

def list_conf(): #Ici je define une function, car j'ai vais avoir besoin de la meme fonctionnalité pour l'option 6
            
    json_files = [f for f in os.listdir(dir_path) if f.endswith('.json')] #on charge la variable à nouveau, sinon quand on revient d'effacer un fichier la function pour lister ne trouve pas le fichier. 
    
    print(Fore.CYAN + Style.BRIGHT + fichier_conf_liste + Style.RESET_ALL) 
    
    print("")
    print("---------------------------------------------")
    print("Voici toutes les configurations des serveurs:")
    print("---------------------------------------------")
    print("")
    

    #for i, element in enumerate(json_files, start=1): #position des elements dans la liste en commencent par 1 et non 0
    #print(f"{i}. {element}") #imprime l'element i avec un string "." plus le numéro de 

    for i, file in enumerate(json_files, start=1): #Ici j'ai récupéré le code de l'option 2 (pour énumérer les fichiers) et j'ai l’intégré à la function que faisait la boucle pour ouvrir chaque fichier et montrer son contenu. Voici l'ancienne function qui énumère pas le nom du fichier:
    
    
        """
    for file in json_files:
        with open(os.path.join(dir_path, file), 'r') as f:
            data = json.load(f)
            print("")
            print("----------------------")
            print(file)
            print("")
            for key, value in data.items(): #fait une boucle pour et passe par item de "data"
                print(f"{key}: {value}")
    """

        print(f"{i}. {file}")
        with open(os.path.join(dir_path, file), 'r') as f:
            data = json.load(f)
            print("")               
            for key, value in data.items(): #fait une boucle pour et passe par item de "data"
                print(f"{key}: {value}")
            print("")   
            print("----------------------")
            
print(Style.BRIGHT + Fore.BLUE + titre_server_config + Style.RESET_ALL) #Titre du Logiciel

data_mod = {} #Ici on défini la variable que on va utiliser en option 2, de cette façon on peut la verifier avant sauvegarder en option 5. Autrement on a un error de variable pas défini si on veut enregistrer et on n'a pas modifié un fichier. (mais ça fonctionne avec la function json.dump)
server_config = {} #Pareil que data_mod dans la ligne d'avant.

while True: #Va créer la boucle, pour revenir toujours sélectionner une option dans le Menu General.


    try: #ici le try/except va nous créer le message d'error si l'option choisi est autre chose q'un int
        print(Style.BRIGHT + Fore.GREEN + Selection + Style.RESET_ALL) #Affiche la variable Selection avec les codes de couleur
        option = int(input(Back.BLUE + "Entrez votre sélection : " + Style.RESET_ALL)) #demande à l'utilisateur un input, Int.
        print("")
        print("--------------------------------")

    except ValueError:
        print(Fore.RED + Style.BRIGHT +"Erreur! Entrez une option entre 1 et 7" + Style.RESET_ALL) #Erreur s'il n'est pas entre 1 et 7 (pareil avec else de la fin du code)
        print("")
        continue

 
    
    if option == 1:
        print(Fore.CYAN + Style.BRIGHT + fichier_conf + Style.RESET_ALL)#Affiche la variable fichier_conf avec les codes de couleur
        print("")
        
        
        nom_ser = input(Fore.CYAN + "Entrez le nom du nouveau serveur\nou 'r' pour revenir au menu : ") #enregistre le nom du serveur dans la variable nom_ser
        

        if nom_ser == 'r': #reviens au menu principal avec l'input 'r'
            continue
        

        ip_ser = input("Entrez l'adresse IP : ") #enregistre l'IP dans la variable ip_ser.
    
        sys_exp = input("Entrez le système d'exploitation : ") #enregistre le système d’exploitation dans la variable sys_exp

        services_up = [input("Entrez les services en cours d'exécution (séparés par des virgules) :")] #enregistre les services qui sont en cours d'exécution dans la liste services_up

        server_config = {"Name":nom_ser, "Ip": ip_ser , "Systeme":sys_exp, "Services UP":services_up} #garde tout dans un dictionnaire dans la variable server_config, (apres avec option 5, le garde dans le fichier)
        print("")
        print(Fore.RED + Style.BRIGHT + """
                 /$$
                | $$
                | $$
                | $$
                |__/

                /$$
                |__/

Configuration pre-enregistré...\nOPTION 5 --> 1 pour Sauvegarder!""" + Style.RESET_ALL) #Une fois tous les paramètres ajoutée, en option 5 va les écrie en un fichier que le logiciel va à créer avec with.open and W mode.
                        
  
         
    
    
    elif option == 2:
        print(Fore.CYAN + Style.BRIGHT + modifier_une_conf + Style.RESET_ALL)
        print("------------------------------------")
        print("Liste des fichiers de configuration\n(Pour voir les contenus de toutes les fichiers --> revenir au menu/opt 3)")
        print("------------------------------------")
        print("")
        
        if 10 <= len(json_files): #Pour une liste trop grande des fichiers, va montrer juste les fichiers, sinon affiche les fichiers et leur contenu avec list_conf().
        
        
            json_files = [f for f in os.listdir(dir_path) if f.endswith('.json')] #Mets au jour la variable, s'il y a eu des fichiers supprimées, où modifiés.
            for i, element in enumerate(json_files, start=1): #position des elements dans la liste en commencent par 1 et non 0
                print(f"{i}. {element}") #imprime l'element i avec un string "." plus le numéro de 
        
        else:
            json_files = [f for f in os.listdir(dir_path) if f.endswith('.json')]#Mets au jour la variable, s'il y a eu des fichiers supprimées, où modifiés.
            list_conf() #Appel la variable.
       
        
        
        
        while True: #Ici j'ai mis une option supplémentaire pour pouvoir revenir au menu quand besoin. sinon faut changer l'input de serv_amod pour un str, et le transformer en int après.
            try:
                print("")
                continuer = input(Fore.CYAN + "--'Entrer'-- pour continuer\n'r' pour revenir au menu precedent: " + Style.RESET_ALL)
                if continuer == 'r':
                    break
                
                if continuer == "":
                    while True: #Boucle pour filtrer toutes les entrées invalides, quand c'est valid, break et continue.
                        try:

                            print("")
                            serv_amod = int(input(Fore.CYAN + "Choisir le numéro fichier de configuration qui vous voulez modifier: " + Style.RESET_ALL))
                           
                            if 1 <= serv_amod <= len(json_files):
                                break
                            else:
                                print(Fore.RED + Style.BRIGHT +  f"Entrée invalide. Seule un N° de Fichier de configuration, entre 1 et {len(json_files)}" + Style.RESET_ALL)
                                continue
                        except ValueError:
                                print(Fore.RED + Style.BRIGHT +  f"Entrée invalide, juste numéros sont accepté.\nSeule un N° de Fichier de configuration, entre 1 et {len(json_files)}" + Style.RESET_ALL)

                    print("")
                    print("-------------------------------")
                    print("Voici l'information du fichier:")
                    print("-------------------------------")
                    print("")
                    
                    with open(json_files[serv_amod - 1], 'r') as f: #ouvre le json_file dans la position choisi ([serv_amod - 1] -1 car on affiche sans compter la position 0), cette fois en mode "r" read et le met dans la variable f
                        data = json.load(f) #Charge la variable "data" avec le contenu (function de json.load) du fichier antérieurement mis das la variable f.
                        print(f"Nom du fichier: {os.path.basename(json_files[serv_amod - 1])}") #imprime le nom du fichier, pour ça utilise la fonctionnalité os.path.basename dans le fichier choisi par le User.
                        print("")
                        
                        for key, value in data.items(): #boucle qui va itérer dans le contenu (data) du dictionnaire
                            print(f"{key}: {value}") #Ici on le donne le format key: value pour qu'il soit lisible.
                        print("\n-----------------------------")                        
                        print("Modification ligne par ligne: ")
                        print("-----------------------------")                        
                        
                        for key, value in data.items(): #fait une boucle pour et passe par item de "data"                         
                            print(Fore.YELLOW + "|")                        
                            print("V")
                            print(f"{key}: {value}" + Style.RESET_ALL) #imprime la ligne qui va être modifié
                            print("")                
                            user_input = input(f"Entrer une nouvelle valeur pour {Fore.YELLOW + key + Style.RESET_ALL} (ou entrer pour conserver l'original): ") #charge la variable avec l'input de l'utilisateur. si pas d'input passe a la ligne suivante sans modifier l'actuel.
                            print("")
                            if user_input: #S'il y a eu un input
                                data_mod[key] = user_input #on remplace le value par l'input de l'utilisateur (que s'il a mis quelque chose). Et on le met das un nouveau dictionnaire (data_mod) avec la nouvelle data. Pour après l'enregistrer avec l'option 5 dans le Fichier.
                            else:
                                data_mod[key] = value #sinon, on laisse la même valeur
                        print("")
                        print(Fore.RED + Style.BRIGHT + """
                  /$$
                 | $$
                 | $$
                 | $$
                 |__/
                 /$$
                 |__/

Configuration pre-enregistré...\nOPTION 5 --> 2 pour Sauvegarder!""" + Style.RESET_ALL)
                        break
                            
                                 #SI ON VEUT QUE çA SOIT SAUVEGARDé DIRECTEMENT PENDANT QU'ON MODIFIE
                                 #data[key] = user_input #on attribue la nouvel key a data automatiquement dans chaque tour de la boucle.
                                    #with open(os.path.basename(json_files[serv_amod]), 'w') as f: #met le fichier choisi en mode write et le me dans la variable f.
                                    #json.dump(data, f, indent=4) #ici on garde data dans le fichier à modifier.
                                        #print("Fichier modifié avec succès!")
                            
                else:
                    print(Fore.RED + Style.BRIGHT + "Entrée invalide, réessayez..." + Style.RESET_ALL)
                    continue
            except ValueError:
                print(Fore.RED + Style.BRIGHT + "Entrée invalide, réessayez..." + Style.RESET_ALL)
                continue
            

    elif option == 3:

          list_conf()
 

    
    elif option == 4:
        json_files = [f for f in os.listdir(dir_path) if f.endswith('.json')] #on charge la variable à nouveau, sinon quand on revient de créer un fichier la function pour supprimer ne trouve pas le fichier. 
        print(Fore.CYAN + Style.BRIGHT + supprimer_conf + Style.RESET_ALL) 
        print("""
---------######---------
----################----
------------------------
-----##############-----
-----###-##--##-###-----
-----###-##--##-###-----
------##-##--##-##------
------##-##--##-##------
------############------
""")       
    
        
        print("")
        
        while True:
            json_files = [f for f in os.listdir(dir_path) if f.endswith('.json')] #on charge la variable à nouveau, sinon quand on revient de effacer un fichier la function pour supprimer garde encore la liste de fichier pas au jour. 
            list_conf()
            print("")
            

            serv_asup = input(Fore.CYAN + "- Choisir le numéro de fichier à supprimer\n- 'r' pour revenir au menu\n--->: " + Style.RESET_ALL)

            if serv_asup == 'r':
                break
                
            else:
                try:
                    serv_asup = int(serv_asup)

                except ValueError:
                    print(Fore.RED + Style.BRIGHT + "Entrée invalide, réessayez" + Style.RESET_ALL)
                    continue

                if not 1 <= serv_asup <= len(json_files): #ici on gère les entrées des l'utilisateur que sont plus grand que la quantité des fichiers, ou négatif 
                    print(Fore.RED + Style.BRIGHT + "Erreur! Les numéros de fichiers doivent être compris entre 1 et", len(json_files))
                    continue        


                                        
             
                print("")
                print("")
                print(Fore.CYAN + "----------------------------------------------------------------------------------------" + Style.RESET_ALL)
                confirmation = input(Fore.CYAN + f"Nom du fichier: {os.path.basename(json_files[serv_asup - 1])} à supprimer, Voulez vous supprimer le fichier o/n: " + Style.RESET_ALL) #imprime le nom du fichier, pour ça utilise la fonctionnalité os.path.basename dans le fichier choisi
                while True:
                    if confirmation == "o":
                        os.remove(json_files[serv_asup - 1])
                        print(Style.BRIGHT + Fore.GREEN + "\nFichier supprimé avec succès!!\n\n" + Style.RESET_ALL)                                               
                        break
                    if confirmation == "n":
                        print(Fore.YELLOW + "\n...Fichier pas supprimé...\n\n" + Style.RESET_ALL)
                        list_conf()
                        break

                    else:
                        print(Fore.RED + Style.BRIGHT + "Entrée invalide, réessayez" + Style.RESET_ALL)
                        break



    elif option == 5:
        print(Fore.CYAN + Style.BRIGHT + sauvegarde_conf + Style.RESET_ALL) 
        print(selection_5)
        print("")

        while True:
            try:
                option_5 = int(input(Fore.CYAN + "Entrez une option: " + Style.RESET_ALL))

            except ValueError:
                print(Fore.RED + Style.BRIGHT + "Error!...Entrez soit 1, 2 ou 3..." + Style.RESET_ALL)
                continue

            if option_5 == 1:
                               
                if server_config: #Vérifie si la variable est vide ou non.

                    Nom_fichier_conf = input(Fore.CYAN + "Entrer le nom du fichier (suggestion: nom du serveur récemment crée): ")
                    Nom_fichier_conf_choisi = Nom_fichier_conf + ".json" 
                
                    

                    with open(Nom_fichier_conf_choisi, 'w') as f: #crée le fichier.json et le met en mode write.
                        json.dump(server_config, f, indent=4) #dump: écris ajoute l'information dans le fichier, indent donne le forma pour qu'il soit lisible en json
                            
    
                    print(Style.BRIGHT + Fore.GREEN + "Fichier sauvegardé avec succès!" + Style.RESET_ALL)
                    print(selection_5)
                    
                    
                else:
                    print(Fore.RED + Style.BRIGHT + "Erreur: Aucun serveur configuré à sauvegarder." + Style.RESET_ALL)
                    

            elif option_5 == 2:
                if data_mod:

                    with open(json_files[serv_amod - 1], 'w') as f: #Prends le fichier sélectionné par l'utilisateur en option 2, le met dans Write mode et le met dans la variable f
                        json.dump(data_mod, f, indent=4) #prends la variable mod8data crée dans l'option 2 avec les modifications faites et le met dans le fichier dans le fichier avec le forma correct.
                    print(Style.BRIGHT + Fore.GREEN + "Fichier sauvegardé avec succès!" + Style.RESET_ALL)
                    print("")
                    print(selection_5)
                else:
                    print(Fore.RED + Style.BRIGHT + "Erreur: Aucun serveur modifié à sauvegarder." + Style.RESET_ALL)

            
            elif option_5 == 3:
                break

            else:
                print(Fore.RED + Style.BRIGHT + "Error!...Entrez soit 1, 2 ou 3..." + Style.RESET_ALL)

            
        

    elif option == 6:

        #Function que liste tous les fichier et dossier de sauvegarde:
        def list_dossier_restauration(): #on crée la function
            path_dossier = './Points_de_Restauration' #Le dossier où la function va chercher les sub-dossier et fichiers.
            count = 0 #on défini la variable qui est utilisé pour compter les repertoires et les fichiers.

            for root, dirs, files in os.walk(path_dossier): #boucle qu'envoi trois valeurs, (ici j'ai choisi root, dirs et files, mais ça peut être nommé à volonté. la fonctionnalité os.walk attends toujours 3 variables): root (le chemin actuel), dirs (une liste de répertoires dans le chemin actuel) et files (une liste de fichiers dans le chemin actuel)
                if root != path_dossier: #ici on met la condition que seulement soit imprime le compteur si le dossier est different au dossier racine, sinon on obtiens au haut de la liste "0. Points_de_Restauration:" et n'est pas nécessaire.
                    count += 1 #si el if precedent est true on incrémente de 1 à chaque tour de la boucle.
                    print("______________________________") #améliore la lisibilité.
                    print("")
                    print(f"{count}. {os.path.basename(root)}:") #affiche le N° du compteur un "."" et le nom de repertoire sans le path avec la function os.path.basename. et ":" à la fin.
                    print("")
                    for file in files:
                        print(f"    - {file}: ") #va faire la boucle à l’intérieur de chaque sub-dossier et imprimer les fichiers (on mets des espaces pour que soit plus lisible).
                        
                        if file.endswith(".txt"):  # Verifie si c'est un .txt
                            with open(os.path.join(root, file), "r") as f: #ouvre le fichier .txt
                                print (f"               `----> {f.read()}") #l'affiche et améliore la lisibilité.
                                print("")
                        
                        if file.endswith(".json"):
                            #file_path = os.path.join(root, file)                           
                            #with open(file_path, 'r') as f:
                            with open(os.path.join(root, file), 'r') as f: #j’utilise le même code que pour afficher la liste de fichiers conf.
                                data = json.load(f)
                                print("")               
                                for key, value in data.items():
                                    print(f"       {key}: {value}")
                            print("")   
                            
            
            subfolders = [f for f in os.listdir(path_dossier) if os.path.isdir(os.path.join(path_dossier, f))] #liste avec tous les sub-dossier pour les sélectionner dans l’option2
            
            return subfolders, path_dossier
                
            

        def function_nvo_dossier(): #Function que crée un nouveau dossier à l’intérieur du dossier "points de restorations"
                     
                    nom_sauvegarde = input(Fore.CYAN + "\n------------------------------------------\nEntrer un nom pour le point de sauvegarde: ")
                    
                    from datetime import datetime #fonctionnalité pour récupérer la date et l'heure
                    now = datetime.now()
                    jour_heure = now.strftime("%d-%m-%Y_%Hh%Mmin") #j'ai du modifier le format pour qu'il soit valid en windows.
                        
                    dossier_sauvegarde = os.path.join('./Points_de_Restauration', nom_sauvegarde + "_" + jour_heure) #Ici avec la function path join gère la concatenation du nom de mon nouveau dossier, et son path. j'ai du modifier le format pour qu'il soit valid en windows.
                    os.mkdir(dossier_sauvegarde) #Ici va créer le dossier avec la variable que je viens de créer au haut.
                    

                    commentaire = input("---------------------------------------------------\nEntrer un commentaire pour le point de restauration: " + Style.RESET_ALL)
                    with open(os.path.join(dossier_sauvegarde, 'Commentaire.txt'), "w") as f:  #ici aussi, on dois utiliser "os.path.join" pour bien formater mon path pour pouvoir créer mon fichier commentaire.txt
                        f.write(commentaire) # Ici écris le commentaire dans le fichier .txt
                    print("")
                    print(Style.BRIGHT + Fore.GREEN + "\nPoint de restauration enregistrée avec succès!\n\n" + Style.RESET_ALL)

                        

                    return dossier_sauvegarde #ici ça permets d'utiliser l'information de la function dans une autre part de mon code.
                    


        
        json_files = [f for f in os.listdir(dir_path) if f.endswith('.json')] #Variable a tester, par fois dans certaine condition si je ne mets pas cette variable ici, il ne fait pas un refresh quand il y a des modifications dans les fichier conf en "."
        list_conf() 
        print(Fore.CYAN + Style.BRIGHT + restaurer_conf + Style.RESET_ALL)
        
        while True:



            print(selection_6)
            
            try:
                option_6 = int(input(Fore.CYAN + "Entrez une option: " + Style.RESET_ALL))

            except ValueError:
                print(Fore.RED + Style.BRIGHT + "Erreur! Entrée invalide. Options possibles: 1,2,3 ou 4." + Style.RESET_ALL)
                continue

            if option_6 == 1:
                json_files = [f for f in os.listdir(dir_path) if f.endswith('.json')] #Si je ne mets pas cette variable ici, il ne fait pas un refresh quand il y a des modifications dans les fichier conf en "."
                list_conf() #On appel la function pour lister les fichier conf.
                print("")


                while True:
                    
                                         
                        fichier_conf_rest = input(Fore.CYAN + "- Entrer le nombre de fichier à sauvegarder \n- Si plusieurs séparer par ',' (Ex: 1, 2, 3) \n- 'all' pour sélectionner tous\n- 'r' Pour retourner au menu precedent.\n\nEntrer votre choix: " + Style.RESET_ALL)

                
                                                       
                        if fichier_conf_rest == "all":
                            
                            dossier_path1 = function_nvo_dossier() #charge la variable avec le contenu crée par function_nvo_dossier() pour être utilisé dans la boucle suivante et aussi lance la function_nvo_dossier()
                                                    
                            for fichier in json_files:
                                shutil.copy(os.path.join(dir_path, fichier), os.path.join(dossier_path1, fichier)) #Fonctionnalité shutil pour copier coller et os.path.join pour lier le path au nim du fichier.
                            
                        

                        elif ',' in fichier_conf_rest: #Ici vérifie si dans l'entrée de l'utilisateur il a des ",". va les séparer les où il y a des ',' et les metre dans une liste. Mais avant il le transforme en un Int

                            
                            try:
                                fichier_conf_rest = [int(x) for x in fichier_conf_rest.split(',')] #Prends les entrées de l'utilisateur, et si sont entiers, séparés par , va a couper dans la , et metre les int dans une liste.
                            except ValueError:
                                print(Fore.RED + Style.BRIGHT + "Erreur! Les valeurs doivent être des entiers." + Style.RESET_ALL) 
                                continue
                            if not all(1 <= x <= len(json_files) for x in fichier_conf_rest): #ici on gère les entrées des l'utilisateur que sont plus grand que la quantité des fichiers, ou négatif 
                                print(Fore.RED + Style.BRIGHT + f"Erreur! Les numéros de fichiers doivent être compris entre 1 et {len(json_files)}" + Style.RESET_ALL)
                                continue 

                            dossier_path2 = function_nvo_dossier() #charge la variable avec le path de mon nouveau dossier crée par function_nvo_dossier() 

                            for fichiers_rest_choisi in fichier_conf_rest:
                                fichier_path = os.path.join(dir_path, json_files[fichiers_rest_choisi - 1])                  
                                shutil.copy(fichier_path, dossier_path2)
                            
                                
                   
                        
                        elif fichier_conf_rest.isdigit(): #Si  l'utilisateur entre un seul int, la function le met dans une liste.  Mais avant il le transforme en un Int
                            
                            try:

                                fichier_conf_rest = int(fichier_conf_rest) #transforme la variable en Int
                            except ValueError:
                                print(Fore.RED + Style.BRIGHT + "Erreur! Les valeurs doivent être des entiers." + Style.RESET_ALL) 
                                continue

                            if not 1 <= fichier_conf_rest <= len(json_files): #ici on gère les entrées des l'utilisateur que sont plus grand que la quantité des fichiers, ou négatif 
                                print(Fore.RED + Style.BRIGHT + f"Erreur! Le numéro de fichier doive être compris entre 1 et {len(json_files)}" + Style.RESET_ALL)
                                continue

                            dossier_path3 = function_nvo_dossier()

                            fichier_path = os.path.join(dir_path, json_files[fichier_conf_rest - 1])
                            shutil.copy(fichier_path, dossier_path3)
                            
                        elif fichier_conf_rest == 'r':
                            break
                        
                        else:                                   #pour tout autre entrée different d'une entrée vide donne un erreur.
                            print(Fore.RED + Style.BRIGHT + "Erreur : Entrée invalide!" + Style.RESET_ALL)
            

            if option_6 == 2:
        
                print("")
                print("----------------------------------")
                print("Liste des points de restauration: ")
                print("----------------------------------")
                print("")
                print("")
                
                
                subfolders, path_dossier = list_dossier_restauration() #ici je défini les variable qui va contenir ma liste de sub_dossiers qui se trouve en list_dossier_restauration() et aussi la va afficher.
                
                              
                while True:

                    try:
                        print("")
                        selection_point_a_restaurer = input(Fore.CYAN + "Entrez le N° de point de restauration à restaurer\n(si les fichiers existent ils seront écrasé)\n- 'r' Pour retourner au menu precedent : " + Style.RESET_ALL)
                        
                        if selection_point_a_restaurer == 'r': 
                            break
                        
                        selection_point_a_restaurer = int(selection_point_a_restaurer) #on transforme le str en int
                        
                        if 1 <= selection_point_a_restaurer <= len(subfolders):

                             

                        
                            dossier_pdr_cible = subfolders[selection_point_a_restaurer - 1] #on établie la position dans la liste pour identifier le dossier à restaurer.
                        

                            json_files_in_pdr_src = glob.glob(os.path.join(path_dossier, dossier_pdr_cible, '*.json')) # Trouver tous les fichiers JSON à l’intérieur du dossier_pdr_cible

                        
                            for file in json_files_in_pdr_src:  # Iteration que copie tous les fichiers JSON dans "."
                                shutil.copy(file, dir_path)

                            print(Style.BRIGHT + Fore.GREEN +"Restauration réussi!" + Style.RESET_ALL)
                            list_conf()
                        
                        else:
                            print(Fore.RED + Style.BRIGHT + f"Erreur : le numéro de fichier doive être compris entre 1 et {len(subfolders)}" + Style.RESET_ALL) 
                            continue
                        

                        
                   
                    except ValueError:
                        print(Fore.RED + Style.BRIGHT + "Erreur : les valeurs doivent être des N° et non de lettres." + Style.RESET_ALL) 
                        continue
                    


            if option_6 == 3:
                
                print("")
                print("----------------------------------")
                print("Liste des points de restauration: ")
                print("----------------------------------")
                print("")
                print("")
                
                
                subfolders, path_dossier = list_dossier_restauration() #ici je défini les variable qui va contenir ma liste de sub_dossiers qui se trouve en list_dossier_restauration() et aussi la va afficher.
                    
                
                while True:
                    
 
                    try:
                        print("")
                        selection_point_a_restaurer = input(Fore.CYAN + "Entrez le N° de point de restauration à supprimer\n- 'r' Pour retourner au menu precedent : " + Style.RESET_ALL)
                    
                    
                    
                        if selection_point_a_restaurer == 'r': 
                            break
                        
                        selection_point_a_restaurer = int(selection_point_a_restaurer) #on transforme le str en int 
                        
                        if not 1 <= selection_point_a_restaurer <= len(subfolders):
                            print(Fore.RED + Style.BRIGHT + f"Erreur! Le numéro de fichier doive être compris entre 1 et{len(subfolders)}" + Style.RESET_ALL)
                            continue
                        
                        while True:
                            try:
                                confirmation = input(Fore.YELLOW + f"-----------------------------------------------------------------------------------------------------------------------\nNom du Point de restauration à supprimer: {subfolders[selection_point_a_restaurer - 1]}, Voulez vous supprimer le fichier o/n: " + Style.RESET_ALL )
                                if confirmation == 'o':
                                    dossier_pdr_cible = subfolders[selection_point_a_restaurer - 1] #on établie la position dans la liste pour identifier le dossier à supprimer.
                        
                                    shutil.rmtree(os.path.join(path_dossier, dossier_pdr_cible))#Supprime le dossier
                                            
                                    print(Style.BRIGHT + Fore.GREEN +"\n!!!!!!!!!!!!!!!!!!!\n Suppression réussi\n!!!!!!!!!!!!!!!!!!!" + Style.RESET_ALL)
                                    subfolders, path_dossier = list_dossier_restauration()                                   
                                    break
                                    
                                elif confirmation == 'n':
                                    print(Fore.CYAN + "Dossier pas supprimé..." + Style.RESET_ALL)
                                    subfolders, path_dossier = list_dossier_restauration()
                                    break
                                else:
                                    print(Fore.RED + Style.BRIGHT + "Reponse possibles: 'o' or 'n'...réessayez" + Style.RESET_ALL)
                                    continue
                            except ValueError:
                                print(Fore.RED + Style.BRIGHT + "Reponse possibles: 'o' or 'n'...réessayez" + Style.RESET_ALL)
                                break
                        
                        
                        
                   
                    except ValueError:
                        print(Fore.RED + Style.BRIGHT + "Erreur! Les valeurs doivent être des N°" + Style.RESET_ALL) 
                        continue

 
                           
            if option_6 == 4:
                break

            if not 1 <= option_6 <= 4:
                print(Fore.RED + Style.BRIGHT + "Options possibles: 1,2,3 ou 4. Réessayez: " + Style.RESET_ALL)
    
    elif option == 7:
        
        print(Fore.CYAN + Style.BRIGHT + scan_conf + Style.RESET_ALL)
        
        nm = nmap.PortScanner() # Démarre l'objet PortScanner
        
        while True:
            
            


            print("")
            ip_range = input(Fore.CYAN + "Entrez la plage d'adresses IP à scanner (ex : 192.168.1.1/24)\n- 'r' Pour revenir au menu : ") # Définie le  la porté de le scan IP  (e.g. 192.168.1.0/24)
            print("")
            print("-------------------------------------------------------------------------------" + Style.RESET_ALL)
            print("")
    

            if ip_range == 'r':
                break
                
                
            try:
                
                nm.scan(hosts=ip_range, arguments='-sV -p 1-1024') # -sV : scan et identifie la version de chaque service. -p scan les ports dans l'IP range.

                # Afficher les résultat 
                print(Fore.YELLOW + Style.BRIGHT + "Analyse terminée...Résultats du scan:" + Style.RESET_ALL)
                print("")
                for host in nm.all_hosts(): #nm.all_hosts() nous retourne une liste avec tous les hosts (ip address) qui Nmap a scanné.
                    print(f"Host: {host}") # Affiche chaque host et sa variable
                    for proto in nm[host].all_protocols(): # Retourne une liste avec tous les protocoles détectés dans le host courent 
                        print(f"  Protocol: {proto}") # Affiche chaque protocole et sa variable
                        lport = nm[host][proto].keys() # Obtiens une liste avec tous les port ouverts dans le host courent et le protocol
                        for port in lport:
                            print(f"    Port: {port} ({nm[host][proto][port]['state']})") # Affiche le numéro de port et son status
                            print(f"    Service: {nm[host][proto][port]['name']}") # Affiche le nom du service up dans le port courent
                            print(f"    Version: {nm[host][proto][port]['version']}") # Affiche la version du service up dans le port courent.
            
            except ValueError:
                    print("Error...")
                    break
        
        
    
    
        
    else:
        print(Fore.RED + Style.BRIGHT +"Erreur! Entrez une option entre 1 et 7" + Style.RESET_ALL) #Erreur s'il n'est pas entre 1 et 7
        



