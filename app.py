import time
from flask import Flask

app = Flask(__name__, static_url_path='', static_folder='build')


@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/time')
def get_current_time():
    return {'time': time.time()}
