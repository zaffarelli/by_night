#!/bin/bash

python ./manage.py makemigrations
python ./manage.py migrate
python ./manage.py collectstatic --noinput
#python ./manage.py dumpdata collector.Chronicle --format xml --output backup/chronicles.xml
#python ./manage.py dumpdata collector.Creature --format xml --output backup/creatures.xml
python ./manage.py runserver 0.0.0.0:8090