#!/usr/bin/env bash
#bash script that sets up my web servers for the deployment

apt-get update
apt-get -y install nginx

mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo "<html>
  <head>
  </head>
  <body>
     Holeberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

if [ -L "/data/web_static/releases/test" ];
then
	rm /data/web_static/releases/test
fi

ln -s /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i '16 i \\n\tlocation /hbnb_static {\n\talias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default

service nginx restart


