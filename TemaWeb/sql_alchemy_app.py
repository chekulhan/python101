from flask import Flask, request, render_template, redirect, url_for

from flask_sqlalchemy import *
import os
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

#with app.app_context():
#    db.create_all()

@app.route("/")
def index():
    jon = Persona()
    jon.nombre = "jon"
    db.session.add(jon)
    db.session.commit()

    return "Hola"


if __name__=="__main__":
    app.run(debug=False)
