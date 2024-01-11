from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def homepage():
    return jsonify({"message": "Welcome to my shop!"})

stockList = [
    {
        'id': 0,
        'product': 'fraise',
        'reference': 'fruit-01',
        'photo': 'https://img.freepik.com/photos-gratuite/baie-fraise-levitation-fond-blanc_485709-57.jpg?w=740&t=st=1699203655~exp=1699204255~hmac=e31baca39bcdc608e322b8562bf1faede61502f794630e9f37990202e8590519',
        'quantity': 1000
    },
    {
        'id': 1,
        'product': 'orange',
        'reference': 'fruit-02',
        'photo': 'https://img.freepik.com/photos-gratuite/orange-blanc-blanc_144627-16571.jpg?w=740&t=st=1699203776~exp=1699204376~hmac=ffafcab7fe3ceb6e05f868957618977bf12e8f7dec91566e7d08a2fa09618693',
        'quantity': 100
    },
    {
        'id': 2,
        'product': 'pomme',
        'reference': 'fruit-03',
        'photo': 'https://img.freepik.com/photos-gratuite/pomme-verte-isolee-blanc_2829-9600.jpg?w=740&t=st=1699203803~exp=1699204403~hmac=6cbf2173de06a899baed27be075118d4ee5bf68618b66ef4ab450d34a006871f',
        'quantity': 5000
    },
    {
        'id': 3,
        'product': 'concombre',
        'reference': 'legume-01',
        'photo': 'https://img.freepik.com/photos-gratuite/concombre-vert_144627-21625.jpg?w=996&t=st=1699203946~exp=1699204546~hmac=5e649ffa5ba28a408f6a3f747d89d4791b9daf4ea7c8be50f2678db79db61afb',
        'quantity': 500
    },
    {
        'id': 4,
        'product': 'courgette',
        'reference': 'legume-02',
        'photo': 'https://img.freepik.com/photos-gratuite/arrangement-angle-eleve-courgettes_23-2148917717.jpg?w=900&t=st=1699204040~exp=1699204640~hmac=cda2ddea0a268ae0a5f54bfc2e7f109e72c362eef09bb178b5fbb1be9bdc87c9',
        'quantity': 1500
    },
    {
        'id': 5,
        'product': 'carotte',
        'reference': 'legume-03',
        'photo': 'https://img.freepik.com/photos-gratuite/fond-carottes_1339-3261.jpg?w=900&t=st=1699204128~exp=1699204728~hmac=b6ea4d35e78e8eef9d02841a85f2ec6bf8ad2362bc098e536c5b0499b602e3e5',
        'quantity': 5000
    }
]

@app.route('/api/v1/stocks', methods=["GET", "POST"])
def stocks():

    if request.method == "GET":
        return jsonify(stockList)
    elif request.method == "POST":
        req_body = request.json
        nextId = len(stockList)

        newStock = {
            'id':nextId,
            'product': req_body['product'],
            'reference': req_body['reference'],
            'photo': req_body['photo'],
            'quantity': req_body['quantity']
        } 
        stockList.append(newStock)

        return jsonify(newStock), 201
    else :
        return jsonify ({"error": "unknown error"}), 404

@app.route('/api/v1/stock/<int:id>', methods=["GET", "PUT", "DELETE"])
def stock(id):

    try:
        stock = stockList[id]
        if request.method == "GET":
            return jsonify(stock)
        elif request.method == "PUT":
            updated = False
            if request.json['product']!=stockList[id]['product']:
                stockList[id]['product'] = request.json['product']
                updated = True
            if request.json['reference']!=stockList[id]['reference']:
                stockList[id]['reference'] = request.json['reference']
                updated = True
            if request.json['photo']!=stockList[id]['photo']:
                stockList[id]['photo'] = request.json['photo']
                updated = True
            if request.json['quantity']!=stockList[id]['quantity']:
                stockList[id]['quantity'] = request.json['quantity']
                updated = True
            if (updated):
                return jsonify({"message": "stock updated"})
            else:
                return jsonify({"message": "stock not updated"})
            
        elif request.method == "DELETE":
            stockList.pop(id)
            return jsonify({"message": "stock deleted"})
        else :
            return jsonify ({"error": "unknown error"}), 404
        
    except Exception as e:
        return jsonify ({"error": e}), 404

app.debug = True
app.run(host='0.0.0.0', port=5000)