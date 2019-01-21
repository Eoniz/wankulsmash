from flask import Flask, render_template, redirect, request
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

db.create_all()