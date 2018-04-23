#!/bin/bash

function test_postgresql {
  args=(
   "-h '${db_server}'"
   "-d '${db}'"
   "-U '${db_user}'"
  )
  if [ "${db_port}" != "" ]; then
   args+=("-p '${db_port}'")
  fi
  eval "pg_isready ${args[@]}"
}

regex="^postgres:\/\/([^:]+)(:(.+))?@([^:]+)(:([0-9]+))?\/(.+)$"
if [[ $DATABASE_URL =~ $regex ]]
then
  db_user="${BASH_REMATCH[1]}"
  db_server="${BASH_REMATCH[4]}"
  db_port="${BASH_REMATCH[6]}"
  db="${BASH_REMATCH[7]}"
else
  >&2 echo "DATABASE_URL is not valid"
  exit 1
fi

# wait for postgres to be ready
count=0
until ( test_postgresql ) do
  ((count++))
  if [ ${count} -gt 100 ]
  then
    >&2 echo "Services didn't become ready in time"
    exit 1
  fi
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done
>&2 echo "Postgres ready - continuing"

python manage.py migrate 

if [ -z "${PORT}" ]; then 
    PORT=8000
fi

exec gunicorn excellalabs.wsgi:application --reload --bind 0.0.0.0:${PORT} --workers 3
