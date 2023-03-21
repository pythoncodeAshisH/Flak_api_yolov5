from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()

    # Do something with the data
    # ...

    response = {
        'message': 'Received data successfully',
        'data': data
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
