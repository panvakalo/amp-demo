import requests
from flask import Flask, render_template, request

app = Flask('VidaXL landingPage', static_url_path='/static')


@app.route("/")
def main():
    query = request.args.get('query')
    response = requests.get(
        'http://10.51.62.67:28321/api/v1/stores/nl_nl/pages/product-listings?search_text={}'.format(query))

    return render_template('main.html', items=response.json().get('product_list_items') if response else {})


if __name__ == '__main__':
    app.run()
