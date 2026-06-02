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
├── config
│   ├── devices.yaml
│   └── hardening_profile.yaml
├── cours_ (5).pdf
├── docs
│   └── notes.md
├── README.md
├── requirements.txt
├── scripts
│   ├── hardening_netmiko.py
│   ├── rules_suricata.rules
│   ├── soar_playbook.py
│   └── test_connectivity.sh
└── venv
    ├── bin
    ├── include
    ├── lib
    ├── lib64 -> lib
    ├── pyvenv.cfg
    └── share
