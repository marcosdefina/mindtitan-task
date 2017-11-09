
from api import app, log

@app.route('/')
def index():
    log.info('index loaded')
    return 'Hello World!'
