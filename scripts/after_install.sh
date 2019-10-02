#!/bin/bash
# sudo systemctl daemon-reload
sudo service nginx restart
sudo service gunicorn restart
