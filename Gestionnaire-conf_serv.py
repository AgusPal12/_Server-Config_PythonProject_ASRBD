import os
import json
import pprint

Selection = """
---------Menu---------------
1. Ajouter une configuration 
2. Modifier une configuration 
3. Supprimer une configuration 
4. Lister les configurations 
5. Sauvegarder les configurations 
6. Restaurer les configurations 
7.Découverte de Services et de Serveurs 
"""

selection_5 = """
-------Option-De-Sauvegarde--------------------------
1. Sauvegarder le nouveau Serveur
2. Sauvegarder les modifications du serveur existant
-----------------------------------------------------
"""
print(Selection)

while True: #Va créer la boucle, pour revenir toujours sélectionner une option valide.
    try: #ici le try/except va nous créer le message d'error si l'option choisi est autre chose q'un int
        option = int(input("Entrez votre sélection : "))

    except ValueError:
        print("Entrez un option de 1 au 7 svp")
        continue

    if option == 1:
        
        nom_ser = input("Entrez le nom du serveur : ") #enregistre le nom du serveur dans la variable nom_ser

        ip_ser = input("Entrez l'adresse IP : ") #enregistre l'IP dans la variable ip_ser. (faire un input valid)
           
        sys_exp = input("Entrez le système d'exploitation : ") #enregistre le système d’exploitation dans la variable sys_exp

        services_up = [input("Entrez les services en cours d'exécution (séparés par des virgules) :")] #enregiste les services qui sont en cours d'exécution dans la liste services_up (faire invalid si mauvais format) 

        server_config = {"Name":nom_ser, "Ip": ip_ser , "Systeme":sys_exp, "Services UP":services_up} #met tout dans un dictionnaire
        print("")
        print("Configuration ajoutée avec succès, oubliez pas de la sauvegarder avant d'ajouter une autre configuration!") #Une fois tous les paramètres ajoutée (faut qu'il le garde en mémoire pour qu'apres avec l'option 5 la config reste et si exit, demander si sauvegarde), idée: creer un deuxieme fichier json genre server_config_tmp)
        print(Selection)
    elif option == 2:
        print("") #pour faire de l'espace(chercher comment faire plus propre)
        print("Liste des fichiers de configuration")
        print("")
        dir_path = '.' #variable pour stocker le repertoire où la ligne suivante va chercher les fichier .json
        json_files = [f for f in os.listdir(dir_path) if f.endswith('.json')] #la function os.listdir(dir_path) retourne les fichier et repertoires qui sont dans le repertoire (dir_path)...."f for f in..." est un boucle qui va itérer dans la liste doné par os.listdir(dir_path)....if f.endswith('.json') c'est un conditional qui filtre la liste avec les fichier qui se terminent par .json
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

            print("Modifications faites!")
            print("")
            print("N'oublie pas de sauvegarder avec l'option 5")
            print("..........................................")
            print(Selection)
            print("..........................................")
                
                    #SI ON VEUT QUE çA SOIT SAUVEGARDé DIRECTEMENT PENDANT QU'ON MODIFIE
                    #data[key] = user_input #on attribue la nouvel key a data automatiquement dans chaque tour de la boucle.
                #with open(os.path.basename(json_files[serv_amod]), 'w') as f: #met le fichier choisi en mode write et le me dans la variable f.
                    #json.dump(data, f, indent=4) #ici on garde data dans le fichier à modifier.
                #print("Fichier modifié avec succès!")
                            
            
            

    elif option == 3:
        print("En cour d'integration, voulez ressayer une autre option")
        
    
    elif option == 4:
        print("En cour d'integration, voulez ressayer une autre option")
        
    elif option == 5:

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
                print(Selection)

            elif option_5 == 2:
                with open(json_files[serv_amod], 'w') as f:
                    json.dump(data_mod, f, indent=4)
                print("Fichier sauvegardé avec succès!")

            else:
                print("Entrez soit 1, soit2 ")

                



    elif option == 6:
        print("En cour d'integration, voulez ressayer une autre option")
        
    elif option == 7:
        print("En cour d'integration, voulez ressayer une autre option")
        
    else:
        print("Option non valide, voulez réessayer")
        option = int(input("Entrez votre sélection : "))



