
import json

Selection = """
Sélectionner l’action :

1. Ajouter une configuration 
2. Modifier une configuration 
3. Supprimer une configuration 
4. Lister les configurations 
5. Sauvegarder les configurations 
6. Restaurer les configurations 
7.Découverte de Services et de Serveurs 
"""
print(Selection)

while True: #Va créer la boucle, pour revenir toujours sélectionner une option valide.
    try: #ici le try/except va nous créer le message d'error si l'option choisi est autre chose q'un int
        option = int(input("Entrez votre sélection : "))

    except ValueError:
        print("Entrez un nombre entier svp")
        continue

    if option == 1:

        nom_ser = input("Entrez le nom du serveur : ") #enregistre le nom du serveur dans la variable nom_ser

        ip_ser = input("Entrez l'adresse IP : ") #enregistre l'IP dans la variable ip_ser. (faire un input valid)

        sys_exp = input("Entrez le système d'exploitation : ") #enregistre le système d’exploitation dans la variable sys_exp

        services_up = [input("Entrez les services en cours d'exécution (séparés par des virgules) :")] #enregiste les services qui sont en cours d'exécution dans la liste services_up (faire invalid si mauvais format) 

        server_config = {"name":nom_ser, "ip": ip_ser , "Systeme":sys_exp, "Services UP":services_up} #met tout dans un dictionnaire

        with open('server_config.json', 'w') as f: #crée le fichier.json et le met en mode write.
            json.dump(server_config, f, indent=4) #dump: écris ajoute l'information dans le fichier, indent donne le forma pour qu'il soit lisible en json

        print("Configuration ajoutée avec succès !") #Une fois tous les paramètres ajoutée (faut qu'il le garde en mémoire pour qu'apres avec l'option 5 la config reste et si exit, demander si sauvegarde), idée: creer un deuxieme fichier json genre server_config_tmp)
        exit()
    elif option == 2:
        print("En cour d'integration, voulez ressayer une autre option")
        option = int(input("Entrez votre sélection : "))
    elif option == 3:
        print("En cour d'integration, voulez ressayer une autre option")
        option = int(input("Entrez votre sélection : "))
    elif option == 4:
        print("En cour d'integration, voulez ressayer une autre option")
        option = int(input("Entrez votre sélection : "))
    elif option == 5:
        print("En cour d'integration, voulez ressayer une autre option")
        option = int(input("Entrez votre sélection : "))
    elif option == 6:
        print("En cour d'integration, voulez ressayer une autre option")
        option = int(input("Entrez votre sélection : "))
    elif option == 7:
        print("En cour d'integration, voulez ressayer une autre option")
        option = int(input("Entrez votre sélection : "))
    else:
        print("Option non valide, voulez réessayer")
        option = int(input("Entrez votre sélection : "))



