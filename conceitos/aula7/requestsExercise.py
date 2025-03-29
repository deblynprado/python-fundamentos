import requests
from flask import Flask, render_template, request, jsonify

url = "https://api.github.com/repositories"
response = requests.get(url)
repos = response.json()

app = Flask(__name__)
@app.route('/repositories')
def repositories():
  return render_template('repositories.html', repos=repos)

__name__ == '__main__' and app.run(debug=True)