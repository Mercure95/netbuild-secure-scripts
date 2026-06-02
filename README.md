# NetBuild Secure — Scripts

Ce dépôt centralise les scripts et configurations du projet NetBuild Secure.

## Contenu

- Scripts de hardening Cisco avec Netmiko
- Scripts de vérification de conformité
- Scripts SOAR de réponse automatique
- Règles Suricata
- Configurations VPN IPsec / WireGuard
- Scripts de test réseau et sécurité

## Structure

```text
netbuild-secure-scripts/
├── config/
│   ├── devices.yaml              # Liste des équipements réseau ciblés
│   └── hardening_profile.yaml    # Commandes de durcissement et contrôles de conformité
├── docs/
│   └── notes.md                  # Notes techniques et justification des commandes
├── scripts/
│   └── hardening_netmiko.py      # Script principal de hardening Cisco avec Netmiko
├── README.md
└── requirements.txt
