from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/about')

def home() :
  return "Welcome to my program"

def about() :
  return "This is a basic Flask Application!"

if __name__ == '__main__':
  app.run(debug=True)