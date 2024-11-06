

from colorama import init, Fore, Back, Style

init()  # Initialize colorama

# Foreground colors
print(Fore.RED + 'some red text')
print(Fore.GREEN + 'some green text')
print(Fore.YELLOW + 'some yellow text')
print(Fore.BLUE + 'some blue text')
print(Fore.MAGENTA + 'some magenta text')
print(Fore.CYAN + 'some cyan text')
print(Fore.WHITE + 'some white text')

# Background colors
print(Back.RED + 'some red background text')
print(Back.GREEN + 'some green background text')
print(Back.YELLOW + 'some yellow background text')
print(Back.BLUE + 'some blue background text')
print(Back.MAGENTA + 'some magenta background text')
print(Back.CYAN + 'some cyan background text')
print(Back.WHITE + 'some white background text')

# Reset color
print(Style.RESET_ALL + 'reset color')

# Bold and italic
print(Style.BRIGHT + 'some bright text')
print(Style.DIM + 'some dim text')
print(Style.NORMAL + 'some normal text')
print(Style.RESET_ALL + 'reset style')

# Combine styles
print(Fore.RED + Style.BRIGHT + 'some bright red text')
print(Fore.GREEN + Style.DIM + 'some dim green text')
print(Fore.YELLOW + Style.NORMAL + 'some normal yellow text')





    if option == 1:
        print(Fore.CYAN + Style.BRIGHT + fichier_conf + Style.RESET_ALL)
        print("")
        
        try:
            nom_ser = input(Fore.CYAN + "Entrez le nom du nouveau serveur\nou 'r' pour revenir au menu : ") #enregistre le nom du serveur dans la variable nom_ser
            
            
            while True:
                try:

                    if nom_ser == 'r':
                        break
                    else:
            
                        ip_ser = input("Entrez l'adresse IP : ") #enregistre l'IP dans la variable ip_ser. (faire un input valid)
                    
                        sys_exp = input("Entrez le système d'exploitation : ") #enregistre le système d’exploitation dans la variable sys_exp

                        services_up = [input("Entrez les services en cours d'exécution (séparés par des virgules) :")] #enregistre les services qui sont en cours d'exécution dans la liste services_up (faire invalid si mauvais format) 

                        server_config = {"Name":nom_ser, "Ip": ip_ser , "Systeme":sys_exp, "Services UP":services_up} #met tout dans un dictionnaire
                        print("")
                        print(Fore.RED + Style.BRIGHT + """
                 /$$
                | $$
                | $$
                | $$
                |__/

                /$$
                |__/

Configuration pre-enregistré...\nOPTION 5 --> 1 pour Sauvegarder!""" + Style.RESET_ALL) #Une fois tous les paramètres ajoutée (faut qu'il le garde en mémoire pour qu'apres avec l'option 5 la config reste et si exit, demander si sauvegarde), idée: creer un deuxieme fichier json genre server_config_tmp)
                        
                        break

                        

                except ValueError:
                    break  
        except ValueError:
                    break














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
                continuer = input(Fore.CYAN + "--'Entrer'-- pour continuer\n'r' pour revenir au menu precedent: ")
                if continuer == 'r':
                    break
                
                if continuer == "":
                    while True: #Boucle pour filtrer toutes les entrées invalides, quand c'est valid, break et continue.
                        try:

                            print("")
                            serv_amod = int(input("Choisir le numéro fichier de configuration qui vous voulez modifier: " + Style.RESET_ALL))
                            
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
                        #data_mod = {}
                        for key, value in data.items(): #fait une boucle pour et passe par item de "data"                         
                            print(Fore.YELLOW + "|")                        
                            print("V")
                            print(f"{key}: {value}" + Style.RESET_ALL) #imprime la ligne qui va être modifié
                            print("")                
                            user_input = input(f"Entrer une nouvelle valeur pour {Fore.YELLOW + key + Style.RESET_ALL} (ou entrer pour conserver l'original): ") #charge la variable avec l'input de l'utilisateur. si pas d'input passe a la ligne suivante sans modifier l'actuel.
                            print("")
                            if user_input: #S'il y a eu un input
                                data_mod[key] = user_input #on remplace la variable par l'input de l'utilisateur (que s'il a mis quelque chose)
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
