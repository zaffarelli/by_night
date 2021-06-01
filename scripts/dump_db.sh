#!/bin/bash
mkdir -p ./backup/$1
echo "Collector Objects"
python ./manage.py dumpdata --format xml collector.Chronicle --output backup/$1/chronicles.xml
python ./manage.py dumpdata --format xml collector.Creature --output backup/$1/creatures.xml
python ./manage.py dumpdata --format xml collector.Rite --output backup/$1/rites.xml
python ./manage.py dumpdata --format xml collector.Gift --output backup/$1/gifts.xml
echo "Storytelling Objects"
python ./manage.py dumpdata --format xml storytelling.Story --output backup/$1/stories.xml
python ./manage.py dumpdata --format xml storytelling.Place --output backup/$1/places.xml
python ./manage.py dumpdata --format xml storytelling.Scene --output backup/$1/scenes.xml

