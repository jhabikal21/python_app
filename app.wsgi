#!/bin/usr/python3.5
activate_this = '/home/ubuntu/restapiservice/venv/bin/activate_this.py'
with open(activate_this) as f:
        exec(f.read(), dict(__file__=activate_this))

import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/html/restapiservice/")

from app import app as application

