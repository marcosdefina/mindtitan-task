
from api import app, log
import flask
import time
import random

### Dicctionary '(user_id, counter)' as row on global_request_counter table.
global_request_counter = {'0': 234, '1':456, '2':567, 'JoãoAlfredo': 789 }

def run_classifier():
    time.sleep(1)
    #while t < (info_lenght - 1):
     #   t0= time.clock()
    #    t= time.clock() - t0 # t is CPU seconds elapsed (floating point)
    #while elapsed_time < 1 second:
    return True
    
def get_external_data():
    #0.1% chance of request failing
    fail_key = random.randrange(1000)
    if(fail_key is 404):
        return 404

    key = random.randrange(10)
    if(key is 9):
        time.sleep(60)
    # non-busy sleeping, we are waiting for IO
    #10% chance of sleep(1 minute)

    return 200

def api_userdata_request():
    #simulates a get on api database
    return global_request_counter

def post_new_request_count(data):
    #simulates a post on api database
    global_request_counter = data
    return 200

def increment_request_count(user_id):
    
    counter_aux = api_userdata_request()
    
    for key, value in counter_aux.items():
        if(key is user_id):
            counter_aux[key] = value + 1
            return counter_aux
    
    counter_aux[user_id] = 1
    return counter_aux

def request(user_id):
    run_classifier()
    get_external_data()
    new_request_count = increment_request_count(user_id)
    return new_request_count

###LANDING PAGE###
@app.route('/')
def index():
    log.info('index loaded')
    return flask.render_template('form.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if flask.request.method == 'POST':
      result = flask.request.form
      global_request_counter = request(result['id'])
      print(result['question'])
      return flask.render_template("result.html",result = result)

@app.route('/database')
def database():
    return flask.render_template('result.html', result=global_request_counter)
