#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Esperando pelo postgress"


    while ! nc -z $SQL_HOST $SQL_PORT; do
        sleep 0.1
    done

    echo "Postgres iniciado"
fi

python -u manage.py create_db

exec "$@"