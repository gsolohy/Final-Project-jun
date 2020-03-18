from flask import render_template, url_for, flash, redirect
from flaskapp import app
from flaskapp.forms import RegistrationForm, LoginForm
from flaskapp.models import User, Post

posts = [
    {
        'author': 'Adan',
        'title': 'Build Model',
        'content': 'working on machine learning model',
        'date_posted': 'March 14, 2020',
    },
    {
        'author': 'Allison',
        'title': 'Create Database',
        'content': 'working on database',
        'date_posted': 'March 16, 2020',
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', posts=posts)

@app.route("/visitor")
def visitor():
    return render_template("visitor.html", title='Visitor')

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!","success")
        return redirect(url_for('home'))
    return render_template("register.html", title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and/or password', 'danger')
    return render_template("login.html", title='Login', form=form)
