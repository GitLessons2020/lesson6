from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Base action'

@app.route('/v1')
def v1():
    return 'Hello from CI with GitHub Actions by Tuzhixina'

@app.route('/v2')
def v2():
    return 'Second action'
