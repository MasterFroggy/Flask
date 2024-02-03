from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
  return "Welcome to Fetchtown Mess!"

@app.route('/yo')
def uhh():
  return "Yo"

app.run()