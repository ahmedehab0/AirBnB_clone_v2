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
        '''
    Deploy archive to web server
    '''
    if not os.path.exists(archive_path):
        return False
    file_name = archive_path.split('/')[1]
    file_path = '/data/web_static/releases/'
    releases_path = file_path + file_name[:-4]
    try:
        put(archive_path, '/tmp/')
        run('mkdir -p {}'.format(releases_path))
        run('tar -xzf /tmp/{} -C {}'.format(file_name, releases_path))
        run('rm /tmp/{}'.format(file_name))
        run('mv {}/web_static/* {}/'.format(releases_path, releases_path))
        run('rm -rf {}/web_static'.format(releases_path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(releases_path))
        print('New version deployed!')
        return True
    except:
        return False
