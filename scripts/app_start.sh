#!/bin/bash
sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
sudo rm /etc/nginx/sites-enabled/default
sudo service nginx restart 

