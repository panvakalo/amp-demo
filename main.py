import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def main():
    query = request.args.get('query') if request.args.get('query') else {}
    response = requests.get('http://10.51.62.67:28321/api/v1/stores/nl_nl/pages/product-listings?search_text={}'.format(query))

    return render_template('main.html', items=response.json().get('product_list_items') if response else {})