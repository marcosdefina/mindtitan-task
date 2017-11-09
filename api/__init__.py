
import os
from flask import Flask

import logging
from logging.config import fileConfig

fileConfig('logging.conf')
log = logging.getLogger(__name__)

app = Flask(__name__)

if os.environ.get('DEPLOYMENT') == 'PRODUCTION':
    log.debug('Using production configuration.')
    app.config.from_object('api.config.ProductionConfig')
else:
    log.debug('Using development configuration.')
    app.config.from_object('api.config.DevelopmentConfig')


import api.views
