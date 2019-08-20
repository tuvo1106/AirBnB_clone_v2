#!/usr/bin/python3
# Deletes out-of-date archives

from fabric.api import *

env.hosts = ['34.73.136.156', '35.196.227.92']
env.user = 'ubuntu'


def do_clean(number=0):
    number = int(number)
    """Cleans old archives"""
    with lcd('versions'):
        if number == 0 or number == 1:
            local('ls -t | tail -n +2 | xargs rm -rfv')
        else:
            local('ls -t | tail -n +{} | xargs rm -rfv'.format(number + 1))
    with cd('/data/web_static/releases/'):
        if number == 0 or number == 1:
            run('ls -t | tail -n +2 | xargs rm -rfv')
        else:
            run('ls -t | tail -n +{} | xargs rm -rfv'.format(number + 1))
