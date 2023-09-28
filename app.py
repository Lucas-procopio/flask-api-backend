from flask import Flask
from pydantic import BaseModel

def creating_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sql////tmp/crud_api.db'
    return app

@app.route('/data') #EndPoint
def extracting_data():
    return 'OK'

app.run()
