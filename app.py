from flask import Flask
from pydantic import BaseModel

server = Flask(__name__)

@server.get('/data')
def extracting_data():
    return 'OK'

server.run()