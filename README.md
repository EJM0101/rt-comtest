# 🔁 RT-ComTest — Simulateur de Communication Inter-Tâches

**RT-ComTest** est une application pédagogique qui permet de simuler différents mécanismes de **communication entre tâches** dans les systèmes temps réel ou embarqués.

---

## 🎯 Objectif pédagogique

Ce simulateur aide les étudiants et développeurs à :
- Comprendre la communication inter-tâches dans un système concurrent.
- Visualiser le comportement de tâches concurrentes via :
  - Pipe (FIFO)
  - Sémaphore (verrou)
  - File de messages (Message Queue)
  - Socket (communication bidirectionnelle)

---

## 🛠 Technologies utilisées

| Composant     | Technologie         |
|---------------|---------------------|
| Backend       | Python + Flask      |
| Communication | Flask-SocketIO      |
| Frontend      | HTML + Bootstrap    |
| Déploiement   | Render.com (Python app) |

---

## 🧪 Fonctionnalités

- Sélection du type de communication à tester.
- Simulation dynamique avec affichage dans un journal.
- Logs temps réel via WebSocket.
- Interface simple à utiliser pour TP ou démonstration.

---

## 📂 Structure du projet

```
rt-comtest/
├── app.py                # Backend Flask + SocketIO
├── templates/
│   └── index.html        # Interface web
├── static/
│   └── sim.js            # Script client WebSocket
├── requirements.txt      # Dépendances Python
└── render.yaml           # Déploiement Render
```

---

## 🔄 Types de communication simulés

### 🧵 Pipe (FIFO)
- Tâche A écrit dans un tube
- Tâche B lit dans l’ordre d’arrivée
- Communication unidirectionnelle

### 🔐 Sémaphore (Verrou)
- Tâche A prend une ressource
- Tâche B attend sa libération
- Utilisé pour la synchronisation

### 📬 File de messages (Queue)
- Tâche A dépose plusieurs messages
- Tâche B les consomme à son rythme
- Découplage temporel producteur / consommateur

### 🌐 Socket (WebSocket)
- Communication en duplex
- Simulation de dialogue A ↔ B
- Utilisé en réseau distribué

---

## 📦 Déploiement sur Render

1. Connecter à [Render.com](https://render.com)
2. Créer un nouveau service **Web (Python)**
3. Indiquer :
   - Build command : `pip install -r requirements.txt`
   - Start command : `python app.py`
4. Renseigner le **publish directory** : `.`

Ou utiliser directement le fichier `render.yaml`.

---

## 📜 Lancer localement

```bash
git clone https://github.com/EJM0101/rt-comtest
cd rt-comtest
pip install -r requirements.txt
python app.py
```

---

## 👨‍🏫 Développé par

**Emman Mlmb 🇨🇩**  
Étudiant en L3 Informatique, Université de Kinshasa  
Module : Informatique Temps Réel — Communication Inter-Tâches

---

> Ce projet est libre d'utilisation à des fins pédagogiques et démonstratives.