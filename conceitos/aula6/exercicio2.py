from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
@app.route('/data', methods=['GET', 'POST'])

def home():
  return "Welcome to my program"

def data():
  if request.method == 'GET':
    return "This is a GET request"
  elif request.method == 'POST':
    return "This is a POST request"
  else:
    return "This is a INVLAID request"

if __name__ == '__main__':
  app.run(debug=True)