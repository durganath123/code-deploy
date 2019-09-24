#!/bin/bash

cd django_chat_app/chatpr
pip3 install virtualenv

virtualenv venv
source venv/bin/activate

sudo apt-get install python3-pip python3-dev nginx git -y
sudo apt-get update

pip3 install -r requirements.txt
pip3 install django bcrypt django-extensions
pip3 install gunicorn
chown ubuntu:www-data /django_chat_app/chatpr/

