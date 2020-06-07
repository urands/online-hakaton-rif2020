from flask import Flask, request, jsonify, Response
from algo import address_parse

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


@app.route('/norm', methods=['POST'])
def address_normalize():
    data = request.form.get('address')
    if data is None:
        data = request.json
        if 'address' not in data:
            return Response(
                "Неверные входные параметры. Укажите 'address'",
                status=400,
            )
    address = address_parse(data)
    if address is None:
        return jsonify({'error': 'Адрес не получается восстановить'})
    return jsonify(address)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
