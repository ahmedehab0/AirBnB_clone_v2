#!/usr/bin/python3

"""
fabric script that generates .tgz archive from the contents of
the web static folder
"""


from datetime import datetime
from fabric.api import local


def do_pack():
    date = datetime.now().strftime("%Y%m%d%H%M%S")

    local("mkdir -p versions")
    filename = "versions/web_static_{}.tgz".format(date)
    result = local("tar -cvzf {} web_static".format(filename))
    if result.succeeded:
        return filename
    else:
        return None

