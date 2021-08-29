#!/usr/bin/python3
""" Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers"""

import os
from datetime import datetime
from fabric.api import *

env.host = ["34.138.245.151", "3.85.112.49"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"
env.warn_only = True


def do_pack():
    """Packs web_static into tgz"""
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = "versions/web_static_" + current_time + ".tgz"
    local("mkdir -p versions")
    local("tar -cvzf " + file_path + " web_static")
    if os.path.exists(file_path):
        return file_path
    else:
        return None


def do_deploy(archive_path):
    """Deploys archive to web servers"""
    if not os.path.exists(archive_path) and not os.path.isfile(archive_path):
        return False

    temp = archive_path.split('/')
    temp0 = temp[1].split(".")
    f = temp0[0]

    try:
        put(archive_path, '/tmp')
        run("sudo mkdir -p /data/web_static/releases/" + f + "/")
        run("sudo tar -xzf /tmp/" + f + ".tgz" +
            " -C /data/web_static/releases/" + f + "/")
        run("sudo rm /tmp/" + f + ".tgz")
        run("sudo mv /data/web_static/releases/" + f +
            "/web_static/* /data/web_static/releases/" + f + "/")
        run("sudo rm -rf /data/web_static/releases/" + f + "/web_static")
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/" + f +
            "/ /data/web_static/current")
        return True
    except:
        return False

    return True


def deploy():
    """at creates and distributes an archive to your web servers,
    using the function deploy"""

    f = do_pack()
    if f:
        deploy = do_deploy(f)
        return deploy
    else:
        return False
