### INSTALLATION DU PROJET

## FRONT

1. Installer node.js
2. Lancer la commande
   ```
    npm i
   ```
   depuis le dossier front
3. Démarrer le projet via
   ```
   npm run start
   ```
   un nouvel onglet s'ouvre dans votre navigateur par défaut, si jamais : http://localhost:3000 par défaut

## BACKEND

1. Installer Python (avec Pip, inclus par défaut dans l'installer python)
2. Créer un environnement virtuel python et l'activer (si l'activation du venv est bloqué Set-ExecutionPolicy unrestricted)
   ```
        python -m venv ./venv
        . ./venv/Scripts/activate
   ```
3. On installe django
   ```
       pip install django
   ```
4. S'il y en a un, on installe les requirements du projet (via le fichier dans le dossier backend)
   ```
       pip install -r requirements.txt
   ```
5. On lance le serveur django
   ```
       python manage.py runserver
   ```

### COMMANDES DJANGO

## Mise à jour BDD

Lors d'une modification des modèles, il peut être nécessaire de mettre à jour la
BDD de Django, pour cela:

```
    python manage.py makemigrations
    python manage.py migrate
```

## Démarrage du serveur

Pour démarrer le serveur il suffit d'éxecuter la commande, le serveur démarre alors par défaut sur 127.0.0.1:8000,
pour indiquer une ip ou un port précis, ajouter le à la suite de la commande:

```
    python manage.py runserver [optionnel: 0.0.0.0:8000 <exemple pour un déployer sur un serveur>]
```

## Création d'un compte superuser

Afin d'accéder à l'interface de l'admin (accessible à 127.0.0.1:8000/admin ), il faut
vous créer un "superuser", pour cela

```
    python manage.py createsuperuser
```
