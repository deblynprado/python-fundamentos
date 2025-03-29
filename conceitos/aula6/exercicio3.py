from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def home():
  return "Homepage"

@app.route('/contact')
def contact():
  return "Contact: email@domain.com"

@app.route('/about')
def about() :
  return "About us"

@app.route('/info') 
def info():
  return jsonify({'version': '1.0', 'author': 'John Doe'})

@app.route('/user/<username>')
def user(username):
  return "Hello, " + username

if __name__ == '__main__':
  app.run(debug=True)