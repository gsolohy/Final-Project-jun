from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from logistics_run import callin_db, calculate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stroke.db'
db = SQLAlchemy(app)

class user_submit(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    race = db.Column(db.String(10), nullable=False)
    condition = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return f"user_submit('{self.sub_age}','{self.sub_gender}','{self.sub_race}','{self.sub_condition}')"

def init_db():
    db.create_all()
    # Test
    new_user = user_submit(age=50,gender='Female',race='CA',condition='None')
    db.session.add(new_user)
    db.session.commit()

@app.route("/",methods=['GET','POST'])
@app.route("/index",methods=['GET','POST'])
def index():
    ages, genders, races, conditions = callin_db()
    return render_template('index.html', ages=ages, genders=genders, races=races, conditions=conditions)

@app.route("/about")
def visitor():
    return render_template("about.html", title='About')

@app.route("/submit")
def submit():
    init_db()
    result = calculate()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)