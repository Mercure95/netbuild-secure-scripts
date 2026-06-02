# NetBuild Secure — Scripts

Ce dépôt centralise les scripts et configurations du projet NetBuild Secure.

## Contenu

- Scripts de hardening Cisco avec Netmiko
- Scripts de vérification de conformité
- Scripts SOAR de réponse automatique
- Règles Suricata
- Configurations VPN IPsec / WireGuard
- Scripts de test réseau et sécurité

### Partie Sécurité
  - Implémentation d'un SoC
      - SIEM/EDR/XDR : Wazuh (Opensource)
      - NDR : 
         - Zeek pour l'analyse du réseau (Opensource)
         - Suricata (Moteur IDS&IPS)
      - DFIR & Threat Hunting :
         - Velociraptor by Rapid7 (Opensource)
      - SOAR & Alerting : Shuffle opéré avec Slack (Opensource)
      - Uptime Kuma : Ping le réseau pour voir ce qui est DOWN opéré avec Slack

## Structure

```text
netbuild-secure-scripts/
├── config/
│   ├── devices.yaml              # Liste des équipements réseau ciblés
│   └── hardening_profile.yaml    # Commandes de durcissement et contrôles de conformité
├── docs/
│   └── notes.md                  # Notes techniques et justification des commandes
│   └── Implementation_security.md # Comment implémenter les services & logiciels opensources   
├── scripts/
│   └── hardening_netmiko.py      # Script principal de hardening Cisco avec Netmiko
├── README.md
└── requirements.txt
