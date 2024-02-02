#!/usr/bin/python2

"""
fabric script that generates .tgz archive from the contents of
the web static folder
"""


from datetime import datetime
from fabric.api import local


def do_pack():
    date = datetime.now().strftime("%Y%m%d%H%M%S")

    local("mkdir -p versions")
    filename = "web_static_{}.tgz".format(date)
    result = local("tar -cvzf versions/{} web_static".format(filename))
    exit_status = result.return_code 
    if exit_status == 0:
        return "versions/{}".format(filename)
    else:
        return None

