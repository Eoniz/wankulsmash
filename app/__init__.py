from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy

# App
app = Flask(__name__)

# Config
app.config.from_object('config')

# DB
db = SQLAlchemy(app)


@app.errorhandler(404)
def not_found(error):
    return redirect('/')


from app.mod_image.controller import mod_image
app.register_blueprint(mod_image)

db.create_all()
