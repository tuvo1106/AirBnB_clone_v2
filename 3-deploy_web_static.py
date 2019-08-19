#!/usr/bin/python3
# Creates and distributes an archive to web servers

from fabric.api import *
from os import path
from datetime import datetime

do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy

n = datetime.now()
env.hosts = ['34.73.136.156', '35.196.227.92']


def deploy():
    """Distribute to all servers"""
    arch_path = do_pack()
    if not arch_path:
        return False
    return do_deploy(arch_path)
