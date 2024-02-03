from flask import Flask

app = Flask(__name__)

@app.route('/yo')
def welcome():
  return "Welcome to the Codecademy Calculator!"
