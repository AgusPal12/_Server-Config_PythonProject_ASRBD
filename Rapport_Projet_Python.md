# Gestionnaire des configurations de serveurs : "Server Config"

"Server Config" est un logiciel qui permet de manipuler des configurations de serveurs. Les configurations ont un format JSON, une par fichier, et contiennent un dictionnaire avec les clés : {Nom du serveur : , adresse IP : , système d'exploitation : , services en cours d'exécution :}.
On peut les créer, modifier, visualiser, supprimer, sauvegarder, et les restaurer. En plus, Server Config permet de scanner une plage d'adresses IP à la recherche de services et de serveurs à l'aide de NMAP.
Tout cela dans une interface accessible à tout utilisateur et exécutable de façon autonome pour Windows et Linux.

## Les fonctionnalités :

 - Ajouter une configuration : On va pré-remplir les informations du fichier de configuration.
 
 - Modifier une configuration : On peut sélectionner d'une liste la configuration que l'on souhaite modifier. Clé par clé, on peut modifier sa valeur ou laisser la précédente.

 - Lister les configurations : On peut voir tous les fichiers de configuration et leur contenu.

 - Supprimer une configuration : On peut sélectionner d'une liste la configuration que l'on souhaite supprimer.

 - Sauvegarder les configurations : Cette option permet d’enregistrer les changements (configuration créée et configurations modifiées).

 - Restaurer les configurations : Ici, on peut créer des points de sauvegarde des fichiers de configuration existants (un, plusieurs ou tous) et ajouter un commentaire. On peut aussi restaurer des configurations en sélectionnant le point de sauvegarde souhaité. De plus, on peut afficher les points de sauvegarde existants.

 - Et enfin, scanner les serveurs à l'aide de NMAP : On donne une IP ou une plage d'IPs et on obtient l'hôte avec les ports ouverts, protocole, services actifs et leur version.

## Les différents choix techniques qui ont été implémentés sont :

   - Langage utilisé : Python V 3.11

   - Stockage : Stockage en local, dans le dossier d'exécution.

   - Bibliothèques : os, json, nmap, shutil, glob, colorama, sys.

   - Intégration NMAP : Prérequis que le logiciel soit installé sur la machine hôte.

   - Interface utilisateur : Terminal avec interface conviviale.

   - Gestion des erreurs et débogage : Gestion des erreurs de saisie par avertissement et d'information manquante si nécessaire.

## Spécificités du "SERVER CONFIG" :

   - Exécutable pour Windows et Linux : S'exécute dans le dossier où il se trouve. Les dépendances pour Linux sont : Les fichiers .sh et le fichier .desktop.

   - Lors de l'ajout ou de la modification d'une configuration, cette information est stockée provisoirement dans une variable. La sauvegarde sera effective une fois les changements enregistrés avec l'option de sauvegarde (Option 5). Ce choix a été fait pour offrir une marge d'erreur à l'utilisateur, car sinon il perdrait la possibilité de rétractation une fois engagé dans la création ou la modification. Un avertissement est déclenché si l'utilisateur veut enregistrer sans avoir encore créé ou modifié un fichier.

   - Le dossier principal pour stocker les fichiers .json est le dossier où le logiciel est exécuté.

   - Le dossier pour stocker les points de restauration doit être créé manuellement ("Point_de_Restauration") avant de lancer le logiciel, sinon le logiciel le crée de façon automatique.

   - L'utilisateur est guidé à tout moment pour confirmer lorsque qu'une action importante va être réalisée ou un rappel s'affiche en cas de besoin :

     - Un rappel : Création ou modification d'un fichier de configuration n'est pas encore sauvegardé.
     - Une recommandation : "Donner au nom du fichier le même que celui du serveur".
     - Une confirmation : Suppression d'un fichier ou d'une sauvegarde.
     - Un avertissement si restauration depuis un point de sauvegarde : "!!SI LES FICHIERS EXISTENT ET ONT LE MÊME NOM ILS SERONT ÉCRASÉS!!"
     - Une confirmation de réussite quand une action est réalisée, ou confirmation que aucun changement était fait.


   - Des messages d'erreur sont affichés lorsqu'il y a des erreurs de saisie de la part de l'utilisateur.

   - Affichage adapté à la quantité de fichiers pour l'option 2. Si plus de 10, le contenu du fichier n'est pas affiché, seulement le nom.

   - Lors de la création d'un nouveau point de sauvegarde, la date et l'heure sont ajoutées au nom du dossier de point de restauration avec la possibilité de laisser un commentaire .

   - NMAP doit être installé au préalable dans le système pour que la bibliothèque nmap de Python fonctionne.

## Quelques soucis rencontrés :

  - Mise à jour de la variable json_files = [f for f in os.listdir(dir_path) if f.endswith('.json')]. Quand on efface, modifie ou crée un fichier, si cette variable n'est pas mise à jour, cela provoque des erreurs.

  - Définition de variables au préalable pour pouvoir les utiliser ensuite à l'intérieur des boucles. Exemples : data_mod = {} ; server_config = {}

  - Création des boucles pour pouvoir revenir en arrière dans le menu : pas toujours facile quand les inputs demandés à l'utilisateur sont des int ou des str, et on revient en arrière soit avec une option dans un menu, soit avec la lettre 'r'.

  - Donner une bonne mise en page pour que le logiciel soit compréhensible par l'utilisateur.

  - Dans l'option 5, si l'on sauvegarde sans être passé par l'option 1 (pour créer ou modifier un fichier), cela crée un fichier .json vide, ce qui faisait planter le reste des options. Donc comme solution j'ai du implementer la vérification de la variable (data_mod:) avant et on informe l'utilisateur qu'il n'a pas encore créé ou modifié un fichier.

  - Rendre disponibles des variables en dehors d'une fonction pour pouvoir être appelées ailleurs dans le code (avec "return"). Exemple : la liste de sous-dossiers "subfolders" et la variable path_dossier dans la fonction list_dossier_restauration(). "dossier_sauvegarde" fonction_nvo_dossier().

  - Définir un bon format pour le nom de chaque nouveau dossier de sauvegarde. Autrement, Windows ne le considère pas valide. Exemple : Pas de ':' pour l'heure.

  - Manque du "nm = nmap.PortScanner()" au début de l'option 7, autrement NMAP n'arrive pas à démarrer.

  - Pour lancer l'application depuis une clé USB sur Linux, il faut faire une démarche de permissions avant de monter la clé.

## Axes d’amélioration  

 - Mécanisme de création, modification et sauvegarde des fichiers localisés dans la même option dans le menu. Ou option de demander à la fin de la creation d'un fichier/modifications si l'on veut le/la sauvegarder.
 - Dans l'option 5, montrer le fichier que l'on va sauvegarder.
 - Le mécanisme actuel de restauration qui écrase les fichiers avec le même nom. Solution : Informer quels sont les fichiers qui vont être écrasés, et donner à choisir si oui ou non pour ces fichiers et copier-coller le reste.
 - Le nom du serveur ne peut pas être 'r', car c'est pour revenir au menu. Donc, modifier la façon de se déplacer dans les menus.
 - Aide à l'utilisateur, --HELP, exemples, etc. Option "Manuel d'utilisation".
 - Dans l'option 5, visualiser la variable avant de sauvegarder (pour l'instant, l'utilisateur doit se déplacer vers le haut pour voir ce qu'il a créé).
 - Pas d'optimisation, utiliser davantage de fonctions() pour que le code soit évolutif et plus facile à modifier.
 - On ne peut pas modifier un fichier manuellement, car on risque de ne pas avoir le bon format JSON (dictionnaire clé-valeur) et la fonction list_conf() ne fonctionne plus. Le dossier où se trouve le logiciel ne peut contenir que des fichiers JSON avec un bon formatage.
 - Une fois engagé dans une configuration, modification ou autre, on ne peut pas revenir en arrière dans le menu précédant, car il n'y a pas d'option dans le menu. Intégrer un raccourci clavier serait une solution.
 - Trier les fichiers par date de création avec "sort".
 - Vérifier si le fichier est créé correctement. Vérifier l’intégrité des fichiers (car si modifié manuellement, il y a risque de crash).
 - Vérifier si le nom du nouveau fichier créé existe déjà, et soit donner un avertissement, soit ajouter un N° 2 à la fin et informer. Pour l'instant, cela écrase le fichier existant si même nom.


