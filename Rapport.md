# Gestionaure des configurations de serveurs: "Server Config"

"Server Config" c'est un logiciel qui nous permet de manipuler des configuration des serveurs. Les configuration ont un format JSON, une par fichier, et contiens un dictionnaire avec les clés: {Nom su serveur: , adresse IP: , système d'exploitation: , services en cours d'exécution: }.
On peut les créer, modifier, visualiser, supprimer, sauvegarder, les restorer. En plus Server Config nous permets de scanner une plage d'address IP à la recherche des services et des serveurs à l'aide du NMAP.
Tout dans une interface accessible à tout utilisateur et executable de façon autonome pour Windows et Linux.

## Les fonctionnalités:
 
 - Ajouter une configuration :
Ou on va pre-remplir les informations du fichier de configuration.
 
 - Modifier une configuration : On peut sélectionner d'un liste la configuration qu'on veut modifier. Clé par clé on peut modifier sa valeur ou laisser la précédente.

 - Lister les configurations : On peut voir toutes les fichier conf et leur contenu.

 - Supprimer une configuration : On peut sélectionner d'un liste la configuration qu'on veut supprimer.

 - Sauvegarder les configurations : Cette option nous permet d’enregistrer les changements (configuration crée et aussi les configuration modifiées).

 - Restaurer les configurations : Ici on peut créer des point de sauvegarde des fichier de configuration existants (un, plusieurs ou touts) et laisser un commentaire. Et donc, on peut aussi restorer des configuration en sélectionnant le point de sauvegarde souhaité. En addition on peut afficher les points de sauvegarde existants.

  - Et en fin Scanner les serveurs à l'aide de NMAP : On donne une IP ou une plage d'IPs et on obtiens le host avec les ports ouverts, protocol, services actives et leurs version.

  

  ## Les différents choix techniques qu'on été implémentée sont:

   - Langage utilisé : Python V 3.11

   - Stockage : Stockage en local, dans le dossier d'execution.

   - Libraries: os, json, nmap, shutil, glob, colorama.

   - Intégration NMAP : Prérequis que le logiciel soit installé dans la machine host.

   - Interface utilisateur : Terminal avec interface "user friendly".

   - Gestion des erreurs et débogage : Gestion des erreurs de saisie par advertisement et d'information manquante si besoin.

  ## Spécificités du "SERVER CONFIG" :

   - Executable pour Windows et Linux : Va s'executer dans le dossier où il se trouve. Les dépendances pour Linux sont : Les fichier .sh et le fichier .desktop
  
   - Au moment d'ajouter ou modifier une configuration, cette information est stocké provisoirement dans une variable. La sauvegarde sera effective une fois les changement seront enregistré avec l'option de sauvegarde (Option 5). On a fait ce choix pour donner à l'utilisateur une marge d'erreur, sinon il perdra la possibilité de retraction une fois engagé a la creation ou a la modification. Un advertisement est déclenché si l'utilisateur veut enregistrer et n'a pas encore crée ou modifié un fichier.

   - Dossier principal pour stocker les fichier .json est le dossier ou le logiciel est exécuté.

   - Dossier pour stocker les points de restoration a besoin d'être crée manuellement 
   ("Point_de_Restauration") avant de lancer le logiciel.

   - L'utilisateur est guidé à tout moment pour donner une confirmations lorsque une action importante va être réalisé ou un rappel en cas de besoin:

     - Un rappel : Creation ou modification d'un fichier conf pas encore sauvegardé.
     - Une recommendation : "Donner au nom du fichier le même que ce du serveur".
     - Une confirmation : Suppression d'un fichier ou une sauvegarde.
     - Un advertisement si restoration depuis un point de sauvegarde : "!!SI LES FICHIERS EXISTENT ET ONT LE MÊME NOM ILS SERONT ÉCRASÉ!!"
     - Une confirmation de réussite quand une actions est réalisé. 

   - Des messages d'erreur sont affichée lorsque il y a des erreur de saisie de part de l'utilisateur.
   
   - Affichage adapté a la quantité des fichiers. Si plus de 10, l'information du contenu n'est pas affichée, juste le nom du fichier.
   
   - Au moment de créer un nouveau point de sauvegarde, la date/heure seront ajoutés au nom du dossier de oint de restauration.

   - NMAP  a besoin d'être installé au préalable dans le système pour que la librairie nmap de Python puisse fonctionner.
   

  
## Quelques soucis rencontrés:

  - Mise au jour de la variable json_files = [f for f in os.listdir(dir_path) if f.endswith('.json')] . Quand on efface, modifie ou crée un fichier, si cette variable n'est pas mis au jour ça nous provoque des erreurs.

  - Definition de variables au préalable pour pouvoir les utiliser apres à l'interior des boucles. Exemples : data_mod = {} ; server_config = {}

  - Creation des boucles pour pouvoir revenir en arrière dans le menu pas toujours facile quand les inputs demandés sont int ou str, et on reviens en arrière soit avec une option dans un menu, soit avec la lettre 'r'.

  - Donner un bon format pour que soit compressible par l'utilisateur.  

  - Dans l'option 5, si on sauvegardé sans avoir passé par l'option 1 (pour créer ou modifier un fichier) il créé un fichier .json vide, ce qui faisait planter le reste des options. Donc on vérifie la variable(data_mod:) avant et on informe l'utilisateur s'il n'a pas encore créé ou modifié un fichier.

  - Rendre disponible des variables de hors une function pour pouvoir être appelé dans une autre part du code (avec "return"). Exemple : la liste de sub-dossiers "subfolders" et la variable path_dossier dans la function list_dossier_restauration(). "dossier_sauvegarde" fonction_nvo_dossier().

  - Définir un bon format pour le nom de chaque nouveau dossier de sauvegarde. Autrement Windows ne le considère pas valide. Exemple : Pas de ':' pour l'heure.         

  - Manque du "nm = nmap.PortScanner()" au debut de l'option 7, autrement NMAP n'arrive pas a démarrer.

  - Pour lancer l'application depuis une clé USB en Linux il faut faire une demarche des permissions avant de monter la clé.


## Axes d’amélioration  


 - Mécanisme de creation et modification et sauvegarde des fichier localisés dans la même option dan le menus. Ou option de demander à la fin si on veut sauvegarder le nouveau fichier/modifications.
 - Dans l'option 5, montrer le fichier q'on va sauvegarder avant de le faire.
 - Mécanisme actuel de restauration écrase les fichiers avec le même nom. Solution: Informer le quel son les fichiers qui va écraser, et donner a choisir si oui ou non pour ces fichier et copier coller le rest.
 - Nom du serveur ne peut pas être 'r'. car c'est pour revenir au menu. Donc Modifier la façon de se déplacer dans le menus.
 - Aide à l'utilisateur, --HELP , exemples, etc. Option "Manuel d'utilisation".
 - Dans l'option 5, visualiser la variable avant la sauvegarder. (pour l'instant il faut que l'utilisateur se déplace vers le haut pour voir ce qu'il a crée).
 - Pas d'optimisation, utiliser plus de functions() pour que le code soit scalable et plus facile à modifier.
 - On ne peut pas modifier un fichier à la main, car si on n'a pas le bon format json (dictionnaire key value) la function list_conf() ne fonctionne plus. Donc le dossier où se trouve le logiciel ne peut contenir que des fichiers json avec un bon format.
 - Une fois qu'on s'engage dans une config, modif ou autres, on ne peut pas revenir en arrière. Car pas d'option dans le menu. Intégrer un raccourci clavier serait une solution.  
 - Trier les fichiers par date de creation avec "sort".
 - Dans l'option 5, montrer le fichier q'on va sauvegarder avant de le faire.
 - Verifier si le fichier est crée correctement. Verifier l’intégrité des fichier (car si modifié manuellement il y a risque de crash).
 - Verifier si nom du Nouveau fichier crée existe déjà, et soit donner un advertisement, soit ajouter un N° 2 a la fin et informer. Pour l'instance ça écrase le fichier existent si même nom.











