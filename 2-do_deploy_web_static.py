#!/usr/bin/python3
"""
a Fabric script that distributes an archive to the web servers
"""


from fabric.api import *
from os.path import exists

env.hosts = ['3.85.196.155', '18.204.9.31']
env.user = 'ubuntu'
env.use_ssh_config = True

def do_deploy(archive_path):
    if exists(archive_path):
        filename = archive_path.split('/')[1]
        dest = '/data/web_static/releases/' + filename[:-4]
        link = '/data/web_static/current/'
        try:
            put(archive_path, '/tmp/')
            run('mkdir -p {}'.format(dest))
            run('tar -xzvf {} -C {}'.format(archive_path, dest))
            run('rm -f /tmp/{}'.format(filename))
            run('rm -rf {}'.format(link))
            run('ln -s {} {}'.format(dest, link))
            return True
        except:
            return False
    else:
        return False
