#!/usr/bin/python2

"""
fabric script that generates .tgz archive from the contents of
the web static folder
"""


from datetime import datetime
import fabric
from fabric.contrib.console import confirm
import os


def do_pack():
    date = datetime.now().strftime("%Y%m%d%H%M%S")

    if os.isdir("versions") is False:
        local("mkdir versions")
    filename = "web_static_{}".fromat(date)
    result = local("tar -cvzf versions/{} web_static".format(filename))
    exit_status = result.return_code 
    if exit_status == 0:
        return "versions/{}".fromat(filename)
    else:
        return None

