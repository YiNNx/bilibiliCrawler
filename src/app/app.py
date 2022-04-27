from flask import Flask
from .. import config

app = Flask(__name__)

app.config.from_object(config)

@app.route('/')
def index():
    pass