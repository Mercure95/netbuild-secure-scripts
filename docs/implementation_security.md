## Prérequis : Installer Docker & Docker Compose (Déjà fait)
```
sudo apt update
sudo apt install docker.io docker-compose-v2 git -y
sudo systemctl enable docker
sudo systemctl start docker
```
## 1. Setup de Uptime Kuma (Port 8001) & Velociraptor (Port 8002 & 8000) : 
### 1.1 - Création du dossier pour l'infrastructure : 
```
mkdir -p ~/soc-containers/velociraptor-data
```
```
cd ~/soc-containers
```
### 1.2 - Création du server.config.yaml de Velociraptor (Génération des clés crypto) :
```
docker run --rm -v $(pwd)/velociraptor-data:/app velocidex/velociraptor config generate -i > velociraptor-data/server.config.yaml
```
#### On répond aux questions demandé pour la création du .yaml : 
[IMPORTANT] : Port 8002 -> GUI  && Port 8000 -> Frontend de l'app

### 1.3 - Création du docker-compose.yml :
```
nano docker-compose.yml
```
#### Configuration : 
[IMPORTANT]

----------------------------------------------------------------------------------------
```bash 
version: '3.8'

services:
  uptime-kuma:
    image: louislam/uptime-kuma:1
    container_name: uptime-kuma
    volumes:
      - ./uptime-kuma-data:/app/data
    ports:
      - "8001:3001" # Port externe 8001 redirigé vers le port interne 3001
    restart: unless-stopped

  velociraptor:
    image: velocidex/velociraptor:latest
    container_name: velociraptor
    volumes:
      - ./velociraptor-data:/velociraptor
    ports:
      - "8000:8000" # Port de communication pour tes agents (endpoints)
      - "8002:8889" # Port externe 8002 redirigé vers le port GUI interne 8889
    command: ["--config", "/velociraptor/server.config.yaml", "frontend"]
    restart: unless-stopped
```
----------------------------------------------------------------------------------------

### 1.5 - On lance le conteneur en fond : 
sudo docker compose up -d

## 2. Setup de Shuffle (SOAR)

Shuffle est une stack complète (incluant un backend, un frontend, une base de données OpenSearch et un cache Redis) qui se déploie de manière optimale en utilisant le dépôt Git officiel.

**1. Cloner le dépôt officiel**
Reviens à la racine de ton utilisateur et clone le dépôt Git de Shuffle :

```bash
cd ~
git clone https://github.com/Shuffle/Shuffle
cd Shuffle

```

**2. Préparer les dossiers de la base de données**
Afin d'éviter les erreurs de permissions avec les conteneurs (notamment avec OpenSearch), crée les répertoires nécessaires et attribue-leur les bons droits :

```bash
mkdir -p shuffle-database
sudo chown -R 1000:1000 shuffle-database

```

**3. Configurer le port du Frontend (8003)**
Shuffle utilise un fichier d'environnement `.env` pour sa configuration réseau et système. Tu dois modifier la variable `FRONTEND_PORT` pour utiliser le port que nous avons défini.

```bash
# Copier le fichier d'exemple pour créer le fichier .env
cp .env.example .env

# Ouvrir le fichier avec un éditeur de texte (nano)
nano .env

```

> **Note :** Dans l'éditeur texte, trouve la ligne correspondant au port et modifie-la pour qu'elle corresponde exactement à ceci :

```text
FRONTEND_PORT=8003

```

**4. Lancer l'infrastructure Shuffle**
Une fois la configuration sauvegardée, démarre l'ensemble des services en tâche de fond avec Docker Compose :

```bash
sudo docker compose up -d

```
