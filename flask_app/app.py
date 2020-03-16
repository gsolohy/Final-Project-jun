from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '0fca5e0ed81befba3b266d43f1a835fe'
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

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", title='Register', form=form)

@app.route("/login")
def login():
    form = RegistrationForm()
    return render_template("login.html", title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)