from flask import Flask,render_template

app = Flask(__name__)


@app.route('/index')
def index():
    return "hello world"

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()