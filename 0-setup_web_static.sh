#!/usr/bin/env bash
# Sets up web servers for the deployment of web_static

apt-get update &&
apt-get -y install nginx
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "/listen 80 default_server/a location /hbnb_static/ {\nalias /data/web_static/current;\nautoindex off;}" /etc/nginx/sites-available/default
service nginx restart
exit 0
