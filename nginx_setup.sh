#!/bin/bash

URL=nvrbckdown.uz

apt install nginx
systemctl start nginx

cd
git clone https://github.com/nvrbckdown/exadel-task2.git

cd exadel-task2
apt update && apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools

apt install python3-venv
python3 -m venv venv
source venv/bin/activate

pip install -r req.txt
pip install wheel uwsgi

deactivate

cp app.service /etc/systemd/system/

cp hello-page.nginx.conf /etc/nginx/sites-available/$URL
ln -s /etc/nginx/sites-available/$URL /etc/nginx/sites-enabled/

systemctl start app.service
