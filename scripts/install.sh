#!/bin/bash

pip3 install -r requirements.txt
pip3 install django bcrypt django-extensions
pip3 install gunicorn
chown ubuntu:www-data /home/ubuntu/django_chat_app/chatpr/
