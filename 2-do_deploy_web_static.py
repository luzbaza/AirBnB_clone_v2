#!/usr/bin/python3
""" Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers"""

import os.path
from datetime import datetime
import re
from fabric.api import *

env.host = ["34.138.245.151", "3.85.112.49"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"
env.warn_only = True


def do_deploy(archive_path):
    """ distributes an archive to your web servers"""
    if not os.path.exists(archive_path):
        return False
    archive_list = archive_path.split(".")
    archive_filename = archive_list[-1]
    filename_list = archive_filename.split(".")
    filename_noext = filename_list[0]
    result = put(archive_path, "/tmp/")
    if result.failed:
        return False
    result = run('sudo mkdir -p /data/web_static/releases/{:}'.format(
        filename_noext))
    if result.failed:
        return False
    result = run('sudo tar -xzf /tmp/{:} -C /data/web_static/releases/{:}'.format(
        archive_filename, filename_noext))
    if result.failed:
        return False
    result = run('sudo rm /tmp/{:}'.format(archive_filename))
    if result.failed:
        return False
    result = run('sudo mv /data/web_static/releases/{:}/web_static/* \
                /data/web_static/releases/{:}/'.format(
        filename_noext, filename_noext))
    if result.failed:
        return False
    result = run("sudo rm -rf /data/web_static/releases/{:}/web_static".format(
        filename_noext))
    if result.failed:
        return False
    result = run('sudo rm -rf /data/web_static/current')
    if result.failed:
        return False
    result = run(
        ' sudo ln -s /data/web_static/releases/{:}/ /data/web_static/current'.format(
            filename_noext))
    if result.failed:
        return False
    return True
