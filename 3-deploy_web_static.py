#!/usr/bin/python3
# Creates and distributes an archive to web servers

from fabric.api import *
from os import path
from datetime import datetime

# do_pack = __import__('1-pack_web_static').do_pack
# do_deploy = __import__('2-do_deploy_web_static').do_deploy

env.hosts = ['34.73.136.156', '35.196.227.92']
env.user = 'ubuntu'

n = datetime.now()


def do_pack():
    """Packs web_static files into .tgz file"""
    file_name = 'versions/web_static_{}{}{}{}{}{}.tgz'\
                .format(n.year, n.month, n.day, n.hour, n.minute, n.second)
    local('mkdir -p versions')
    command = local("tar -cvzf " + file_name + " ./web_static/")
    if command.succeeded:
        return file_name
    return None


def do_deploy(archive_path):
    """Deploys archive"""
    if not path.exists(archive_path):
        return False
    ret_value = True
    a = put(archive_path, '/tmp/')
    if a.failed:
        ret_value = False
    arch = archive_path.replace(".tgz", "").replace("versions/", "")
    b = run('mkdir -p /data/web_static/releases/' + arch + '/')
    if b.failed:
        ret_value = False
    c = run('tar -xzf /tmp/' + arch + '.tgz' +
            ' -C /data/web_static/releases/' + arch + '/')
    if c.failed:
        ret_value = False
    d = run('rm /tmp/' + arch + '.tgz')
    if d.failed:
        ret_value = False
    e = run('mv /data/web_static/releases/' + arch +
            '/web_static/* /data/web_static/releases/' + arch + '/')
    if e.failed:
        ret_value = False
    f = run('rm -rf /data/web_static/releases/' + arch + '/web_static')
    if f.failed:
        ret_value = False
    g = run('rm -rf /data/web_static/current')
    if g.failed:
        ret_value = False
    h = run('ln -sf /data/web_static/releases/' + arch +
            '/' + ' /data/web_static/current')
    if h.failed:
        ret_value = False
    if ret_value:
        print("All tasks succeeded!")
    return ret_value


def deploy():
    """Distribute to all servers"""
    arch_path = do_pack()
    if arch_path is None:
        return False
    return do_deploy(arch_path)
