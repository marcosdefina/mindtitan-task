#!/usr/bin/env python3

from api import app

app.debug = app.config['DEBUG']
app.run(host=app.config['HOST'], port=app.config['PORT'])
