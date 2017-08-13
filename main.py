#!/usr/bin/env python3

from worker import app

app.debug = app.config['DEBUG']
app.run(host=app.config['HOST'], port=app.config['PORT'])
