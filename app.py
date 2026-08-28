# this code is from https://github.com/LondheShubham153/flask-app-ecs/tree/main
from flask import Flask, render_template
app = Flask(_name_)


@app.route()
def hello_world():
  return render_template('index.html')

@app.route('/health')
def health():
  return 'server is up and running'
