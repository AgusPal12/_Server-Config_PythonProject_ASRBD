---
title: Projet Python Gestionnaire de Configuration des Serveurs
author: Tom Avenel
date: 2024 / 2025
correction: false
---

# Projet Python - Gestionnaire de Configuration des Serveurs

## Présentation

Le but de ce projet est de créer une application en ligne de commande qui permet aux administrateurs système de gérer la configuration de plusieurs serveurs. L'application devra permettre d'ajouter, de modifier et de supprimer des configurations, ainsi que de les sauvegarder et de les restaurer.

### Objectifs pédagogiques

Ce projet vous permettra de :

- Manipuler les variables et les types de données en Python.
- Utiliser des structures de contrôle comme les conditions et les boucles.
- Gérer les entrées utilisateur.
- Gérer des fichiers en Python.

### Modules Python recommandés

- `json` ou `csv` pour la gestion des fichiers
- `argparse` pour gérer les arguments de la ligne de commande.

## Fonctionnalités

### Ajouter une configuration :

Permettre à l'utilisateur d'ajouter des configurations pour un nouveau serveur (nom, adresse IP, système d'exploitation, services en cours d'exécution, etc.).

```python
> ajouter_configuration

Entrez le nom du serveur : Serveur1
Entrez l'adresse IP : 192.168.1.10
Entrez le système d'exploitation : Ubuntu 20.04
Entrez les services en cours d'exécution (séparés par des virgules) : Apache, MySQL
Configuration ajoutée avec succès !
```

### Modifier une configuration :

Permettre à l'utilisateur de modifier les détails d'une configuration existante.

```python
> modifier_configuration

Entrez le nom du serveur à modifier : Serveur1
Entrez la nouvelle adresse IP : 192.168.1.15
Configuration mise à jour avec succès !
```

### Supprimer une configuration :

Permettre à l'utilisateur de supprimer une configuration.

```python
> supprimer_configuration

Entrez le nom du serveur à supprimer : Serveur1
Configuration supprimée avec succès !
```

### Lister les configurations :

Afficher toutes les configurations enregistrées avec leurs détails.

```python
> lister_configurations

Configurations enregistrées :
1. Serveur1
   - Adresse IP : 192.168.1.15
   - Système d'exploitation : Ubuntu 20.04
   - Services : Apache, MySQL

2. Serveur2
   - Adresse IP : 192.168.1.20
   - Système d'exploitation : CentOS 7
   - Services : Nginx
```

### Sauvegarder les configurations :

Enregistrer les configurations dans un fichier JSON ou CSV pour les sauvegarder.

```python
> sauvegarder_configurations

Entrez le nom du fichier de sauvegarde (ex: configurations.json) : sauvegarde_config.json
Configurations sauvegardées avec succès dans sauvegarde_config.json
```

### Restaurer les configurations :

Charger les configurations depuis le fichier sauvegardé pour les réintégrer dans l'application.

```python
> restaurer_configurations

Entrez le nom du fichier de sauvegarde à restaurer (ex: sauvegarde_config.json) : sauvegarde_config.json
Configurations restaurées avec succès !
```

### Découverte de Services et de Serveurs

Permettre à l'utilisateur de scanner le réseau local pour détecter les serveurs actifs et les services qu'ils exécutent :

- Scanner une plage d'adresses IP pour détecter les serveurs actifs.
- Identifier les services en cours d'exécution sur les serveurs détectés.

Vous pouvez utiliser la bibliothèque `nmap` pour scanner les ports.

```python
> decouvrir_services

Entrez la plage d'adresses IP à scanner (ex : 192.168.1.1/24) : 192.168.1.0/24
Scan en cours...

Résultats du scan :
1. Serveur actif : 192.168.1.10
   - Services détectés :
     - Port 22 : SSH
     - Port 80 : HTTP
     - Port 3306 : MySQL

2. Serveur actif : 192.168.1.20
   - Services détectés :
     - Port 80 : Nginx
```

## Évaluation

### Le rapport

Chaque groupe devra fournir un rapport résumant la réalisation de leur projet. Ce rapport est un rapport technique devant inclure :

- un court rappel du projet et des fonctionnalités attendues ;
- l'architecture de votre projet ;
- les choix techniques réalisés ;
- les spécificités de votre application ;
- les soucis rencontrés ;
- des axes d'amélioration pour le futur.

Le rendu devra également inclure le code source prêt pour la production (code nettoyé, commenté, ...).

### La soutenance

Chaque groupe devra présenter sa solution lors d'une soutenance.

Attention, il ne s'agit pas de lire le rapport ou de le recopier dans quelques slides, mais bien de présenter le projet à un jury qui ne connaîtrait pas votre réalisation. Il est fortement conseillé d'inclure une démonstration de votre rendu.

