import os
dir_path = "."
json_files = [f for f in os.listdir(dir_path) if f.endswith('.json')]
#print(json_files)



"""def function_comparer_dossier():
    dir_path1 = "."  # replace with the path to the first directory
    dir_path2 = os.path.join(".\Points_de_Restauration", dossier_restaurer)
    json_files1 = set(f for f in os.listdir(dir_path1) if f.endswith('.json'))
    json_files2 = set(f for f in os.listdir(dir_path2) if f.endswith('.json'))
    if json_files1 == json_files2:
        print("ils sont égal")
        else:
        print("sont differents")"""

"""def list_dossier_restauration():
    dossiers_dans_pdr = [f for f in os.listdir('./Points_de_Restauration')]
    for i, folder in enumerate(dossiers_dans_pdr):
        print(f"{i+1}. {folder}")
list_dossier_restauration()
#path_to_check = './Points_de_Restauration'
#list_dossier_restauration(path_to_check)"""

dir_path_pdr = './Points_de_Restauration'
subfolders = [f.path for f in os.scandir(dir_path_pdr) if f.is_dir()]
    
for i, folder in enumerate(subfolders, start=1):
    print(f"{i}. {os.path.basename(folder)}")
    for subfolder in os.listdir(folder):
        if os.path.isdir(os.path.join(folder, subfolder)):
            print(f"{i}.{len(str(i))}. {subfolder}")

        print(i, folder, subfolder)
        break"""
            
            
            
#path_dossier = './Points_de_Restauration'
#for root, dirs, files in os.walk(path_dossier):
#    print(f"{root}:")
#    for file in files:
#        print(f"  {file}")
#        for dir in dirs:
#            print(f"  {dir}")



#list_dossier_restauration()



        def list_dossier_restauration(): #on crée la function
            path_dossier = './Points_de_Restauration' #Le dossier où la function va chercher les sub-dossier et fichiers.
            count = 0 #on défini la variable qui est utilisé pour compter les repertoires et les fichiers.

            for root, dirs, files in os.walk(path_dossier): #boucle qu'envoi trois valeurs, (ici j'ai choisi root, dirs et files, mais ça peut être nome a volonté. la fonctionnalité os.walk attends toujours 3 variables): root (le chemin actuel), dirs (une liste de répertoires dans le chemin actuel) et files (une liste de fichiers dans le chemin actuel)
                if root != path_dossier: #ici on met la condition que seulement soit imprime le compteur si le dossier est different au dossier racine, sinon on obtiens au haut de la liste "0. Points_de_Restauration:" et n'est nécessaire.
                    count += 1 #si el if precedent est true on incrémente de 1 à chaque tour de la boucle.
                    print("______________________________") #améliore la lisibilité.
                    print(f"{count}. {os.path.basename(root)}:") #affiche le N° du compteur un "."" et le nom de repertoire sans le path avec la function os.path.basename. et ":" à la fin.
                    print("")
                    for file in files:
                        print(f"    - {file}: ") #va faire la boucle à l’intérieur de chaque sub-dossier et imprimer les fichiers (on mets des espaces pour que soit plus lisible).
                        
                        if file.endswith(".txt"):  # Verifie si c'est un .txt
                            with open(os.path.join(root, file), "r") as f: #ouvre le fichier .txt
                                print (f"               `----> {f.read()}") #l'affiche et améliore la lisibilité.
                                print("")
                        
                        if file.endswith(".json"):
                            
                            with open(os.path.join(dir_path, file), 'r') as f: #j’utilise le même code que pour afficher la liste de fichiers conf.
                                data = json.load(f)
                                print("")               
                                for key, value in data.items():
                                    print(f"       {key}: {value}")
                            print("")   
                            print("")
            
            subfolders = [f for f in os.listdir(path_dossier) if os.path.isdir(os.path.join(path_dossier, f))] #liste avec tous les sub-dossier pour les sélectionner dans l’option2
            
            return subfolders, path_dossier




Option eliminar

        list_conf()
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
                print("Fichier supprimé avec succès!!")
                break
            elif confirmation == "n":
                print("Fichier pas supprimé")
                break