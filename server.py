from flask import Flask, send_from_directory
import requests
import random
import json

app = Flask(__name__)

# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('client/public', 'index.html')

# Path for all the static files (compiled JS/CSS, etc.)
@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)

@app.route("/api/getproduit/<string:codeBarre>.json", methods=["GET"])
def get_by_name(codeBarre):
    r = requests.get('https://world.openfoodfacts.org/api/v0/product/'+codeBarre+'.json')
    resp = r.json()
    nomProduit = resp['product']['product_name']
    return json.dumps(nomProduit)
    
if __name__ == "__main__":
    app.run(port=80)