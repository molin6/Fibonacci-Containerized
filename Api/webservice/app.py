from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

@app.route('/fibonacci', methods=['GET'])
def get_fibonacci():
    n = request.args.get('n', default=1, type=int)
    return jsonify({"nth Fibonacci Number": fibonacci(n)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
