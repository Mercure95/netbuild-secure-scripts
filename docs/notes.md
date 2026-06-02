# Notes techniques — NetBuild Secure

## Objectif du dépôt

Ce dépôt regroupe les scripts utilisés dans le projet NetBuild Secure.

## Scripts disponibles

### hardening_netmiko.py

Ce script se connecte en SSH à des équipements Cisco avec Netmiko.  
Il applique des commandes de durcissement définies dans `config/hardening_profile.yaml`.

Fonctions principales :

- Connexion SSH au switch
- Passage en mode enable
- Application des commandes de hardening
- Sauvegarde de la configuration
- Vérification de conformité
- Génération d'un rapport JSON

### soar_playbook.py

Ce script simule un playbook SOAR.

Il permet de :

- Détecter un scan réseau
- Bloquer une IP suspecte sur un pare-feu
- Envoyer une alerte Slack

### rules_suricata.rules

Ce fichier contient des règles Suricata pour détecter :

- ARP spoofing
- Port scan SYN
- Requêtes DNS vers des domaines suspects

### test_connectivity.sh

Ce script permet de tester rapidement la connectivité vers plusieurs passerelles réseau.

## Remarques

Les adresses IP, identifiants et URL d’API sont fictifs et doivent être adaptés à l’environnement de simulation.