from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
prods = ["Computer", "Phone"]

@app.route('/products/<name>', methods=["GET", "POST"])
def products(name=None) :
  if request.method == "POST" :
    prods.append(name)
    return jsonify(prods)
  else :
    return jsonify(prods)
  
if __name__ == '__main__':
  app.run(debug=True)