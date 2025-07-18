from app.routes.route import route 
from flask import Flask

def createApp():
    app=Flask(__name__)
    app.register_blueprint(route)
    return app 