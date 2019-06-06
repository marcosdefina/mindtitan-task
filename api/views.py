
from api import app, log
import flask

def run_classifier():
    # must do busy sleeping
    #while elapsed_time < 1 second:
    return True
def get_external_data():
    # non-busy sleeping, we are waiting for IO
    #10% chance of sleep(1 minute)
    return False

def increment_request_count(user_id):
    return 1*user_id

def request(user_id):
    run_classifier()
    get_external_data()
    new_request_count = increment_request_count(user_id)
    return new_request_count

@app.route('/')
@app.route('/<id>')
def index(id=None):
    log.info('index loaded')
    if(id and int(id) > 5):
        return "Hell Yeah!"
    else:
        return "Hello World!"





### UNDERSTANDING FLASK ###

@app.route('/landing')
def landing():
    return flask.render_template('landing.html')

@app.route('/student')
def student():
   return flask.render_template('student.html')

@app.route('/handle_data', methods=['POST'])
def handle_data():
    data = flask.request.form
    #projectpath = app.request.form['projectFilepath']
    # your code
    # return a response
    return data

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if flask.request.method == 'POST':
      result = flask.request.form
      return flask.render_template("result.html",result = result)