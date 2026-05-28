from flask import Flask, request, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/ex44')
def hello():
    return 'Hello, World!'


@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/Apple')
def apple():
    return render_template('apple.html')


@app.route('/ex47')
def show_variables():
    x = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    return render_template('page.html', x=x, text="Exercise 47 !")


@app.route('/ex48')
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    x = int(request.form["x"])
    result = x * 2
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
