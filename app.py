# coding=utf-8

from flask import Flask, jsonify, render_template
import json
from spider.barcode_spider import BarCodeSpider
from functools import wraps
from flask import make_response


def allow_cross_domain(fun):
    @wraps(fun)
    def wrapper_fun(*args, **kwargs):
        rst = make_response(fun(*args, **kwargs))
        rst.headers['Access-Control-Allow-Origin'] = '*'
        rst.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
        allow_headers = "Referer,Accept,Origin,User-Agent"
        rst.headers['Access-Control-Allow-Headers'] = allow_headers
        return rst
    return wrapper_fun


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.debug = True


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/api/good/<barcode>', methods=['GET'])
@allow_cross_domain
def get_good(barcode):
    good = BarCodeSpider.get_good(barcode)
    return jsonify(good.__dict__)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
