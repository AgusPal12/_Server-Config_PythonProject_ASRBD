with open('server_config.json', 'w') as f: #crée le fichier.json et le met en mode write.
            json.dump(server_config, f, indent=4) #dump: écris ajoute l'information dans le fichier, indent donne le forma pour qu'il soit lisible en json




Option 5
            
Question_sauvegarde = int(input("Entrez '1' pour sauvegarder le nouveau serveur; Entrez '2' pour sauvegardez les modification effectuées sure l\'ancien serveur" ))

if Question_sauvegarde == 1:
    Nom_fichier_conf = input("Entrez le nom du fichier de sauvegarde: ")
        Nom_fichier_conf_choisi = Nom_fichier_conf + ".json" 
        with open(Nom_fichier_conf_choisi, 'w') as f: #crée le fichier.json et le met en mode write.
            json.dump(server_config, f, indent=4) #dump: écris ajoute l'information dans le fichier, indent donne le forma pour qu'il soit lisible en json
        #print("En cour d'integration, voulez ressayer une autre option")
        
        print("Fichier sauvegardé avec succès!")

elif Question_sauvegarde == 2:
    with open(Nom_fichier_conf_existent, 'w') as f: #crée le fichier.json et le met en mode write.
            json.dump(variable_que_stocke_les_modif, f, indent=4) #dump: écris ajoute l'information dans le fichier, indent donne le forma pour qu'il soit lisible en json
        #print("En cour d'integration, voulez ressayer une autre option") 

else:
    print(Entrée invalide)


