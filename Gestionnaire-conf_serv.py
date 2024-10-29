import os
import json
import pprint
import nmap
import shutil

dir_path = '.' #variable pour stocker le repertoire où la ligne suivante va chercher les fichier .json
json_files = [f for f in os.listdir(dir_path) if f.endswith('.json')] #la function os.listdir(dir_path) retourne les fichier et repertoires qui sont dans le repertoire (dir_path)...."f for f in..." est un boucle qui va itérer dans la liste doné par os.listdir(dir_path)....if f.endswith('.json') c'est un conditional qui filtre la liste avec les fichier qui se terminent par .json


server_config = """

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
3. Revenir au Menu
-----------------------------------------------------
"""

def list_conf(): #Ici je define une function, car j'ai vais avoir besoin de la meme fonctionnalité pour l'option 6

            print(fichier_conf_liste)
            json_files = [f for f in os.listdir(dir_path) if f.endswith('.json')] #on charge la variable à nouveau, sinon quand on revient d'effacer un fichier la function pour lister ne trouve pas le fichier. 
            print("")
            print("Voici toutes les configurations des serveurs:")
            print("")
            print("----------------------")

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
            


print(server_config)
print(Selection)

while True: #Va créer la boucle, pour revenir toujours sélectionner une option valide.
    try: #ici le try/except va nous créer le message d'error si l'option choisi est autre chose q'un int
        option = int(input("Entrez votre sélection : "))
        print("")
        print("--------------------------------")

    except ValueError:
        print("Entrez un option de 1 au 7 svp")
        print("")
        continue

    
    
    if option == 1:
        print(fichier_conf)
        print("")
        nom_ser = input("Entrez le nom du serveur : ") #enregistre le nom du serveur dans la variable nom_ser

        ip_ser = input("Entrez l'adresse IP : ") #enregistre l'IP dans la variable ip_ser. (faire un input valid)
           
        sys_exp = input("Entrez le système d'exploitation : ") #enregistre le système d’exploitation dans la variable sys_exp

        services_up = [input("Entrez les services en cours d'exécution (séparés par des virgules) :")] #enregiste les services qui sont en cours d'exécution dans la liste services_up (faire invalid si mauvais format) 

        server_config = {"Name":nom_ser, "Ip": ip_ser , "Systeme":sys_exp, "Services UP":services_up} #met tout dans un dictionnaire
        print("")
        print("""

 /$$
| $$
| $$
| $$
|__/
    
 /$$
|__/

Configuration pre-enregistré. OPTION 5 pour Sauvegarder!""") #Une fois tous les paramètres ajoutée (faut qu'il le garde en mémoire pour qu'apres avec l'option 5 la config reste et si exit, demander si sauvegarde), idée: creer un deuxieme fichier json genre server_config_tmp)
        print(Selection)
    
    
    
    
    elif option == 2:
        print(modifier_une_conf)
        print("Liste des fichiers de configuration:")
        print("")
        json_files = [f for f in os.listdir(dir_path) if f.endswith('.json')]
        for i, element in enumerate(json_files, start=1): #position des elements dans la liste en commencent par 1 et non 0
            print(f"{i}. {element}") #imprime l'element i avec un string "." plus le numéro de 
        
        print("")
        serv_amod = int(input("Choisir le numéro fichier de configuration qui vous voulez modifier: "))
        print("")
        print("Voici l'information du fichier:")
        print("")
        print("-------------------------------")
        serv_amod -= 1 #l’opérateur -= soustrait (dans ce cas 1) x quantité d'elements dans la liste indexée. Important plus tard quand il va afficher la liste de fichier dans le dossier de manière qu'il commence par 1
        with open(json_files[serv_amod], 'r') as f: #ouvre le json_file dans la position choisi (serv_amod), cette fois en mode "r" read et le met dans la variable f
            data = json.load(f) #Charge la variable "data" avec le contenu (tout ça fait la function json.load) du fichier antérieurement mis das la variable f.
            print(f"Nom du fichier: {os.path.basename(json_files[serv_amod])}") #imprime le nom du fichier, pour ça utilise la fonctionnalité os.path.basename dans le fichier choisi
            
            #print(json.load(f)) #Un autre manier de le afficher
            #data = json.load(f) #Un autre manier de le afficher
            #pprint.pprint(data)
            
            print("")
            for key, value in data.items(): #boucle qui va itérer dans le contenu (data) du dictionnaire
                print(f"{key}: {value}") #Ici on le donne le format key: value pour qu'il soit lisible.
            print("------------------------------")
            print("")
            print("Modification ligne par ligne: ")
            print("")
            data_mod = {}
            for key, value in data.items(): #fait une boucle pour et passe par item de "data"
                print(f"{key}: {value}") #imprime la ligne qui va être modifié
                print("")
                user_input = input(f"Entrer une nouvelle valeur pour {key} (ou entrer pour conserver l'original): ") #charge la variable avec l'input de l'utilisateur. si pas d'input passe a la ligne suivante sans modifier l'actuel.
                print("")
                if user_input: #S'il y a eu un input
                    data_mod[key] = user_input #on remplace la variable par l'input de l'utilisateur (que s'il a mis quelque chose)
                else:
                    data_mod[key] = value #sinon, on laisse la même valeur
            print("")
            print("""

 /$$
| $$
| $$
| $$
|__/
    
 /$$
|__/

Modifications pre-enregistré. OPTION 5 pour Sauvegarder!""")
            print("")
            print(Selection)
            print("..........................................")
                
                    #SI ON VEUT QUE çA SOIT SAUVEGARDé DIRECTEMENT PENDANT QU'ON MODIFIE
                    #data[key] = user_input #on attribue la nouvel key a data automatiquement dans chaque tour de la boucle.
                #with open(os.path.basename(json_files[serv_amod]), 'w') as f: #met le fichier choisi en mode write et le me dans la variable f.
                    #json.dump(data, f, indent=4) #ici on garde data dans le fichier à modifier.
                #print("Fichier modifié avec succès!")
                            
            
            

    elif option == 3:

          list_conf()
          print(Selection) 
        
        
    
    
    
    elif option == 4:
        json_files = [f for f in os.listdir(dir_path) if f.endswith('.json')] #on charge la variable à nouveau, sinon quand on revient de créer un fichier la function pour supprimer ne trouve pas le fichier. 
        print(supprimer_conf)
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
        print("Liste des fichiers:")
        print("...................")
        
        for i, element in enumerate(json_files, start=1): #position des elements dans la liste en commencent par 1 et non 0
            print(f"{i}. {element}") #imprime l'element i avec un string "." plus le numéro de 
        
        print("")
        serv_asup = int(input("Choisir le numéro fichier de configuration qui vous voulez supprimer: "))
        print("")
        print("")
        print("-------------------------------")
        serv_asup -= 1 #l’opérateur -= soustrait (dans ce cas 1) x quantité d'elements dans la liste indexée. Important plus tard quand il va afficher la liste de fichier dans le dossier de manière qu'il commence par 1
        confirmation = input(f"Nom du fichier: {os.path.basename(json_files[serv_asup])} à supprimer, Voulez vous supprimer le fichier o/n: ") #imprime le nom du fichier, pour ça utilise la fonctionnalité os.path.basename dans le fichier choisi
        while True:
            if confirmation == "o":
                os.remove(json_files[serv_asup])
                print("Fichier supprimé avec succès")
                break
            elif confirmation == "n":
                print("Fichier pas supprimé")
                break
        print(Selection)
    
    
    
    
    
    elif option == 5:
        print(sauvegarde_conf)
        print(selection_5)
        print("")

        while True:
            try:
                option_5 = int(input("Entrez une option: "))

            except ValueError:
                print("Entrez soit 1, soit2 ")
                continue

            if option_5 == 1:

                Nom_fichier_conf = input("Entrez le nom du fichier de sauvegarde (suggestion: nom du serveur): ")
                Nom_fichier_conf_choisi = Nom_fichier_conf + ".json" 
                with open(Nom_fichier_conf_choisi, 'w') as f: #crée le fichier.json et le met en mode write.
                    json.dump(server_config, f, indent=4) #dump: écris ajoute l'information dans le fichier, indent donne le forma pour qu'il soit lisible en json
                #print("En cour d'integration, voulez ressayer une autre option")
                
                print("Fichier sauvegardé avec succès!")
                print(selection_5)

            elif option_5 == 2:
                with open(json_files[serv_amod], 'w') as f: #Prends le fichier sélectionné par l'utilisateur en option 2, le met dans Write mode et le met dans la variable f
                    json.dump(data_mod, f, indent=4) #prends la variable mod8data crée dans l'option 2 avec les modifications faites et le met dans le fichier dans le fichier avec le forma correct.
                print("Fichier sauvegardé avec succès!")
                print("")
                print(selection_5)
            
            elif option_5 == 3:
                break

            else:
                print("Entrez soit 1, soit 2, soit 3")

            
        print(Selection)

    elif option == 6:
        json_files = [f for f in os.listdir(dir_path) if f.endswith('.json')]
        list_conf() 
        print(restaurer_conf)
        print(selection_6)
        while True:
            try:
                option_6 = int(input("Entrez une option: "))

            except ValueError:
                print("Options possibles: 1, 2 ou 3, Réessayez: ")
                continue

            if option_6 == 1:
                json_files = [f for f in os.listdir(dir_path) if f.endswith('.json')]
                list_conf() #On appel la function pour lister les fichier conf.
                print("")
                


                def function_nvo_dossier():
                    nom_sauvegarde = input("Entrer un nom pour le point de sauvegarde: ")
                    
                    from datetime import datetime #fonctionnalité pour récupérer la date et l'heure
                    now = datetime.now()
                    jour_heure = now.strftime("%d-%m-%Y_%H-%M") #j'ai du modifier le format pour qu'il soit valid en windows.
                        
                    dossier_sauvegarde = os.path.join('./Points_de_Restauration', nom_sauvegarde + "_" + jour_heure) #Ici avec la function path join gère la concatenation du nom de mon nouveau dossier, et son path. j'ai du modifier le format pour qu'il soit valid en windows.
                    os.mkdir(dossier_sauvegarde) #Ici va créer le dossier avec la variable que je viens de créer au haut.
                    

                    commentaire = input("Entrer un commentaire pour le point de restauration: ")
                    with open(os.path.join(dossier_sauvegarde, 'Commentaire.txt'), "w") as f:  #ici aussi, on dois utiliser "os.path.join" pour bien formater mon path pour pouvoir créer mon fichier commentaire.txt
                        f.write(commentaire) # Ici écris le commentaire dans le fichier .txt
                    print("Pont de restauration enregistrée avec succès!")

                    return dossier_sauvegarde #ici ça permets d'utiliser l'information de la function dans une autre part de mon code.
                        
        


                while True:
                    
                                         
                        fichier_conf_rest = input("Entres les nombre de fichiers à sauvegarder séparé par ',' (Ex: 1, 2, 3) ou all pour sélectionner tous: ")

                
                                                       
                        if fichier_conf_rest == "all":
                            
                            dossier_path1 = function_nvo_dossier() #charge la variable avec le contenu crée par function_nvo_dossier() pour être utilisé dans la boucle suivante et aussi lance la function_nvo_dossier()
                                                    
                            for fichier in json_files:
                                shutil.copy(os.path.join(dir_path, fichier), os.path.join(dossier_path1, fichier)) #Fonctionnalité shutil pour copier coller.
                            
                        

                        elif ',' in fichier_conf_rest: #Ici vérifie si dans l'entrée de l'utilisateur il a des ",". va les séparer les où il y a des ',' et les metre dans une liste. Mais avant il le transforme en un Int

                            
                            try:
                                fichier_conf_rest = [int(x) for x in fichier_conf_rest.split(',')] #Prends les entrées de l'utilisateur, et si sont entiers, séparés par , va a couper dans la , et metre les int dans une liste.
                            except ValueError:
                                print("Erreur : les valeurs doivent être des entiers.") 
                                continue
                            if not all(1 <= x <= len(json_files) for x in fichier_conf_rest): #ici on gère les entrées des l'utilisateur que sont plus grand que la quantité des fichiers, ou négatif 
                                print("Erreur : les numéros de fichiers doivent être compris entre 1 et", len(json_files))
                                continue 

                            dossier_path2 = function_nvo_dossier() #charge la variable avec le path de mon nouveau dossier crée par function_nvo_dossier() 

                            for fichiers_rest_choisi in fichier_conf_rest:
                                fichier_path = os.path.join(dir_path, json_files[fichiers_rest_choisi - 1])                  
                                shutil.copy(fichier_path, dossier_path2)
                            break
                                
                   
                        
                        elif fichier_conf_rest.isdigit(): #Si  l'utilisateur entre un seul int, la function le met dans une liste.  Mais avant il le transforme en un Int
                            
                            try:

                                fichier_conf_rest = int(fichier_conf_rest) #liste d'un seule element? try just avec ()
                            except ValueError:
                                print("Erreur : les valeurs doivent être des entiers.") 
                                continue

                            if not 1 <= fichier_conf_rest <= len(json_files): #ici on gère les entrées des l'utilisateur que sont plus grand que la quantité des fichiers, ou négatif 
                                print("Erreur : le numéro de fichier doive être compris entre 1 et", len(json_files))
                                continue

                            dossier_path3 = function_nvo_dossier()

                            fichier_path = os.path.join(dir_path, json_files[fichier_conf_rest - 1])
                            shutil.copy(fichier_path, dossier_path3)
                            break

                        elif fichier_conf_rest != "": #pour tout autre entrée different d'une entrée vide donne un erreur.
                            print("Erreur : Entrée invalide!")

                   
                                          

    
    
    elif option == 7:
        print(scan_conf)
        nm = nmap.PortScanner() # Crée un objet Nmap


        print("")
        ip_range = input("Entrez la plage d'adresses IP à scanner (ex : 192.168.1.1/24) : ") # Définie le  la porté de le scan IP  (e.g. 192.168.1.0/24)
        print("")
        print("-------------------------------------------------------------------------------")
        print("")

        nm.scan(hosts=ip_range, arguments='-sV -p 1-1024') # -sV : scan et identifie la version de chaque service. Scan the IP range

        # Afficher les résultat 
        print("Résultats du scan:")
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
        
        print(Selection)
    
    
        
    else:
        print("Option non valide, voulez réessayer")
        option = int(input("Entrez votre sélection : "))



