# Django Helpdesk API

Ce projet est une API REST de gestion de tickets d’assistance (helpdesk) développée avec Django et Django REST Framework.  
Elle permet aux clients de créer des tickets et aux agents de les gérer via une API sécurisée.

## Fonctionnalités

- Authentification (client / agent)
- Création, mise à jour, suppression de tickets
- Filtres par statut, priorité
- Assignation des tickets
- API REST sécurisée
- Prête à être étendue ou dockerisée

## Stack

- Python 3.x
- Django 5.x
- Django REST Framework
- Djoser (auth)

## Lancer le projet

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
