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


def from_off(codeBarre):
    r = requests.get('https://world.openfoodfacts.org/api/v0/product/'+codeBarre+'.json')
    resp = r.json()
    return resp

@app.route("/api/getproduitname/<string:codeBarre>.json", methods=["GET"])
def get_name(codeBarre):
    resp = from_off(codeBarre)
    nomProduit = resp['product']['product_name']
    return json.dumps(nomProduit)

@app.route("/api/getproduitimage/<string:codeBarre>.json", methods=["GET"])
def get_image(codeBarre):
    resp = from_off(codeBarre)
    lienImage = resp['product']['image_front_url']
    return json.dumps(lienImage).strip("\"")


    
if __name__ == "__main__":
    app.run(port=80)