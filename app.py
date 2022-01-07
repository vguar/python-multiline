from flask import Flask

app = Flask(__name__)

@app.route('/test/')
def test():
    return 'rest'

@app.route('/honeypot/')
def test1():
    1/0
    return 'lol'