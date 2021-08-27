#!/usr/bin/env bash

from fabric.api import local
from datetime import datetime


def do_pack():
    '''
    script that generates a .tgz archive from the contents of the web_static
    '''
    try:
        now_string = datetime.now().strftime('%Y%m%d%H%M%S')
        filename = 'versions/web_static_' + now_string + '.tgz'
        local('mkdir -p versions')
        print('Packing web_static to {}'.format(filename))
        local('tar -cvzf {} web_static'.format(filename))
    except:
        None
