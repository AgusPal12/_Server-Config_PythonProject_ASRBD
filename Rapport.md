# Gestionaure des configurations de serveurs: "Server Config"

"Server Config" c'est un logiciel qui nous permet de manipuler des configuration des serveurs. Les configuration ont un format JSON, une par fichier, et contiens un dictionnaire avec les clés: {Nom su serveur: , adresse IP: , système d'exploitation: , services en cours d'exécution: }.
On peut les créer, modifier, visualiser, supprimer, sauvegarder, les restorer. En plus ell nous permets de scanner une plage d'address IP à la recherche des services et des serveurs.
Tout dans une interface accessible à tout utilisateur.

Les fonctionnalités abordes sont:
 
 - Ajouter une configuration :
Ou on va pre-remplir les informations du fichier de configuration.
 
 - Modifier une configuration : On peut sélectionner d'un liste la configuration qu'on veut modifier.

 - Lister les configurations : On peut voir toutes les fichier conf et leur contenu.

 - Supprimer une configuration : On peut sélectionner d'un liste la configuration qu'on veut supprimer.

 - Sauvegarder les configurations : Cette option nous permet d’enregistrer les changements (configuration crée et aussi les configuration modifiées).

 - Restaurer les configurations : Ici on peut créer des point de sauvegarde des fichier de configuration existants (un, plusieurs ou touts) et laisser un commentaire. Et donc, on peut aussi restorer des configuration en sélectionnant le point de sauvegarde souhaité. 

  - Et en fin Scanner les serveurs à l'aide de NMAP : On donne une IP ou une plage d'IPs et on obtiens le host avec les ports ouverts, protocol, services actives et leurs version.


  Les différents choix techniques qu'on été implémentée sont:

  Langage utilisé : Python3
  Libraries: os, json, nmap, shutil, glob, colorama

  
    Exigences fonctionnelles : ce que le logiciel est censé faire, son but et les tâches qu'il exécute.
    Exigences techniques : les spécifications techniques, telles que les langages de programmation, les frameworks, les bases de données et les systèmes d'exploitation utilisés pour développer et exécuter le logiciel.
    Interface utilisateur : la façon dont le logiciel interagit avec les utilisateurs, y compris l'interface utilisateur, l'expérience utilisateur et les fonctionnalités d'accèsibilité.
    Stockage et gestion des données : la façon dont le logiciel stocke, traite et gère les données, y compris les formats de données, les bases de données et les mesures de sécurité des données.
    Performances et scalabilité : la capacité du logiciel à gérer de grandes quantités de données, de trafic ou d'utilisateurs simultanés, et sa performance sous différents fardeaux.
    Sécurité et conformité : les mesures prises pour assurer la sécurité, l'intégrité et la conformité du logiciel aux réglementations, aux normes et aux lois applicables.
    Intégration et interoperabilité : la façon dont le logiciel interagit avec d'autres systèmes, applications ou services, et sa capacité à les intégrer de manière fluide.
    Gestion des erreurs et débogage : la capacité du logiciel à détecter, signaler et récupérer des erreurs, ainsi que ses capacités de débogage.
    Personnalisation et extension : la capacité du logiciel à être personnalisé ou étendu pour répondre à des besoins ou des exigences spécifiques.
    Support et maintenance : le niveau de soutien et de maintenance fourni par les développeurs du logiciel, y compris la documentation, les mises à jour et les corrections de bogues.
