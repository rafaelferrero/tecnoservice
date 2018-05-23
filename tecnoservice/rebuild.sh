#!/usr/bin/env bash

#borrar las migraciones
rm -r productos/migrations/

#borrar la base de datos
rm db.sqlite3

#recrear las migraciones
./manage.py makemigrations productos

#migrar
./manage.py migrate

#cargar los datos
./manage.py loaddata dumps/user.json

#correr el servidor
./manage.py runserver