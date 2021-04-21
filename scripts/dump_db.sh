#!/bin/bash
mkdir -p ./backup/$1
python ./manage.py dumpdata --format xml collector.Chronicle --output backup/$1/chronicles.xml
python ./manage.py dumpdata --format xml collector.Creature --output backup/$1/creatures.xml
