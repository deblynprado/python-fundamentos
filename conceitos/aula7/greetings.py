from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/greetings/<name>')
def greetings(name):
  return render_template('greetings.html', name=name)

if __name__ == '__main__':
  app.run(debug=True)