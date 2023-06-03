# IntegradorIngenieriaSoftware

# Orden de pasos a ejecutar 1 por 1.

python -m venv venv

source venv/Scripts/activate

pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver