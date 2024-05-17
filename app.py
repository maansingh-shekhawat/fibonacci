from flask import Flask, jsonify, request

app = Flask(__name__)

def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 1,1
        for _ in range(n - 2):
            a, b = b, a + b
        return b

@app.route('/fibonacci', methods=['GET'])
def get_fibonacci():
    n = request.args.get('n', default = 1, type = int)
    return jsonify(fibonacci(n))

if __name__ == '__main__':
    app.run(debug=True)
