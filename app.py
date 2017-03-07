# coding=utf-8

from flask import Flask, jsonify, render_template
import json
from spider.barcode_spider import BarCodeSpider

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.debug = True


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/api/good/<barcode>', methods=['GET'])
def get_good(barcode):
    good = BarCodeSpider.get_good(barcode)
    return jsonify(good.__dict__)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
