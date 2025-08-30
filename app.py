import os
import random
import requests

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/player')
def get_player():
    return jsonify({"player":"Lamine Yamal, Raphinha, Pedri, Lewandowski"})

@app.route('/coupons')
def get_coupons():
    return jsonify({"coupons": "1% 할인, 2% 할인"})

@app.route('/order', methods = ["post"])
def order():
    data = request.get_json()
    name = data.get("name")
    type = data.get("type")
    aura = 0

    aura = int(type)
    coupon = data.get("coupon")
    coupon =int(coupon)

    aura = (1 -coupon/100) * aura

    type_name = data.get("type_name")

    return jsonify({"msg": f"{name} 님, welcome to the club, {type_name} visca barca. visca catalunia. total aura is{aura}"})

if __name__ == '__main__':
    # debug=True 모드는 개발 중에만 사용해야 합니다.
    port = int(os.environ.get("PORT",5002))
    app.run(host = "0.0.0.0", port =port, debug=False)