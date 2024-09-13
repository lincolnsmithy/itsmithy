import datetime
from flask import Flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html", title="Jinja and Flask", utc_dt=datetime.datetime.utcnow())

@app.route("/list")
def hello_world():
    #return "<p>Hello, hmmmItSmiKDKDKDthy</p>"
    items = ['Item 1', 'Item 2', 'Item 3']
    return render_template('index.html', items=items)

if __name__ == '__main__':

 app.run(debug=False,port=8080,host="0.0.0.0a")
