from flask import Flask, render_template, url_for, redirect, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, SelectMultipleField, widgets
from wtforms.validators import DataRequired, EqualTo, ValidationError
from logistics_run import calculate, ages, genders, races, conditions, columns
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class user_submit(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    race = db.Column(db.String(10), nullable=False)
    condition = db.Column(db.String(30), nullable=False)
    def __repr__(self):
        return f"user_submit('{self.age}','{self.gender}','{self.race}','{self.condition}')"
def user_submit_query():
    return user_submit.query

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class selectionForm(FlaskForm):
    age = SelectField('age', choices=ages, validators=[DataRequired()],default='',coerce=int)
    gender = SelectField('gender', choices=genders, validators=[DataRequired()],default='')
    race = SelectField('race', choices=races, validators=[DataRequired()],default='')
    condition = SelectField('condition', choices=conditions,default='')
    submit = SubmitField('Submit')
@app.route("/")
@app.route("/home")
def index():
    form = selectionForm()
    return render_template('home.html',form=form)

@app.route("/submit", methods=['GET','POST'])
def submit():
    form = selectionForm()
    # result = calculate(age_id,gen_id,race_id,con_id)
    return render_template("submit.html",form=form)

@app.route('/predict/<data>', methods=['GET'])
def predict(data):
    inputs = json.loads(data)
    result = calculate(inputs.get('age_id'),
        inputs.get('gender_id'),
        inputs.get('race_id'),
        inputs.get('condition_id')
        )
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)