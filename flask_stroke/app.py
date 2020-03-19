from flask import Flask, render_template, url_for, redirect, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, EqualTo, ValidationError
from logistics_run import callin_db, calculate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'

db = SQLAlchemy(app)

class user_submit(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    race = db.Column(db.String(10), nullable=False)
    condition = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return f"user_submit('{self.age}','{self.gender}','{self.race}','{self.condition}')"

class selectionForm(FlaskForm):
    ages, genders, races, conditions = callin_db()
    age = SelectField('age', choices=ages, validators=[DataRequired()])
    gender = SelectField('gender', choices=genders, validators=[DataRequired()])
    race = SelectField('race', choices=races, validators=[DataRequired()])
    condition = SelectField('condition', choices=conditions)
    # submit = SubmitField('submit')

@app.route("/")
@app.route("/index",methods=['GET','POST'])
def index():
    form = selectionForm()
    # if request.method == 'POST':
    #     return redirect(url_for('/about'))
    # user = user_submit(age=age_val[1],gender=gen_val[1],race=race_val[1],condition=con_val[1])
    # db.session.add(user)
    # db.session.commit()
    return render_template('index.html',title='Index',form=form)


@app.route("/about")
def visitor():
    return render_template("about.html", title='About')

@app.route("/submit",methods=['POST'])
def submit():
    age_id = request.form['age']
    gen_id = request.form['gender']
    race_id = request.form['race']
    con_id = request.form['condition']
    result = calculate(age_id,gen_id,race_id,con_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)