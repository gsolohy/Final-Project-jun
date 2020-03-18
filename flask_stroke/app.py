from flask import Flask, render_template, url_for, flash, redirect
# import model_logisticsRun

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/about")
def visitor():
    return render_template("about.html", title='About')

if __name__ == '__main__':
    app.run(debug=True)